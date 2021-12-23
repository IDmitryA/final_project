"""
This module contains the functions for processing user's commands, which are called from module 'for_user.py'.
"""

from cash_balance import balance
from current_rate import usd_rate, uah_rate


def get_uah_information() -> str:  # processing command 'COURSE USD'
    return f'RATE {uah_rate}, AVAILABLE {balance.uah_balance}'


def get_usd_information() -> str:  # processing command 'COURSE UAH'
    return f'RATE {usd_rate}, AVAILABLE {balance.usd_balance}'


def exchange_uah(uah_sum) -> str:  # processing command 'EXCHANGE UAH {uah_sum}'
    usd_sum: float = round(uah_sum / usd_rate, 4)
    rate: float = round(usd_sum / uah_sum, 6)
    balance.change(balance.uah_balance + uah_sum, round(balance.usd_balance - usd_sum, 2))
    return f'USD {usd_sum}, RATE {rate}'


def exchange_usd(usd_sum) -> str:  # processing command 'EXCHANGE USD {usd_sum}'
    uah_sum: float = round(usd_sum * uah_rate, 4)
    rate: float = round(uah_sum / usd_sum, 6)
    balance.change(round(balance.uah_balance - uah_sum, 2), balance.usd_balance + usd_sum)
    return f'UAH {uah_sum}, RATE {rate}'


def processing():
    while True:
        command: str = input('enter command:\n')
        # for cases when user accidentally types extra ' ' at the beginning or the end of a string and between the
        # words. upper() is used for any types of user's input: 'uAH', 'uAh', 'UsD', 'usD', 'coURsE', 'ExCHangE',
        # 'sTop', etc.
        list_command = command.upper().split(' ')
        work_command = []
        for i in list_command:
            if i != '':
                work_command.append(i)

        if work_command[0] == 'STOP':
            return 'end'

        try:
            if work_command[0] + ' ' + work_command[1] == 'COURSE UAH':
                print(get_uah_information())
            elif work_command[0] + ' ' + work_command[1] == 'COURSE USD':
                print(get_usd_information())
            elif all([work_command[0] == 'COURSE', work_command[1] not in ['UAH', 'USD']]):
                print(f'INVALID CURRENCY {work_command[1]}')

            elif work_command[0] + ' ' + work_command[1] == 'EXCHANGE UAH':  # selling USD
                if balance.usd_balance >= float(work_command[2]) / usd_rate:  # enough USD to complete exchange
                    if float(work_command[2]) > 0:
                        print(exchange_uah(float(work_command[2])))
                    else:
                        print('You might be wrong, repeat your command:\n')
                        continue
                else:                                                          # not enough USD to complete exchange
                    print(f'UNAVAILABLE, REQUIRED BALANCE USD {float(work_command[2]) / usd_rate},'
                          f' AVAILABLE {balance.usd_balance}')
                    break
            elif work_command[0] + ' ' + work_command[1] == 'EXCHANGE USD':  # buying USD
                if balance.uah_balance >= float(work_command[2]) * uah_rate:  # enough UAH to complete exchange
                    if float(work_command[2]) > 0:
                        print(exchange_usd(float(work_command[2])))
                    else:
                        print('You might be wrong, repeat your command:\n')
                        continue
                else:                                                          # not enough UAH to complete exchange
                    print(f'UNAVAILABLE, REQUIRED BALANCE USD {float(work_command[2]) * uah_rate},'
                          f' AVAILABLE {balance.uah_balance}')
                    break
            else:
                print('You might be wrong, repeat your command:\n')
                continue
        except IndexError:
            print('You might be wrong, repeat your command:\n')
            continue
        except ValueError:
            print('You might be wrong, repeat your command:\n')
            continue

