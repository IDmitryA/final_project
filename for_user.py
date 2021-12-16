from calculations import get_uah_information, get_usd_information, exchange_uah
from calculations import balance


while True:
    command: str = input('enter command:\n')
    split_command: list = command.upper().split(' ')

    if split_command[0] + ' ' + split_command[1] == 'COURSE UAH':
        print(get_uah_information())
    elif split_command[0] + ' ' + split_command[1] == 'COURSE USD':
        print(get_usd_information())
    elif all([split_command[0] == 'COURSE', split_command[1] not in ['UAH', 'USD']]):
        print(f'INVALID CURRENCY {split_command[1]}')

    elif split_command[0] + ' ' + split_command[1] == 'EXCHANGE UAH':
        print(exchange_uah(int(split_command[2])))

    elif split_command[0] + ' ' + split_command[1] == 'EXCHANGE USD':
        print(exchange_usd(int(split_command[2])))

