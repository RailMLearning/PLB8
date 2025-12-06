"""Утилита для получения курсов валют с API ЦБ РФ."""

from typing import List, Dict
import requests


def get_currencies(
    currency_codes: List[str],
    url: str = "https://www.cbr-xml-daily.ru/daily_json.js"
) -> Dict[str, float]:
    """Получает курсы валют с API ЦБ РФ.

    Args:
        currency_codes: Список символьных кодов валют (например, ["USD", "EUR"]).
        url: Адрес API (по умолчанию официальный ЦБ РФ).

    Returns:
        Словарь вида {"USD": 93.25, "EUR": 101.7}.

    Raises:
        ConnectionError: Если API недоступен.
        ValueError: Если JSON некорректный.
        KeyError: Если нет ключа 'Valute' или валюта отсутствует.
        TypeError: Если курс валюты имеет неверный тип.
    """
    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as exc:
        raise ConnectionError("API недоступен") from exc

    try:
        data = response.json()
    except Exception as exc:
        raise ValueError("Некорректный JSON") from exc

    if "Valute" not in data:
        raise KeyError("Нет ключа 'Valute' в ответе API")

    valute = data["Valute"]
    result: Dict[str, float] = {}

    for code in currency_codes:
        if code not in valute:
            raise KeyError(f"Валюта {code} отсутствует в ответе API")

        value = valute[code]["Value"]
        if not isinstance(value, (int, float)):
            raise TypeError(f"Курс валюты {code} имеет неверный тип: {type(value)}")

        result[code] = float(value)

    return result
