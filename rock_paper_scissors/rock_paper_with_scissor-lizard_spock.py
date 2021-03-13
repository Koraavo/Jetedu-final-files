"""
winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
"""


# Write your code here


import random


# returns a dictionary with the data on rating for names and scores
def read_from_file():
    names = []
    scores = []
    with open('rating.txt') as f:
        for elements in f:
            name, score = elements.split(' ')
            names.append(name)
            scores.append(int(score.strip()))
    game_played = dict(zip(names, scores))
    return game_played


# what happens with the choices?
def game_choices(data, com_input, user_input):
    if com_input == user_input:
        print(f'There is a draw {(com_input)}')
        return 'Draw'
    elif com_input in data.get(user_input):
        print(f'Sorry, but the computer chose {com_input}')
        return 'Lost'
    else:
        print(f'Well done. The computer chose {com_input} and failed')
        return 'Won'


# score depending on the name
def current_score():
    game_played = read_from_file()
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    initial_game_list = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water',
                         'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']
    print(*initial_game_list, sep=',')
    if name in game_played.keys():
        score = game_played.get(name)
    else:
        score = 0
    return score


def which_game():
    user_choice = input()
    if user_choice == '':
        wins1 = ['rock', 'paper', 'scissors']
        lose1 = ['scissors', 'rock', 'paper']
        data = dict(zip(lose1, wins1))
        return data
    else:
        # wins = ['scissors', 'rock', 'paper', 'lizard', 'spock',
        #         'scissors', 'lizard', 'paper', 'spock', 'rock']

        # lose = ['paper', 'lizard', 'rock', 'spock', 'scissors',
        #         'lizard', 'paper', 'spock', 'rock', 'scissors']

        # data = {}
        # for x, y in zip(wins, lose):
        #     data.setdefault(x, []).append(y)
        data = {
            'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
            'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
            'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
            'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
            'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
            'rock': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
            'fire': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            'scissors': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
            'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
            'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
            'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
            'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
            'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
            'paper': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
            'air': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']
        }
        return data


# game on!
def game():

    # instantiate score
    score = current_score()
    game_off = False
    data = which_game()
    wins = list(set(data))
    print("Okay, let's start")
    while not game_off:
        # user_choice
        user_choice = input()
        if user_choice == '!exit':
            print('Bye!')
            game_off = True
        elif user_choice == '!rating':
            print(f'Your rating: {score}')
        elif user_choice not in wins and user_choice != '':
            print('Invalid input')
        else:
            com_choice = random.choice(wins)
            choices = game_choices(data, com_choice, user_choice)
            if choices == 'Draw':
                score += 50
            elif choices == 'Lost':
                score += 0
            else:
                score += 100


game()
