import unittest
from utils import currencies_api

class TestCurrenciesAPI(unittest.TestCase):
    def test_get_currencies_ok(self):
        result = currencies_api.get_currencies(["USD", "EUR"])
        self.assertIn("USD", result)
        self.assertIn("EUR", result)
        self.assertIsInstance(result["USD"], float)

    def test_get_currencies_invalid(self):
        with self.assertRaises(KeyError):
            currencies_api.get_currencies(["XXX"])
