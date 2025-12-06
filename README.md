Нуриахметов Раиль P3121

Цель работы
Создать простое клиент‑серверное приложение на Python без серверных фреймворков.

Освоить работу с HTTPServer и маршрутизацию запросов.

Применять шаблонизатор Jinja2 для отображения данных.

Реализовать модели предметной области (User, Currency, UserCurrency, App, Author) с геттерами и сеттерами.

Структурировать код в соответствии с архитектурой MVC.

Получать данные о курсах валют через функцию get_currencies и отображать их пользователям.

Реализовать функциональность подписки пользователей на валюты и отображение динамики их изменения.

Научиться создавать тесты для моделей и серверной логики.



Описание предметной области
В предметной области рассматриваются пользователи и их подписки на валюты.

User — хранит информацию о пользователе (id, имя, email).

Currency — хранит данные о валюте (код, название, текущий курс).

UserCurrency — связывает пользователя с выбранными валютами.

App — основной класс приложения, управляющий моделями и логикой.

Author — информация об авторе приложения.

Связи:

Один пользователь может подписаться на несколько валют.

Валюта может быть выбрана многими пользователями.

App управляет взаимодействием между моделями и контроллером.



```
LB8/
 ├── models/              # модели предметной области
 │   ├── user.py
 │   ├── currency.py
 │   ├── user_currency.py
 │   ├── app.py
 │   └── author.py
 ├── utils/               # вспомогательные функции
 │   ├── currencies_api.py
 │   └── history_api.py
 ├── templates/           # HTML-шаблоны Jinja2
 │   ├── index.html
 │   ├── users.html
 │   ├── currencies.html
 │   └── author.html
 ├── tests/               # тесты
 │   ├── test_models.py
 │   ├── test_utils.py
 │   ├── test_controller.py
 │   └── test_templates.py
 ├── myapp.py             # основной контроллер HTTPServer
 └── README.md            # отчёт
```



Описание реализации
Модели: каждая модель реализована как класс с геттерами и сеттерами для доступа к свойствам.

Маршруты: в myapp.py используется HTTPServer и BaseHTTPRequestHandler. Примеры маршрутов:

/ — главная страница

/users — список пользователей

/currencies — список валют

/user?id=... — информация о конкретном пользователе

Jinja2: инициализация через Environment(loader=FileSystemLoader("templates")). Шаблоны рендерятся с передачей данных из моделей.

get_currencies: функция в utils/currencies_api.py, получает актуальные курсы валют через API и передаёт их в шаблоны.



Примеры работы приложения

/ — главная страница
<img width="823" height="434" alt="изображение" src="https://github.com/user-attachments/assets/5d594554-f2db-4ced-94b4-f8cee6bf5e28" />

/users — список пользователей
<img width="1119" height="494" alt="изображение" src="https://github.com/user-attachments/assets/59c68027-efdb-46d6-9b44-a7786843c0bc" />

/currencies — список валют
<img width="1092" height="1283" alt="изображение" src="https://github.com/user-attachments/assets/4b61dbf9-a32c-4de4-8c3e-6848985e0e9c" />

/user?id=... — страница конкретного пользователя
<img width="1046" height="975" alt="изображение" src="https://github.com/user-attachments/assets/e7c1d30c-f243-4a62-aaba-1fb6e082b233" />

Пример данных из консоли
```
C:\Users\Rail\PycharmProjects\LB8\.venv\Scripts\python.exe C:\Users\Rail\PycharmProjects\LB8\myapp.py 
server is running on http://localhost:8080
127.0.0.1 - - [06/Dec/2025 04:50:29] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:51:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:51:32] "GET /users HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:51:41] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:51:43] "GET /currencies HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:51:44] "GET /history?code=USD HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:51:44] "GET /history?code=EUR HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:52:12] "GET /users HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:52:14] "GET /user?id=1 HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:52:14] "GET /history?code=USD HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 04:52:14] "GET /history?code=EUR HTTP/1.1" 200 -
```



<img width="2361" height="1326" alt="изображение" src="https://github.com/user-attachments/assets/d799d005-8a06-474d-99b3-6c7dbf6a78d9" />
<img width="2378" height="754" alt="изображение" src="https://github.com/user-attachments/assets/3d0b14a3-3636-4519-95a4-842196b8fcc3" />

В реализации функции get_currency_history для получения истории курсов валют ЦБ РФ применяются следующие библиотеки:

datetime (стандартная библиотека Python)

Используется для работы с датами и диапазонами (date.today(), timedelta).

Позволяет вычислить начальную и конечную дату периода (например, последние 90 дней).

Форматирует даты в нужный вид для запроса к API ЦБ РФ (DD/MM/YYYY).

typing (стандартная библиотека Python)

Применяется для аннотаций типов (Dict, List, Optional).

Делает код более читаемым и удобным для проверки статическими анализаторами.

requests

Используется для выполнения HTTP‑запроса к API ЦБ РФ (XML_dynamic.asp).

Позволяет отправить GET‑запрос, получить XML‑ответ и проверить статус ответа (resp.raise_for_status()).

xml.etree.ElementTree (ET)

Применяется для парсинга XML‑ответа от ЦБ РФ.

Позволяет извлекать записи <Record> с датой, номиналом и значением курса.

Используется для преобразования данных в удобный формат (список словарей с датой и значением).



Тестирование
Назначение тестов
Для проверки корректной работы приложения реализован набор модульных и интеграционных тестов с использованием библиотеки unittest. Тесты охватывают:

маршруты HTTP‑сервера (test_controller.py)

обработку истории курсов валют (test_history.py)

модели предметной области (test_models.py)

шаблоны Jinja2 (test_templates.py)

API получения курсов валют (test_utils.py)

Структура тестов
test_controller.py — запускает сервер на localhost:8081 и проверяет маршруты /, /users, /currencies, /user?id=1.

test_history.py — проверяет функцию get_currency_history на валидный и несуществующий код валюты.

test_models.py — тестирует классы Author, App, User, Currency, UserCurrency.

test_templates.py — проверяет рендеринг шаблонов index.html, users.html, user.html.

test_utils.py — проверяет функцию get_currencies на корректную работу и обработку ошибок.

Примеры кода
Тест маршрута /users
```
def test_users_route(self):
    r = requests.get("http://localhost:8081/users")
    self.assertEqual(r.status_code, 200)
    self.assertIn("Пользователи", r.text)
```

Тест модели Currency
```
def test_currency(self):
    c = Currency("R01235", "840", "USD", "Доллар США", 90.5, 1)
    self.assertEqual(c.char_code, "USD")
    self.assertEqual(c.value, 90.5)
    self.assertEqual(c.nominal, 1)
```

Тест шаблона user.html
```
def test_user_template(self):
    template = env.get_template("user.html")
    html = template.render(user={"name": "Jane Doe", "id": "1"}, currencies=[])
    self.assertIn("Jane Doe", html)
    self.assertIn("Нет подписок", html)
```

Выводы тестов из консоли
```
127.0.0.1 - - [06/Dec/2025 05:07:59] "GET /currencies HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 05:08:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 05:08:03] "GET /user?id=1 HTTP/1.1" 200 -
127.0.0.1 - - [06/Dec/2025 05:08:05] "GET /users HTTP/1.1" 200 -
Ran 4 tests in 8.641s
OK

Ran 2 tests in 0.274s
OK

Ran 5 tests in 0.002s
OK

Ran 3 tests in 0.006s
OK

Ran 2 tests in 0.511s
OK
```



Выводы
Какие проблемы возникли при реализации
Возникли сложности с настройкой маршрутов и корректной обработкой параметров в URL (например, user?id=...).

Были трудности с парсингом XML‑ответов от API ЦБ РФ, особенно при преобразовании значений с запятой в float.

При тестировании возникали конфликты портов при запуске HTTPServer, что потребовало переноса на другой порт (8081).

При работе с шаблонами Jinja2 потребовалось точно контролировать передаваемые переменные, иначе шаблоны не рендерились корректно.
