"""
This module is for containg the Player class.

Written by: AlphaBeta906
Use: Class

3/2/2022
"""

from pyfiglet import Figlet

from game import Game
from ansi import get_color_escape, set_color

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
        print(set_color(f.renderText('Player'), get_color_escape(255, 215, 0)))
        print(set_color('Coins: ' + str(self.coins), get_color_escape(0, 0, 255)))