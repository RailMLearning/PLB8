import unittest
from utils.history_api import get_currency_history

class TestHistoryAPI(unittest.TestCase):
    def test_history_usd(self):
        points = get_currency_history("USD", days=10)
        self.assertIsInstance(points, list)
        if points:
            self.assertIn("date", points[0])
            self.assertIn("value", points[0])

    def test_history_invalid_code(self):
        points = get_currency_history("XXX", days=10)
        self.assertEqual(points, [])
