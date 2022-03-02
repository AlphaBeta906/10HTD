"""
This module is for containg the Player class.

Written by: AlphaBeta906
Use: Classes

3/2/2022
"""

from card import Card
from ansi import get_color_escape, set_color

class Nation(Card):
    def __init__(self, name, description, hp, atk, rank) -> None:
        super().__init__(name, description)
        self.hp = hp
        self.atk = atk
        self.rank = rank

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'hp': self.hp,
            'atk': self.atk,
            'rank': self.rank
        }

    def info(self):
        color = ''
        ITALIC = '\033[3m'
        BOLD = '\033[1m'

        match self.rank:
            case 1: color = get_color_escape(128, 128, 128)
            case 2: color = get_color_escape(128, 0, 128)
            case 3: color = get_color_escape(255, 0, 0)
            case 4: color = get_color_escape(0, 255, 0)
            case 5: color = get_color_escape(255, 215, 0)

        print(set_color(BOLD + self.name, color))
        print(set_color(ITALIC + self.description, get_color_escape(128, 128, 128)) + '\n')

        print(set_color('HP: ' + str(self.hp), get_color_escape(0, 0, 255)))
        print(set_color('ATK: ' + str(self.atk), get_color_escape(255, 0, 0)))
        print('Rank: ' + set_color("★" * self.rank, color))
