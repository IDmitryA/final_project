"""
This module is for users.
There is an infinite loop which takes commands from user and processes them with appropriate functions
from 'calculations.py'.
The loop can be stopped by calling command 'STOP' or in case of lack of any currency for complete exchange
operation.
"""

from calculations import get_uah_information, get_usd_information, exchange_uah, exchange_usd
from calculations import balance
from current_rate import usd_rate, uah_rate

while True:
    command: str = input('enter command:\n')
    split_command: list = command.upper().split(' ')  # using upper() for any types of user input: 'uAH', 'uAh',
    # 'UsD', 'usD', 'coURsE', 'ExCHangE', 'sTop', etc.

    if command.upper() == 'STOP':
        break

    if split_command[0] + ' ' + split_command[1] == 'COURSE UAH':
        print(get_uah_information())
    elif split_command[0] + ' ' + split_command[1] == 'COURSE USD':
        print(get_usd_information())
    elif all([split_command[0] == 'COURSE', split_command[1] not in ['UAH', 'USD']]):
        print(f'INVALID CURRENCY {split_command[1]}')

    if split_command[0] + ' ' + split_command[1] == 'EXCHANGE UAH':  # selling USD
        if balance.usd_balance >= int(split_command[2]) / usd_rate:  # enough USD for complete exchange
            print(exchange_uah(int(split_command[2])))
        else:                                                        # not enough USD for complete exchange
            print(f'UNAVAILABLE, REQUIRED BALANCE USD {balance.usd_balance},'
                  f' AVAILABLE {int(split_command[2]) / usd_rate}')
            break
    elif split_command[0] + ' ' + split_command[1] == 'EXCHANGE USD':  # buying USD
        if balance.uah_balance >= int(split_command[2]) * uah_rate:    # enough UAH for complete exchange
            print(exchange_usd(int(split_command[2])))
        else:                                                          # not enough UAH for complete exchange
            print(f'UNAVAILABLE, REQUIRED BALANCE USD {balance.uah_balance},'
                  f' AVAILABLE {int(split_command[2]) * uah_rate}')
            break

