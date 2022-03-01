"""
This module is for color related functions, such as decimal to rgb.

Written by: AlphaBeta906
Use: Helpers and Functions

3/1/2022
"""

def decimal_to_rgb(decimal: tuple) -> tuple:
    return tuple(int(x*255) for x in decimal)

# No use for the one below, but it's here for reference.
def rgb_to_decimal(rgb: tuple) -> tuple:
    return tuple(x/255 for x in rgb)