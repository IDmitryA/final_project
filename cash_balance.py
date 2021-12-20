"""
In this module class 'Balance' is created with method 'change' for updating current balance of currencies
and instance of this class - 'balance'.
"""


class Balance:
    def __init__(self, uah_balance=100000, usd_balance=10000):
        self.uah_balance = uah_balance
        self.usd_balance = usd_balance

    def change(self, current_uah_balance, current_usd_balance):
        self.uah_balance = current_uah_balance
        self.usd_balance = current_usd_balance


balance = Balance()
