# Write your code here
import random
import string

print("H A N G M A N")


def game_start():
    word_list = ['python', 'java', 'kotlin', 'javascript']

    # choice made by the computer
    com_choice = random.choice(word_list)

    # secret word currently = -----
    sec_word = list('-' * len(com_choice))

    # no of chances counter
    chances = 0

    # letters not in secret_word
    letters = []

    while chances < 8:
        print()
        # show the secret_word as joint and not a list
        print(''.join(sec_word))

        user_input = input("Input a letter: ")
        # checking all possible issues in the if elif clause
        # sequence: length, lower, in com_choice,
        # already entered but not in com_choice, in secret_word

        if len(user_input) != 1:
            print("You should input a single letter")
        elif not user_input.islower():
            print("It is not an ASCII lowercase letter")

        elif user_input in letters:
            print("You already typed this letter")

        # if letter not found
        elif user_input not in com_choice:
            print("No such letter in the word")
            letters.append(user_input)
            chances += 1

        # check if the input is in secret_word_list
        elif user_input in set(sec_word):
            print("You already typed this letter")

        else:
            # j = index, k = values
            for j, k in enumerate(com_choice):
                # letter found, replace with index values
                if user_input == k:
                    sec_word[j] = user_input
                else:
                    pass

            # if word figured stop loop
            if ''.join(sec_word) == com_choice:
                print("You guessed the word!\nYou survived!\n")
                break

    # end of loop
    if chances == 8:
        print("You are hanged!")


game = True
while game:
    play = input('Type "play" to play the game, "exit" to quit: ')
    if play == 'play':
        game_start()
    elif play == 'exit':
        game = False
    else:
        print("Wrong Input")
