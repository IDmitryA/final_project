"""
This module contains the functions for processing user's commands, which are called in module 'for_user.py'.
"""

from cash_balance import balance
from current_rate import usd_rate, uah_rate


def get_uah_information() -> str:  # processing command 'COURSE USD'
    return f'RATE {uah_rate}, AVAILABLE {balance.uah_balance}'


def get_usd_information() -> str:  # processing command 'COURSE UAH'
    return f'RATE {usd_rate}, AVAILABLE {balance.usd_balance}'


def exchange_uah(uah_sum) -> str:  # processing command 'EXCHANGE UAH {uah_sum}'
    usd_sum = round(uah_sum / usd_rate, 4)
    rate = round(usd_sum / uah_sum, 6)
    balance.change(balance.uah_balance + uah_sum, round(balance.usd_balance - usd_sum, 2))
    return f'USD {usd_sum}, RATE {rate}'


def exchange_usd(usd_sum) -> str:  # processing command 'EXCHANGE USD {usd_sum}'
    uah_sum = round(usd_sum * uah_rate, 4)
    rate = round(uah_sum / usd_sum, 6)
    balance.change(round(balance.uah_balance - uah_sum, 2), balance.usd_balance + usd_sum)
    return f'UAH {uah_sum}, RATE {rate}'



