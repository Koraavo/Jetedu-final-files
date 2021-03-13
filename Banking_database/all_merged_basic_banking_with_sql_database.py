# Write your code here
import sqlite3
import random
import sys


def account_create(conn, card_numbers, pin_numbers):
    """Creates an account and prints your card and pin number, also adds it to sqlite database"""
    card_list(card_numbers, pin_numbers)
    # print(card_numbers)
    # print(pin_numbers)
    print("Your card has been created")
    print("Your card number:")
    print(card_numbers[-1])

    print("Your card PIN:")
    print(pin_numbers[-1])

    # sql lite create table and insert data as soon as it is created
    insert_into_tables(conn, card_numbers, pin_numbers)


def login(conn, card_numbers, pin_numbers):
    """logging requires card number and card pin"""
    card_log = input("Enter your card number:")
    pin_log = input("Enter your PIN:")
    if card_log in card_numbers and pin_log == pin_numbers[card_numbers.index(card_log)]:
        print("You have successfully logged in!")
        after_login()
    else:
        print("Wrong card number or PIN!")
        menu(conn, card_numbers, pin_numbers)


def after_login():
    """Options to see the balance, logout and exit after logging in"""
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
    return card_number


# generate pin
def create_pin():
    """generates a 4-digit-pin for your card"""
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
            # try:
            #     print(select_all(conn, c))
            # except:
            #     pass
            print('Bye!')
            sys.exit()


#####SQL DATABASE STARTS FROM HERE#####


def create_table(conn):
    """create a table in the database after connecting"""
    table_name = """
    CREATE TABLE IF NOT EXISTS card (
                                     id integer primary key AUTOINCREMENT NOT NULL, 
                                     number TEXT UNIQUE, 
                                     pin TEXT, 
                                     balance integer DEFAULT 0);"""
    with conn:
        conn.execute(table_name)


def insert_into_tables(conn, card_numbers, pin_numbers):
    """create a table in the database after connecting"""
    sql_statement = "INSERT INTO card(number, pin) VALUES (?, ?);"
    # insert_table = "INSERT INTO card VALUES (:number, :pin)", {'number': all_cards[-1], 'pin': all_pins[-1]}
    with conn:
        conn.execute(sql_statement, (card_numbers[-1], pin_numbers[-1]))


def select_all(conn):
    with conn:
        conn.execute("SELECT * FROM card")
        return conn.fetchall()


def select_where(conn, card_number):
    with conn:
        conn.execute("SELECT * FROM card where card_number=:card_number", {'card_number': card_number})
        return conn.fetchall()


def drop_table(conn):
    with conn:
        conn.execute("DROP TABLE IF EXISTS card")


def main():
    # path to the database
    database = 'banking/card.s3db'
    # connection to the database
    conn = sqlite3.connect(database)
    # create a table
    create_table(conn)

    # saving of card_numbers and pin_numbers in a list, dictionary was not very helpful somehow
    card_numbers = []
    pin_numbers = []
    menu(conn, card_numbers, pin_numbers)

    # dropping table if exists
    drop_table(conn)

    # print(select_cards(conn, c))
    conn.close()


main()

