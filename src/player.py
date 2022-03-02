"""
This module is for containg the Player class.

Written by: AlphaBeta906
Use: Class

3/2/2022
"""

from game import Game

class Player:
    def __init__(self, cards: list) -> None:
        self.cards = cards

    def to_json(self):
        return {
            'cards': self.cards
        }

    def get_cards(self, game: Game) -> list:
        cards = []

        for index in self.cards:
            cards.append(game.cards[index])

        return cards