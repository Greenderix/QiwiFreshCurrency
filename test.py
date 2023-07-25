import unittest
import api_cbr
from exceptions import IncorrectCodeError, IncorrectDateError


class TestApiCbr(unittest.TestCase):
    def test_get_currency_rate_valid(self):
        code = 'USD'
        date = '2022-10-08'
        value, name = api_cbr.get_currency_rate(code, date)
        self.assertEqual(value, '61,2475')
        self.assertEqual(name, 'Доллар США')

    def test_get_currency_rate_invalid_code(self):
        code = 'INVALID'
        date = '2022-08-10'
        with self.assertRaises(IncorrectCodeError):
            api_cbr.get_currency_rate(code, date)

    def test_get_currency_rate_invalid_date(self):
        code = 'USD'
        date = '88-10-2022'
        with self.assertRaises(IncorrectDateError):
            api_cbr.get_currency_rate(code, date)

    def test_get_currency_rate_invalid_month(self):
        code = 'USD'
        date = '08-13-2022'
        with self.assertRaises(IncorrectDateError):
            api_cbr.get_currency_rate(code, date)

    def test_get_currency_rate_invalid_year_future(self):
        code = 'USD'
        date = '08-12-2050'
        with self.assertRaises(IncorrectDateError):
            api_cbr.get_currency_rate(code, date)

    def test_get_currency_rate_invalid_year_not_4_symbols(self):
        code = 'USD'
        date = '08-12-100'
        with self.assertRaises(IncorrectDateError):
            api_cbr.get_currency_rate(code, date)

    def test_get_currency_rate_invalid_date_string(self):
        code = 'USD'
        date = 'INVALID'
        with self.assertRaises(IncorrectDateError):
            api_cbr.get_currency_rate(code, date)


if __name__ == '__main__':
    unittest.main()
