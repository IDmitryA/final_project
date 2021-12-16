from cash_balance import balance
from current_rate import usd_rate, uah_rate


def get_uah_information():
    return f'RATE {uah_rate}, AVAILABLE {balance.uah_balance}'


def get_usd_information():
    return f'RATE {usd_rate}, AVAILABLE {balance.usd_balance}'


def exchange_uah(uah_sum):
    print(balance.uah_balance)
    print(balance.usd_balance)
    usd_sum = round(uah_sum / usd_rate, 4)
    rate = usd_sum / uah_sum
    balance.change(balance.uah_balance + uah_sum, round(balance.usd_balance - usd_sum, 2))
    print(balance.uah_balance)
    print(balance.usd_balance)
    return f'USD {usd_sum}, RATE {rate}'

"""
def exchange_usd(usd_sum, balance.u):
    uah_sum = round(usd_sum / uah_rate, 4)
    rate = uah_sum / usd_sum
    uah_balance -= uah_sum
    usd_balance += usd_sum
    print(f'UAH {uah_sum}, RATE {rate}')
    return uah_balance, usd_balance

"""


