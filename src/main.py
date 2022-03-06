"""
This module is for running the main file.

Written by: AlphaBeta906
Use: Main

3/1/2022
"""

from pyfiglet import Figlet
import inquirer
from random import randint

from gradient import gradient
from color import rgb_to_decimal
from ansi import set_color, get_color_escape
from console import clear_line, clear_screen
from issue_handler import IssueHandler
from json_reader import JSONLoader
from game import Game
from nation import Nation
from player import Player
from er import exponential_randomness

YELLOW = get_color_escape(255, 255, 0)
RED = get_color_escape(255, 0, 0)
MAGENTA = get_color_escape(255, 0, 255)
BOLD = '\033[1m'

def json_to_class(json):
    return Game(
        [Nation(
            card['name'], 
            card['description'], 
            card['hp'],
            card['atk']
        ) for card in json['cards']],
        Player(
            json['player']['cards'],
            json['player']['coins']
        )
    )

def play_game(game):
    player = game.player
    data = JSONLoader('data/data.json')

    while True:
        questions = [
            inquirer.List('action',
                message='What would you like to do?',
                choices=['View cards', 'View player', 'Upgrade cards', 'Exit']
            )
        ]

        answers = inquirer.prompt(questions)

        clear_screen()

        match answers['action']:
            case 'View cards':
                cards = player.get_cards(game)
                card_names = [card.name for card in cards]

                questions = [
                    inquirer.List('card',
                        message='Which card would you like to view?',
                        choices=card_names
                    )
                ]

                answers = inquirer.prompt(questions)

                clear_screen()
                card = cards[card_names.index(answers['card'])]
                card.info()
            case 'View player':
                player.info()
            case 'Upgrade cards':
                cards = player.get_cards(game)
                card_names = [card.name for card in cards]

                if randint(1, 5) == 1:
                    questions = [
                        inquirer.List('card',
                            message='Which card would you like to view?',
                            choices=card_names
                        )
                    ]

                    answers = inquirer.prompt(questions)
                    card = cards[card_names.index(answers['card'])]

                    issue_handler = IssueHandler(game, card)

                    clear_screen()
                    issue_data = issue_handler.handle()

                    card.atk = issue_data['attack']
                    card.hp = issue_data['defense']

                    game.cards[card_names.index(answers['card'])] = card
                else:
                    print(set_color('No issues found.', YELLOW))
            case 'Exit':
                break

        data.write(game.to_json())

        print()

def create_game():
    clear_screen()
    cards = []

    questions = [
        inquirer.Text('card1',
            message="What is the first nation's name?",
        ),
        inquirer.Text('card2',
            message="What is the second nation's name?",
        ),
        inquirer.Text('card3',
            message="What is the third nation's name?",
        ),
        inquirer.Text('card4',
            message="What is the fourth nation's name?",
        ),
        inquirer.Text('card5',
            message="What is the fifth nation's name?",
        ),
        inquirer.Text('card6',
            message="What is the sixth nation's name?",
        ),
    ]

    answers = inquirer.prompt(questions)
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

    for i in range(1, 7):
        cards.append(Nation(answers['card' + str(i)], "This is the player's " + ordinal(i) + " nation.", randint(1, 15), randint(1, 15), exponential_randomness(5)))

    player = Player([
        0,
        1,
        2,
        3,
        4,
        5
    ])

    game = Game(cards, player)

    return game

def play():
    clear_screen()
    data = JSONLoader('data/data.json')

    if data.read() == {}:
        print(RED + BOLD + 'Error: No data found.')

        questions = [
            inquirer.List('action',
                message='What would you like to do?',
                choices=['Add a new game', 'Exit']
            )
        ]

        answers = inquirer.prompt(questions)

        if answers['action'] == 'Add a new game':
            game = create_game()
            data.write(game.to_json())
        else:
            return
    else:
        game = json_to_class(data.read())
        play_game(game)

def title():
    version = JSONLoader('data/version.json').read()
    clear_screen()
    f = Figlet(font='roman')

    print(gradient(
        f.renderText('10 Hours \'Til Doom'), 
        rgb_to_decimal((255, 255, 255)), 
        rgb_to_decimal((255, 0, 0))
    ))

    clear_line(2)

    print(gradient(
        f'Version v{version["version"]} - {version["nick"]}',
        rgb_to_decimal((255, 255, 255)),
        rgb_to_decimal((255, 0, 0))
    ) + '\n')

    questions = [
        inquirer.List('choice',
            message="What do you want to do?",
            choices=['Play', 'Credits', 'Changelog', 'Exit'],
        )
    ]
    
    while True:
        answers = inquirer.prompt(questions)
        
        match answers['choice']:
            case 'Play':
                play()
                break
            case 'Credits':
                clear_screen()
                print(set_color('Credits', YELLOW + BOLD))
                print(set_color('Creator - ', YELLOW + BOLD) + set_color('AlphaBeta906', YELLOW))
                print(set_color('Programmer - ', YELLOW + BOLD) + set_color('AlphaBeta906', YELLOW))
                print(set_color('Ideas - ', YELLOW + BOLD) + set_color('AlphaBeta906', YELLOW))
                print()
            case 'Exit':
                exit()
            case 'Changelog':
                clear_screen()
                print(set_color('Changelog', MAGENTA + BOLD))

                for i in range(len(version['changes'])):
                    print(set_color(f'{i + 1}. ', MAGENTA + BOLD) + version['changes'][i])

                print()
            case _:
                print(answers)

if __name__ == "__main__":
    title()