
# Write your code here
import banking_database
import random
import sys


def account_create(conn, card_numbers, pin_numbers):
    """Creates an account and prints your card and pin number"""
    card_list(card_numbers, pin_numbers)
    print("\nYour card has been created")
    print("Your card number:")
    print(card_numbers[-1])
    print("Your card PIN:")
    print(pin_numbers[-1])
    print()
    """Insert the data into sql"""
    banking_database.insert_into_tables(conn, card_numbers, pin_numbers)


def login(conn, card_numbers, pin_numbers):
    """logging requires card number and card pin"""
    # for debugging
    print()
    card_log = input("Enter your card number:\n")
    pin_log = input("Enter your PIN:\n")
    if card_log in card_numbers and pin_log == pin_numbers[card_numbers.index(card_log)]:
        print("\nYou have successfully logged in!\n")
        after_login(conn, card_log, card_numbers, pin_numbers)
    else:
        print("Wrong card number or PIN!")
        menu(conn, card_numbers, pin_numbers)


def after_login(conn, card_log, card_numbers, pin_numbers):
    game = True
    while game:
        # after login options
        choices = input("1. Balance\n"
                        "2. Add Income\n"
                        "3. Do transfer\n"
                        "4. Close Account\n"
                        "5. Log out\n"
                        "0. Exit\n")
        if choices == '1':
            print()
            print(f"Balance: {banking_database.show_balance(conn, card_log)[0]}")
            print()
        elif choices == '2':
            income = int(input("\nEnter income:\n"))
            banking_database.add_balance(conn, income, card_log)
            print("Income was added!\n")
        elif choices == '3':
            print()
            print("Transfer")
            account_to_transfer = input("Enter card number:\n")
            transfer(conn, card_log, account_to_transfer)
        elif choices == '4':
            banking_database.close_account(conn, card_log)
            pin_numbers.pop(card_numbers.index(card_log))
            card_numbers.remove(card_log)
            print("The account has been closed!\n")
            menu(conn, card_numbers, pin_numbers)
        elif choices == '5':
            print("You have successfully logged out!")
            game = False
        elif choices == '0':
            print('Bye!')
            sys.exit()


def transfer(conn, card_log, account_to_transfer):
    """Steps
    1. Ask user to input card number
    2. check how many numbers match with the given account number
        if match < 2:
            print(display Probably you made a mistake in the card number. Please try again!)
        go back to login after menu
        if match >= 2:
            print("Such a card does not exist.")
        else:
            transfer_amount to be input
            "Enter how much money you want to transfer:"
            if transfer_amount > balance:
                print(Not enough money!)
            else:
                print("Success")
        """
    if card_mistaken(conn, account_to_transfer) == 0:
        transfer_amount = int(input("Enter how much money you want to transfer:\n"))
        if transfer_amount > banking_database.show_balance(conn, card_log)[0]:
            print("Not enough money!\n")

        else:
            banking_database.add_balance(conn, transfer_amount, account_to_transfer)
            banking_database.sub_balance(conn, transfer_amount, card_log)
            print("Success!\n")

    elif (card_mistaken(conn, account_to_transfer) == 1) or (account_to_transfer[-1] != luhn_check(account_to_transfer)):
        print("\nProbably you made a mistake in the card number. Please try again!")

    elif card_mistaken(conn, account_to_transfer) >= 2 and not account_to_transfer.startswith('4'):
        print("Such a card does not exist.")


def card_mistaken(conn, account_to_transfer):
    counter_list = []
    cards_in_batabase = banking_database.get_all_card_numbers(conn)
    card_entered = list(account_to_transfer)
    for cards in cards_in_batabase:
        counter = 0
        count = list(*cards)
        for c, value in enumerate(count):
            if count[c] != card_entered[c]:
                counter += 1
        counter_list.append(counter)
    return min(counter_list)


# generate pin
def create_pin():
    """generates a 4-digit-pin for your card"""
    pin_number = '{:04d}'.format(random.randrange(0000, 9999))
    return pin_number


# generate a card
def create_card():
    """creates a 15-digit-card starting with 400000.
    The last digit is created using luhn's algorithm in the luhn_check function"""
    last_9 = random.randint(100000000, 999999999)
    card_number = '400000' + str(last_9)
    return card_number


def luhn_check(card_number):
    """creates the card with a checksum number"""
    # digit_15_card = create_card()

    # card tests
    # card = '400000844943340'
    # card = '400000775074255'

    # if index == even, multiply by 2 else num
    numbers = [str(int(num) * 2)
               if index % 2 == 0
               else str(int(num))
               for index, num in enumerate(card_number)]

    # if number is two digit, subtract by 9 else num
    new_number = [int(each_number) - 9
                  if len(each_number) == 2
                  else int(each_number)
                  for each_number in numbers]

    # get the last digit and subtract by 10 to get the checksum
    if sum(new_number) % 10 == 0:
        return '0'
    else:
        luhn_number = (10 - (sum(new_number) % 10))
        return str(luhn_number)


def digit_16_card():
    """creates the final 16_digit_card"""
    card_number = create_card()
    last_number = luhn_check(card_number)
    return card_number + last_number


# dictionary update every time a card is created and added to cards
def card_list(card_numbers, pin_numbers):
    """adds the created card to a dictionary of cards with card number and pin"""
    luhns_card = digit_16_card()
    pin = create_pin()
    card_numbers.append(luhns_card)
    pin_numbers.append(pin)
    return (*card_numbers, *pin_numbers)


def menu(conn, card_numbers, pin_numbers):
    """Main menu with options to create an account, log into an account and view balance"""
    # while I am on the site
    site_in = True

    # instantiate a dict, that will have all the cards with its pin number, every time a customer creates an account
    while site_in:
        create = input("1. Create an account\n"
                       "2. Log into account\n"
                       "0. Exit\n")
        if create == '1':
            account_create(conn, card_numbers, pin_numbers)
        elif create == '2':
            login(conn, card_numbers, pin_numbers)
        elif create == '0':
            # print(card_numbers)
            # print(pin_numbers)
            # try:
            #     print(banking_database.get_all_info_cards(conn))
            # except:
            #     pass
            print()
            print('Bye!')
            sys.exit()


def main():
    conn = banking_database.connect()
    banking_database.drop_table(conn)
    banking_database.create_table(conn)
    # saving of card_numbers and pin_numbers in a list, dictionary was not very helpful somehow
    card_numbers = []
    pin_numbers = []
    menu(conn, card_numbers, pin_numbers)
    conn.close()


main()
