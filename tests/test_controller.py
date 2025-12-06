import unittest
import threading
import requests
from http.server import HTTPServer
from myapp import SimpleHTTPRequestHandler

class TestControllerIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("localhost", 8081), SimpleHTTPRequestHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever)
        cls.thread.daemon = True
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join()

    def test_index_route(self):
        r = requests.get("http://localhost:8081/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("CurrenciesListApp", r.text)

    def test_users_route(self):
        r = requests.get("http://localhost:8081/users")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Пользователи", r.text)

    def test_currencies_route(self):
        r = requests.get("http://localhost:8081/currencies")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Текущие курсы валют", r.text)

    def test_user_route(self):
        r = requests.get("http://localhost:8081/user?id=1")
        self.assertEqual(r.status_code, 200)
        self.assertIn("Jane Doe", r.text)
