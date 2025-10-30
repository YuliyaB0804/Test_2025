class Deposit:
    def __init__(self, start_balance, years):
        self.start_balance = start_balance
        self.years = years


class Bank:
    def __init__(self):
        self.clients = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            return False
        self.clients[client_id] = {'name': name, 'deposit': None}
        return True

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            return False
        if self.clients[client_id]['deposit'] is not None:
            return False
        deposit = Deposit(start_balance, years)
        self.clients[client_id]['deposit'] = deposit
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            return False
        deposit = self.clients[client_id].get('deposit')
        if deposit is None:
            return False
        interest_rate = 0.10
        months = deposit.years * 12
        balance = deposit.start_balance
        for _ in range(months):
            interest_month = balance * (interest_rate / 12)
            balance += interest_month
        total_amount = round(balance, 2)
        return total_amount

    def close_deposit(self, client_id):
        if client_id not in self.clients:
            return False
        deposit = self.clients[client_id].get('deposit')
        if deposit is None:
            return False
            # Получаем накопленную сумму
        interest_rate = 0.10
        months = deposit.years * 12
        balance = deposit.start_balance
        for _ in range(months):
            interest_month = balance * (interest_rate / 12)
            balance += interest_month
        # Удаляем депозит
        self.clients[client_id]['deposit'] = None
        total_amount = round(balance, 2)
        return total_amount


class CurrencyConverter:
    def __init__(self):
        self.rates = {
            'USD': 2.97,  # 1 USD ≈ 2.97 BYN
            'EUR': 3.39,  # 1 EUR ≈ 3.39 BYN
            'BYN': 1.0  # базовая валюта
            }

    def exchange_currency(self, currency, amount, target_currency=None):
        if currency not in self.rates:
            raise ValueError(f'Unsupported currency: {currency}')
        if target_currency is None:
            target_currency = 'BYN'
        if target_currency not in self.rates:
            raise ValueError(f'Unsupported target currency: {target_currency}')

        amount_in_byn = amount * self.rates[currency]

        if target_currency == 'BYN':
            return round(amount_in_byn, 2), 'BYN'

        target_amount = amount_in_byn / self.rates[target_currency]
        return round(target_amount, 2), target_currency


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


converter = CurrencyConverter()
