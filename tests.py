"""
This module contains tests that check if the commands are processed correctly even if typet with different case and
extra spaces typed accidentally.
"""
from unittest import TestCase, main
from calculations import exchange_uah, exchange_usd
from current_rate import usd_rate, uah_rate
from cash_balance import balance
import calculations


class TestExchange(TestCase):

    # testing 'COURSE UAH'. Command 'stop' using jast for brake infinite loop
    def test_get_uah_information(self):
        command_list = ['course uah', 'CoUrSe UaH', '   COURSE uah', '   course   UAH', '   COURSE    UAH   ', 'stop']

        # next generator is used to get elements from 'command_list' one by one
        def list_items():
            for item in command_list:
                yield item
        gen = list_items()
        my_iter = 0
        while my_iter < len(command_list):
            # place elements from 'command_list' to 'input' in main loop
            try:
                calculations.input = lambda _: next(gen)
                out: str = calculations.processing()
                self.assertTrue(out == f'RATE {usd_rate}, AVAILABLE {balance.usd_balance}' or out == 'end')
                my_iter += 1
            except StopIteration:
                break

    # testing 'COURSE USD'. Command 'stop' using jast for brake infinite loop
    def test_get_usd_information(self):
        command_list = ['course usd', 'CoUrSe UsD', '   COURSE usd', '   course   USD', '   COURSE    USD   ', 'stop']

        # next generator is used to get elements from 'command_list' one by one
        def list_items():
            for item in command_list:
                yield item
        gen = list_items()
        my_iter = 0
        while my_iter < len(command_list):
            # place elements from 'command_list' to 'input' in main loop
            try:
                calculations.input = lambda _: next(gen)
                out: str = calculations.processing()
                self.assertTrue(out == f'RATE {uah_rate}, AVAILABLE {balance.uah_balance}' or out == 'end')
                my_iter += 1
            except StopIteration:
                break

    # testing 'EXCHANGE UAH {uah_sum}'. Command 'stop' using jast for brake infinite loop
    def test_exchange_uah(self):
        command_list = ['exchange uah 100', '   exchange UaH 100   ', '   ExChAnGe     UaH     100   ', 'stop']

        # next generator is used to get elements from 'command_list' one by one
        def list_items():
            for item in command_list:
                yield item
        gen = list_items()
        my_iter = 0
        while my_iter < len(command_list):
            # place elements from 'command_list' to 'input' in main loop
            try:
                calculations.input = lambda _: next(gen)
                out: str = calculations.processing()
                self.assertTrue(out == exchange_uah(100) or out == 'end')
                my_iter += 1
            except StopIteration:
                break

    # testing 'EXCHANGE USD {usd_sum}'. Command 'stop' using jast for brake infinite loop
    def test_exchange_usd(self):
        command_list = ['exchange usd 100', '   exchange UsD 100   ', '   ExChAnGe     UsD     100   ', 'stop']

        # next generator is used to get elements from 'command_list' one by one
        def list_items():
            for item in command_list:
                yield item
        gen = list_items()
        my_iter = 0
        while my_iter < len(command_list):
            # place elements from 'command_list' to 'input' in main loop
            try:
                calculations.input = lambda _: next(gen)
                out: str = calculations.processing()
                self.assertTrue(out == exchange_usd(100) or out == 'end')
                my_iter += 1
            except StopIteration:
                break


if __name__ == '__main__':
    main()
