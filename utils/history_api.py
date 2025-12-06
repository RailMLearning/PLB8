"""Реальная история курсов ЦБ РФ за диапазон дат, один запрос на период + кэш."""

from datetime import date, timedelta
from typing import Dict, List, Optional
import requests
import xml.etree.ElementTree as ET

# Простой кэш в памяти: {char_code: {"date_from": str, "date_to": str, "points": List[...]} }
_HISTORY_CACHE: Dict[str, Dict[str, object]] = {}

# Карта символьного кода в VAL_NM_RQ (идентификатор валюты на сайте ЦБ)
VALUTE_ID_MAP: Dict[str, str] = {
    "USD": "R01235",
    "EUR": "R01239",
}


def history_cache_get(char_code: str) -> Optional[List[Dict[str, float]]]:
    entry = _HISTORY_CACHE.get(char_code)
    if not entry:
        return None
    return entry.get("points")  # type: ignore


def history_cache_put(char_code: str, points: List[Dict[str, float]], date_from: str, date_to: str) -> None:
    _HISTORY_CACHE[char_code] = {"date_from": date_from, "date_to": date_to, "points": points}


def _format_cbr_date(d: date) -> str:
    # ЦБ ждёт формат DD/MM/YYYY
    return f"{d.day:02}/{d.month:02}/{d.year}"


def get_currency_history(char_code: str, days: int = 90) -> List[Dict[str, float]]:
    """Получить историю курса за последние days дней (каждый доступный день) одним запросом к XML_dynamic.asp."""
    if char_code not in VALUTE_ID_MAP:
        return []

    today = date.today()
    start = today - timedelta(days=days)
    date_from = _format_cbr_date(start)
    date_to = _format_cbr_date(today)

    # Если в кэше уже есть и диапазон совпадает — отдаём кэш
    cached = _HISTORY_CACHE.get(char_code)
    if cached and cached.get("date_from") == date_from and cached.get("date_to") == date_to:
        return cached.get("points", [])  # type: ignore

    url = (
        "https://www.cbr.ru/scripts/XML_dynamic.asp"
        f"?date_req1={date_from}&date_req2={date_to}&VAL_NM_RQ={VALUTE_ID_MAP[char_code]}"
    )

    points: List[Dict[str, float]] = []
    try:
        resp = requests.get(url, timeout=4)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)

        # Формат XML: <Record Date="02.12.2025" Id="R01235"><Nominal>1</Nominal><Value>93,1234</Value></Record>
        for record in root.findall("Record"):
            date_str = record.attrib.get("Date")  # DD.MM.YYYY
            nominal_text = (record.findtext("Nominal") or "1").strip()
            value_text = (record.findtext("Value") or "").strip()

            if not date_str or not value_text:
                continue

            try:
                nominal = float(nominal_text.replace(",", "."))
                value = float(value_text.replace(",", "."))
                # Приводим к номиналу 1
                value_per_one = value / nominal if nominal else value
                # Преобразуем дату в ISO YYYY-MM-DD
                d, m, y = date_str.split(".")
                iso = f"{y}-{m}-{d}"
                points.append({"date": iso, "value": round(value_per_one, 4)})
            except Exception:
                continue

        # Сортировка по дате
        points.sort(key=lambda x: x["date"])

    except Exception:
        # Если запрос не удался, не ломаем UI: возвращаем пустой список
        points = []

    # Кладём в кэш (даже пустое), чтобы не спамить API
    history_cache_put(char_code, points, date_from, date_to)
    return points
