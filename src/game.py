"""
This module is for containg the Game class.

Written by: AlphaBeta906
Use: Classes

3/2/2022
"""

class Game:
    def __init__(self, cards, player) -> None:
        self.cards = cards
        self.player = player

    def to_json(self):
        return {
            'cards': [card.to_json() for card in self.cards],
            'player': self.player.to_json()
        }