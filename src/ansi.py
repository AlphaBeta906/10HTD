"""
This module is for ansi related functions, such as changing the color of text and turning hex
into ansi color codes.

Written by: AlphaBeta906
Use: Helpers and Functions

3/1/2022
"""

def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def get_color_escape_decimal(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, int(r*255), int(g*255), int(b*255))

def set_color(text, color_escape):
    return color_escape + text + '\033[m'