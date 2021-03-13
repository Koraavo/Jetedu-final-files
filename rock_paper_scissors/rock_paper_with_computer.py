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
    elif com_input == data.get(user_input):
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
    if name in game_played.keys():
        score = game_played.get(name)
    else:
        score = 0

    return score


# game on!
def game():
    wins = ['rock', 'paper', 'scissors']
    lose = ['scissors', 'rock', 'paper']
    data = dict(zip(lose, wins))

    # instantiate score
    score = current_score()

    game_off = False
    while not game_off:

        # user_choice
        user_choice = input()

        if user_choice == '!exit':
            print('Bye!')
            game_off = True
        elif user_choice == '!rating':
            print(f'Your rating: {score}')
        elif user_choice not in wins:
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
