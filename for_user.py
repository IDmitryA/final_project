"""
This module is for users.
It calls an infinite loop which takes commands from user and processes them with appropriate functions
from 'calculations.py'.
The loop can be stopped by calling command 'STOP' or in case of lack of any currency to complete exchange
operation.
"""

from calculations import processing

if __name__ == '__main__':
    processing()
