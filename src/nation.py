"""
This module is for containing the Player class.

Written by: AlphaBeta906
Use: Classes

3/2/2022
"""

from card import Card
from ansi import get_color_escape, set_color

class Nation(Card):
    def __init__(self, name, description, hp, atk) -> None:
        super().__init__(name, description)
        self._hp = hp
        self._atk = atk

        if self._hp + self._atk < 8:
            self.rank = 1
        elif self._hp + self._atk < 16:
            self.rank = 2
        elif self._hp + self._atk < 24:
            self.rank = 3
        elif self._hp + self._atk < 32:
            self.rank = 4
        else:
            self.rank = 5

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'hp': self._hp,
            'atk': self._atk
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

        print(set_color('HP: ' + str(self._hp), get_color_escape(0, 0, 255)))
        print(set_color('ATK: ' + str(self._atk), get_color_escape(255, 0, 0)))
        print('Rank: ' + set_color("★" * self.rank, color))

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @hp.setter
    def hp(self, hp):
        self._hp += hp

        if self._hp + self._atk < 8:
            self.rank = 1
        elif self._hp + self._atk < 16:
            self.rank = 2
        elif self._hp + self._atk < 24:
            self.rank = 3
        elif self._hp + self._atk < 32:
            self.rank = 4
        else:
            self.rank = 5
    
    @atk.setter
    def atk(self, atk):
        self._atk += atk

        if self._hp + self._atk < 8:
            self.rank = 1
        elif self._hp + self._atk < 16:
            self.rank = 2
        elif self._hp + self._atk < 24:
            self.rank = 3
        elif self._hp + self._atk < 32:
            self.rank = 4
        else:
            self.rank = 5