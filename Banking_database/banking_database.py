import sqlite3

#####SQL DATABASE STARTS FROM HERE#####

DROP_TABLE = "DROP TABLE IF EXISTS card;"

CREATE_CARD_TABLE = """CREATE TABLE IF NOT EXISTS card (
                                     id integer primary key AUTOINCREMENT NOT NULL, 
                                     number TEXT UNIQUE, 
                                     pin TEXT, 
                                     balance integer DEFAULT 0);"""

INSERT_DEBIT_CARD = "INSERT INTO card(number, pin) VALUES (?, ?);"

GET_ALL_INFO_CARDS = "SELECT id, number, pin, balance FROM card;"

GET_ALL_CARD_NUMBERS = """
SELECT number FROM card;
"""

GET_CARDS_BALANCE_BY_CARD_NUMBER = "SELECT balance FROM card WHERE number = ?;"

LOGIN_CONFIRMATION = """
SELECT number, pin FROM card
WHERE number = ?
AND pin = ?;
"""

GET_PIN_BY_CARD_NUMBER = "SELECT pin FROM card WHERE number = ?;"

GET_CARD_IF_EXISTS = """
SELECT number FROM card
WHERE number = ?;
"""

GET_CARDS_BALANCE_NOT_0 = """
SELECT * FROM card
WHERE balance != 0
ORDER BY DESC;
"""

GET_BALANCE = """
SELECT balance from card
where number = ?;
"""

ADD_BALANCE = """
UPDATE card 
SET balance = balance+?
where number = ?;
"""

DEDUCT_BALANCE = """
UPDATE card 
SET balance = balance-?
where number = ?;
"""

CLOSE_ACCOUNT = """
DELETE FROM card
WHERE number = ?;
"""


def connect():
    # path to the database
    database = 'card.s3db'
    # database = 'banking/card.s3db'

    # connection to the database
    return sqlite3.connect(database)


def create_table(conn):
    """create a table in the database after connecting"""
    with conn:
        conn.execute(CREATE_CARD_TABLE)


def insert_into_tables(conn, card_numbers, pin_numbers):
    """create a table in the database after connecting"""
    # insert_table = "INSERT INTO card VALUES (:number, :pin)", {'number': all_cards[-1], 'pin': all_pins[-1]}
    with conn:
        conn.execute(INSERT_DEBIT_CARD, (card_numbers, pin_numbers))


def get_all_info_cards(conn):
    with conn:
        return conn.execute(GET_ALL_INFO_CARDS).fetchall()


def get_all_card_numbers(conn):
    with conn:
        return conn.execute(GET_ALL_CARD_NUMBERS).fetchall()


def login_confirmation(conn, card_numbers, pin_number):
    with conn:
        return conn.execute(LOGIN_CONFIRMATION, (card_numbers, pin_number)).fetchone()


def get_balance(conn, card_number):
    with conn:
        return conn.execute(GET_CARDS_BALANCE_BY_CARD_NUMBER, (card_number,)).fetchone()


def get_pin(conn, card_number):
    with conn:
        return conn.execute(GET_PIN_BY_CARD_NUMBER, (card_number,)).fetchone()


def get_card_if_exists(conn, card_number):
    with conn:
        return conn.execute(GET_CARD_IF_EXISTS, (card_number,)).fetchone()


def drop_table(conn):
    with conn:
        conn.execute(DROP_TABLE)


def get_cards_with_balance(conn):
    with conn:
        return conn.execute(GET_CARDS_BALANCE_NOT_0).fetchall()


def show_balance(conn, card_number):
    with conn:
        return conn.execute(GET_BALANCE, (card_number,)).fetchone()


def add_balance(conn, amount, card_number):
    with conn:
        return conn.execute(ADD_BALANCE, (amount, card_number)).fetchone()


def sub_balance(conn, amount, card_number):
    with conn:
        return conn.execute(DEDUCT_BALANCE, (amount, card_number)).fetchone()


def close_account(conn, card_number):
    with conn:
        return conn.execute(CLOSE_ACCOUNT, (card_number,)).fetchall()