import unittest
from models.author import Author
from models.app import App
from models.user import User
from models.currency import Currency
from models.user_currency import UserCurrency

class TestModels(unittest.TestCase):
    def test_author(self):
        a = Author("Rail", "P3121")
        self.assertEqual(a.name, "Rail")
        self.assertEqual(a.group, "P3121")

    def test_app(self):
        a = Author("Rail", "P3121")
        app = App("TestApp", "1.0", a)
        self.assertEqual(app.name, "TestApp")
        self.assertEqual(app.version, "1.0")
        self.assertEqual(app.author.name, "Rail")

    def test_user(self):
        u = User("Jane Doe", "1")
        self.assertEqual(u.name, "Jane Doe")
        self.assertEqual(u.id, "1")

    def test_currency(self):
        c = Currency("R01235", "840", "USD", "Доллар США", 90.5, 1)
        self.assertEqual(c.char_code, "USD")
        self.assertEqual(c.value, 90.5)
        self.assertEqual(c.nominal, 1)

    def test_user_currency(self):
        uc = UserCurrency("1", "1", "R01235")
        self.assertEqual(uc.id, "1")
        self.assertEqual(uc.user_id, "1")
        self.assertEqual(uc.currency_id, "R01235")
