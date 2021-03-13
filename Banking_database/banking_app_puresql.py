
# Write your code here
import banking_database
import random
import sys


def account_create(conn):
    """Creates an account and prints your card and pin number
        Also creates an sql database using the details"""

    card_number = digit_16_card()
    pin = create_pin()
    print("\nYour card has been created")
    print("Your card number:")
    print(card_number)
    print("Your card PIN:")
    print(pin)
    print()
    """Insert the data into sql"""
    banking_database.insert_into_tables(conn, card_number, pin)
    print(banking_database.get_all_info_cards(conn))


def login_sql(conn):
    """logging requires card number and card pin-SQL Version"""
    # for debugging
    print()
    card_log = input("Enter your card number:\n")
    pin_log = input("Enter your PIN:\n")
    if banking_database.login_confirmation(conn, card_log, pin_log) is None:
        print("Wrong card number or PIN!\n")
        menu(conn)
    else:
        if banking_database.login_confirmation(conn, card_log, pin_log):
            print("\nYou have successfully logged in!\n")
            after_login(conn, card_log)
        else:
            print("Wrong card number or PIN!\n")
            menu(conn)


def after_login(conn, card_log):
    """List and SQL for after login options"""
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
            try:
                income = int(input("\nEnter income:\n"))
                banking_database.add_balance(conn, income, card_log)
                print("Income was added!\n")
            except ValueError:
                print("The income needs to be an integer amount")
                pass

        elif choices == '3':
            print()
            print("Transfer")
            account_to_transfer = input("Enter card number:\n")
            """check if the cards are valid before moving to transfer"""
            if not account_to_transfer.startswith('4'):
                print("\nSuch a card does not exist.")
            elif account_to_transfer[-1] != luhn_check(account_to_transfer[:-1]):
                print("\nProbably you made a mistake in the card number. Please try again!")
            else:
                transfer(conn, card_log, account_to_transfer)

        elif choices == '4':
            banking_database.close_account(conn, card_log)
            print("The account has been closed!\n")
            menu(conn)
        elif choices == '5':
            print("You have successfully logged out!")
            game = False
        elif choices == '0':
            print('Bye!')
            sys.exit()


def transfer(conn, card_log, account_to_transfer):
    """Steps
    1. Ask user to input card number
    2. if the card number starting with 4?
       if the card number a valid card number, passing the luhn's check?
       else:
            transfer_amount to be input
            "Enter how much money you want to transfer:"
            if transfer_amount > balance:
                print(Not enough money!)
            else:
                print("Success")
        """
    transfer_amount = int(input("Enter how much money you want to transfer:\n"))
    if transfer_amount > banking_database.show_balance(conn, card_log)[0]:
        print("Not enough money!\n")

    else:
        banking_database.add_balance(conn, transfer_amount, account_to_transfer)
        banking_database.sub_balance(conn, transfer_amount, card_log)
        print("Success!\n")


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


def menu(conn):
    """Main menu with options to create an account, log into an account and exit"""
    # while I am on the site
    site_in = True

    # instantiate a dict, that will have all the cards with its pin number, every time a customer creates an account
    while site_in:
        create = input("1. Create an account\n"
                       "2. Log into account\n"
                       "0. Exit\n")
        if create == '1':
            account_create(conn)
        elif create == '2':
            # login(conn, card_numbers, pin_numbers)
            login_sql(conn)
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
    """The current version uses both lists and sql database.
       While most of the operations are done using SQL,
       I have kept the lists and have tried to follow the same sequences has sql"""
    conn = banking_database.connect()
    banking_database.drop_table(conn)
    banking_database.create_table(conn)
    menu(conn)
    conn.close()


main()
