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
        self.clients[client_id] = {
            'name': name,
            'deposit': None
        }
        return True

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            return False
        deposit = Deposit(start_balance, years)
        self.clients[client_id]['deposit'] = deposit
        return True

    def calc_interest_rate(self, client_id):
        if client_id not in self.clients:
            return None
        deposit = self.clients[client_id].get('deposit')
        if deposit is None:
            return None
        annual_rate = 0.10
        months = deposit.years * 12
        balance = deposit.start_balance
        for _ in range(months):
            interest_month = balance * (annual_rate / 12)
            balance += interest_month
        return round(balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.clients:
            return False
        deposit = self.clients[client_id].get('deposit')
        if deposit:
            self.clients[client_id]['deposit'] = None
            return True
        return False
