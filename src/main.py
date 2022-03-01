"""
This module is for running the main file.

Written by: AlphaBeta906
Use: Helpers and Functions

3/1/2022
"""

from pyfiglet import Figlet

from gradient import gradient
from color import rgb_to_decimal

RESET = '\033[0m'

def title():
    f = Figlet(font='slant')
    print(gradient(
        f.renderText('10 Hours \'Til Doom'), 
        rgb_to_decimal((255, 0, 0)), 
        rgb_to_decimal((255, 255, 0))
    ) + RESET)

if __name__ == "__main__":
    title()