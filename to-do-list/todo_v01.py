from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import sys


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return f"{self.id}. {self.task}"


def add_task():
    print("Enter task")
    entry = input()
    new_row = Table(task=entry, deadline=datetime.today())
    session.add(new_row)
    session.commit()
    print("The task has been added!")


def print_todays_tasks():
    rows = session.query(Table).all()
    if len(rows) == 0:
        print("Today:")
        print("Nothing to do!")
    else:
        for row in rows:
            print(row)

Base.metadata.create_all(engine)

def main_menu():
    tasks = """1) Today's tasks
    2) Add task
    0) Exit 
    """

    while (user_input := input(tasks)) != '0':
        if user_input == '1':
            print_todays_tasks()

        elif user_input == '2':
            add_task()
    print("Bye!")

main_menu()