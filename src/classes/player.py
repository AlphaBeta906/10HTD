"""
This module is for containing the Player class.

Written by: AlphaBeta906
Use: Class

3/2/2022
"""

from pyfiglet import Figlet

from services.color import rgb_to_decimal
from .game import Game
from services.ansi import get_color_escape, set_color
from services.gradient import gradient

class Player:
    def __init__(self, cards: list, coins: int) -> None:
        self.cards = cards
        self.coins = coins

    def to_json(self):
        return {
            'cards': self.cards,
            'coins': self.coins
        }

    def get_cards(self, game: Game) -> list:
        cards = []

        for index in self.cards:
            cards.append(game.cards[index])

        return cards

    def info(self):
        f = Figlet(font='slant')
        print(gradient(
            f.renderText('Player'), 
            rgb_to_decimal((255, 215, 0)),
            rgb_to_decimal((0, 0, 255))
        ))
        print(set_color('Coins: ' + str(self.coins), get_color_escape(0, 0, 255)))