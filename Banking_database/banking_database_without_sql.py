import sqlite3
# Write your code here
import random
import sys


def account_create(card_numbers, pin_numbers):
    """Creates an account and prints your card and pin number"""

    card_list(card_numbers, pin_numbers)

    print("Your card has been created")
    print("Your card number:")
    print(card_numbers[-1])

    print("Your card PIN:")
    print(pin_numbers[-1])


def login(card_numbers, pin_numbers):
    """logging requires card number and card pin"""
    # for debugging
    print(dict(zip(card_numbers, pin_numbers)))
    card_log = input("Enter your card number:")
    pin_log = input("Enter your PIN:")
    if card_log in card_numbers and pin_log == pin_numbers[card_numbers.index(card_log)]:
        print("You have successfully logged in!")
        after_login()
    else:
        print("Wrong card number or PIN!")
        menu(card_numbers, pin_numbers)


def after_login():
    game = True
    while game:
        # after login options
        choices = input("1. Balance\n"
                        "2. Log out\n"
                        "0. Exit\n")
        if choices == '1':
            print(balance())
        elif choices == '2':
            print("You have successfully logged out!")
            game = False
        elif choices == '0':
            print('Bye!')
            sys.exit()


# generate a card
def create_card():
    """creates a 15-digit-card starting with 400000.
    The last digit is created using luhn's algorithm in the luhn_check function"""
    last_9 = random.randint(100000000, 999999999)
    card_number = '400000' + str(last_9)
    # n = 10
    # num = range(0, 10)
    # lst = random.sample(num, n)
    # card_number = '400000' + ''.join(str(num) for num in lst)
    return card_number


# generate pin
def create_pin():
    """generates a 4-digit-pin for your card"""
    # n = 4
    # num = range(0, 10)
    # pin_list = random.sample(num, n)
    # pin_number =''.join(str(num) for num in pin_list)
    pin_number = '{:04d}'.format(random.randrange(0000, 9999))
    return pin_number


# dictionary update every time a card is created and added to cards
def card_list(card_numbers, pin_numbers):
    """adds the created card to a dictionary of cards with card number and pin"""
    luhns_card = luhn_check()
    pin = create_pin()
    card_numbers.append(luhns_card)
    pin_numbers.append(pin)
    return (*card_numbers, *pin_numbers)


def luhn_check():
    """creates the card with a checksum number"""
    digit_15_card = create_card()

    # card tests
    # card = '400000844943340'
    # card = '400000775074255'

    # if index == even, multiply by 2 else num
    numbers = [str(int(num) * 2)
               if index % 2 == 0
               else str(int(num))
               for index, num in enumerate(digit_15_card)]

    # if number is two digit, subtract by 9 else num
    new_number = [int(each_number) - 9
                  if len(each_number) == 2
                  else int(each_number)
                  for each_number in numbers]

    # get the last digit and subtract by 10 to get the checksum
    if sum(new_number) % 10 == 0:
        return digit_15_card + '0'
    else:
        luhn_number = (10 - (sum(new_number) % 10))
        return digit_15_card + str(luhn_number)


def balance():
    """shows the balance in your account"""
    return '0'


def menu(card_numbers, pin_numbers):
    """Main menu with options to create an account, log into an account and view balance"""
    # while I am on the site
    site_in = True

    # instantiate a dict, that will have all the cards with its pin number, every time a customer creates an account
    while site_in:
        create = input("1. Create an account\n"
                       "2. Log into account\n"
                       "0. Exit\n")
        if create == '1':
            account_create(card_numbers, pin_numbers)
        elif create == '2':
            login(card_numbers, pin_numbers)
        elif create == '0':
            print(card_numbers)
            print(pin_numbers)
            print('Bye!')
            site_in = False


def main():
    # saving of card_numbers and pin_numbers in a list, dictionary was not very helpful somehow
    card_numbers = []
    pin_numbers = []
    menu(card_numbers, pin_numbers)


main()