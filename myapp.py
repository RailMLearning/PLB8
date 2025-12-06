"""HTTP-сервер приложения: маршрутизация, шаблоны и API истории."""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from typing import Dict, List
import json
from jinja2 import Environment, PackageLoader, select_autoescape

from models import Author, User, Currency, UserCurrency, App
from utils.currencies_api import get_currencies
from utils.history_api import get_currency_history, history_cache_get

# Jinja2
env = Environment(loader=PackageLoader("myapp"), autoescape=select_autoescape())
template_index = env.get_template("index.html")
template_users = env.get_template("users.html")
template_user = env.get_template("user.html")
template_currencies = env.get_template("currencies.html")
template_author = env.get_template("author.html")

# Данные
main_author = Author("Nuriakhmetov Rail", "P3121")
app = App("CurrenciesListApp", "1.0", main_author)

users: List[User] = [User("Jane Doe", "1"), User("John Doe", "2")]

CURRENCY_META: Dict[str, Dict[str, str]] = {
    "USD": {"id": "R01235", "num_code": "840", "name": "Доллар США"},
    "EUR": {"id": "R01239", "num_code": "978", "name": "Евро"},
}

user_currencies: List[UserCurrency] = [
    UserCurrency("1", "1", "R01235"),
    UserCurrency("2", "2", "R01239"),
    UserCurrency("3", "1", "R01239"),
]


def load_currencies_from_api() -> List[Currency]:
    rates = get_currencies(list(CURRENCY_META.keys()))
    return [
        Currency(meta["id"], meta["num_code"], code, meta["name"], rates[code], 1)
        for code, meta in CURRENCY_META.items()
    ]


currencies_cache: List[Currency] = load_currencies_from_api()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        try:
            if path == "/":
                html = template_index.render(
                    myapp=app.name,
                    author_name=app.author.name,
                    group=app.author.group,
                    navigation=[
                        {"caption": "Пользователи", "href": "/users"},
                        {"caption": "Валюты", "href": "/currencies"},
                        {"caption": "Автор", "href": "/author"},
                    ],
                )
                self._send_html(html)

            elif path == "/users":
                html = template_users.render(users=users)
                self._send_html(html)

            elif path == "/user":
                uid = query.get("id", [""])[0]
                user = next((u for u in users if u.id == uid), None)
                if not user:
                    self.send_error(404, "User not found")
                    return
                subs = [
                    c for uc in user_currencies if uc.user_id == uid
                    for c in currencies_cache if c.id == uc.currency_id
                ]
                html = template_user.render(user=user, currencies=subs)
                self._send_html(html)

            elif path == "/currencies":
                refresh = query.get("refresh", ["0"])[0] == "1"
                global currencies_cache
                if refresh:
                    try:
                        currencies_cache = load_currencies_from_api()
                    except Exception:
                        pass
                html = template_currencies.render(currencies=currencies_cache, refreshed=refresh)
                self._send_html(html)

            elif path == "/author":
                html = template_author.render(author=main_author)
                self._send_html(html)

            elif path == "/history":
                code = query.get("code", [""])[0]
                if not code:
                    self.send_error(400, "Missing code")
                    return

                # Быстрый ответ: сначала пытаемся отдать из кэша
                cached = history_cache_get(code)
                if cached is not None:
                    self._send_json(cached)
                    return

                # Если нет в кэше — получаем, кладём в кэш и отдаём
                points = get_currency_history(code)
                self._send_json(points)

            else:
                self.send_error(404, "Not Found")

        except Exception as e:
            # Не даём соединению "рваться": отвечаем 500 JSON/HTML без задержек
            self.send_error(500, f"Internal Server Error: {e}")

    def _send_html(self, html: str) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def _send_json(self, obj) -> None:
        payload = json.dumps(obj, ensure_ascii=False)
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(payload.encode("utf-8"))


def run() -> None:
    httpd = HTTPServer(("localhost", 8080), SimpleHTTPRequestHandler)
    print("server is running on http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
