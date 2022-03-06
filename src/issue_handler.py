"""
This module is for handling issues.

Written by: AlphaBeta906
Use: Utils

3/2/2022
"""

from random import randint
import inquirer
from faker import Faker

from json_reader import JSONLoader
from ansi import get_color_escape, set_color
from console import clear_screen

class IssueHandler:
    def __init__(self, game, selected_nation) -> None:
        self.game = game
        self.issues = JSONLoader('data/issue.json').read()
        self.selected_nation = selected_nation

    def value(self, value):
        GRAY = get_color_escape(128, 128, 128)
        GREEN = get_color_escape(0, 255, 0)
        RED = get_color_escape(255, 0, 0)

        if value == 0:
            return set_color('⋕ 0', GRAY)
        elif value > 0:
            return set_color(f'⇡ {value}', GREEN)
        elif value < 0:
            return set_color(f'⇣ {value}', RED)

    def possessive(self, text):
        if text[-1] == 's': return "'"
        else: return "'s"

    def narcotize(self, text):
        faker = Faker()

        return text.replace('@nation_self', self.selected_nation.name + self.possessive(self.selected_nation.name)).replace('@nation', self.selected_nation.name).replace('@name', faker.name())
    
    def handle(self, issue=None):
        YELLOW = get_color_escape(255, 215, 0)
        RED = get_color_escape(255, 0, 0)
        GREEN = get_color_escape(0, 0, 255)
        BLUE = get_color_escape(0, 0, 255)
        BOLD = '\033[1m'
        RESET = '\033[m'

        if issue is None:
            issue = randint(0, len(self.issues) - 1)

        if len(list(self.issues.keys())) - 1 < issue:
            raise IndexError('Issue does not exist.')
        else:
            issue_name = list(self.issues.keys())[issue]

            print(self.narcotize(issue_name))
            print(set_color("Context: ", YELLOW + BOLD) + self.narcotize(self.issues[issue_name]["context"]) + "\n")

            questions = [
                inquirer.List('option',
                    message='What would you like to do?',
                    choices=list(self.issues[issue_name]["choices"].keys()) + ['Abstain']
                )
            ]

            for o in self.issues[issue_name]["choices"]:
                print(f"{set_color(o, YELLOW + BOLD)}: {self.narcotize(self.issues[issue_name]['choices'][o]['reason'])}")

            print()

            answers = inquirer.prompt(questions)

            clear_screen()

            if answers['option'] == 'Abstain':
                print(set_color('You have abstained from this issue.', GREEN))
                print(set_color("ATTACK: ", RED + BOLD) + self.value(0))
                print(set_color("DEFENSE: ", BLUE + BOLD) + self.value(0))
                return {}
            else:
                print(set_color("Aftermath: ", BOLD + RED) + self.narcotize(self.issues[issue_name]["choices"][answers["option"]]["after"]))

                print(set_color("ATTACK: ", RED + BOLD) + RESET + self.value(self.issues[issue_name]["choices"][answers["option"]]["attack"]))
                print(set_color("DEFENSE: ", BLUE + BOLD) + RESET + self.value(self.issues[issue_name]["choices"][answers["option"]]["defense"]))

                return {
                    'attack': self.issues[issue_name]["choices"][answers['option']]["attack"],
                    'defense': self.issues[issue_name]["choices"][answers['option']]["defense"]
                }
