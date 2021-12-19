from calculations import get_uah_information, get_usd_information, exchange_uah, exchange_usd
from calculations import balance
from current_rate import usd_rate, uah_rate

while True:
    command: str = input('enter command:\n')
    split_command: list = command.upper().split(' ')

    if command.upper() == 'STOP':
        break

    if split_command[0] + ' ' + split_command[1] == 'COURSE UAH':
        print(get_uah_information())
    elif split_command[0] + ' ' + split_command[1] == 'COURSE USD':
        print(get_usd_information())
    elif all([split_command[0] == 'COURSE', split_command[1] not in ['UAH', 'USD']]):
        print(f'INVALID CURRENCY {split_command[1]}')

    if split_command[0] + ' ' + split_command[1] == 'EXCHANGE UAH':  # продаем доллар
        if balance.usd_balance >= int(split_command[2]) / usd_rate:
            print(exchange_uah(int(split_command[2])))
        else:
            print(f'UNAVAILABLE, REQUIRED BALANCE USD {balance.usd_balance},'
                  f' AVAILABLE {int(split_command[2]) / usd_rate}')
            break
    elif split_command[0] + ' ' + split_command[1] == 'EXCHANGE USD':  # покупаем доллар
        if balance.uah_balance >= int(split_command[2]) * uah_rate:
            print(exchange_usd(int(split_command[2])))
        else:
            print(f'UNAVAILABLE, REQUIRED BALANCE USD {balance.uah_balance},'
                  f' AVAILABLE {int(split_command[2]) * uah_rate}')
            break

