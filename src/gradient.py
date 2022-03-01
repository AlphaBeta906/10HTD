"""
This module is for console related functions, such as clearing a line.

Written by: AlphaBeta906
Use: Helpers and Functions

3/1/2022
"""

from colour import Color

from ansi import get_color_escape_decimal, set_color

def gradient(text, c1, c2):
    if '\n' in text: text_len = len(text.split('\n'))
    else: text_len = len(text)

    colors = list(Color(rgb=c1).range_to(Color(rgb=c2),text_len))

    if '\n' in text:
        text = text.split('\n')
        for i in range(len(text)):
            text[i] = set_color(text[i], get_color_escape_decimal(colors[i].red, colors[i].green, colors[i].blue))

        return '\n'.join(text)
    else:
        text = list(text)
        for i in range(len(text)):
            text[i] = set_color(text[i], get_color_escape_decimal(colors[i].red, colors[i].green, colors[i].blue))
        return ''.join(text)