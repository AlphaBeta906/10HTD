"""
This module is for console related functions, such as clearing a line.

Written by: AlphaBeta906
Use: Utils

3/1/2022
"""

import sys
import os

def clear_line(i=1):
    for _ in range(i):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')