import unittest
from homeworks.hw20.bank import Bank, CurrencyConverter, Person


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_register_client_positive(self):
        result = self.bank.register_client(1, "Ivan")
        self.assertTrue(result)

    def test_register_client_duplicate(self):
        self.bank.register_client(1, "Ivan")
        result = self.bank.register_client(1, "Ivan")
        self.assertFalse(result)

    def test_open_deposit_positive(self):
        self.bank.register_client(2, "Anna")
        result = self.bank.open_deposit_account(2, 1000, 1)
        self.assertTrue(result)
        self.assertIsNotNone(self.bank.clients[2]['deposit'])

    def test_open_deposit_for_unregistered_client(self):
        result = self.bank.open_deposit_account(999, 500, 1)
        self.assertFalse(result)

    def test_open_deposit_when_already_exists(self):
        self.bank.register_client(3, "Maksim")
        self.bank.open_deposit_account(3, 1000, 2)
        result = self.bank.open_deposit_account(3, 500, 1)
        self.assertFalse(result)

    def test_calc_interest_positive(self):
        self.bank.register_client(4, "Maria")
        self.bank.open_deposit_account(4, 1000, 1)
        result = self.bank.calc_interest_rate(4)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 1000)

    def test_calc_interest_for_unregistered(self):
        result = self.bank.calc_interest_rate(999)
        self.assertFalse(result)

    def test_close_deposit_positive(self):
        self.bank.register_client(5, "Vladimir")
        self.bank.open_deposit_account(5, 2000, 2)
        amount = self.bank.close_deposit(5)
        self.assertIsInstance(amount, float)
        self.assertEqual(self.bank.clients[5]['deposit'], None)

    def test_close_deposit_unregistered(self):
        result = self.bank.close_deposit(999)
        self.assertFalse(result)

    def test_exchange_currency_usd_to_eur(self):
        converter = CurrencyConverter()
        amount, currency = converter.exchange_currency('USD', 10, 'EUR')
        self.assertEqual(currency, 'EUR')
        self.assertIsInstance(amount, float)
        self.assertGreater(amount, 0)

    def test_exchange_currency_unsupported(self):
        converter = CurrencyConverter()
        with self.assertRaises(ValueError):
            converter.exchange_currency('XYZ', 10)

    def test_person_initialization(self):
        person = Person('USD', 100)
        self.assertEqual(person.currency, 'USD')
        self.assertEqual(person.amount, 100)


if __name__ == '__main__':
    unittest.main()
