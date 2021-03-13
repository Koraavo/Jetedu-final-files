"""This program prints a to-do-list with SQL ALCHEMY"""

# Importing necessary modules
from datetime import timedelta, datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import sys

Base = declarative_base()


class Table(Base):
    """This class creates the table-'task'"""
    """Always query by class name and not table name"""
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return f"{self.task}"


class ToDOList:
    """This is the main function of the todolist"""

    def __init__(self):
        """Initialising the engine and the session. Base.metadata-creates the database"""
        engine = create_engine('sqlite:///todo.db?check_same_thread=False')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        Base.metadata.create_all(engine)

    def add_task(self):
        """Adding a task"""
        entry = input("Enter task\n").capitalize()
        new_row = Table(task=entry, deadline=datetime.strptime(input("Enter deadline\n"), '%Y-%m-%d'))
        self.session.add(new_row)
        self.session.commit()
        print("The task has been added!")
        print()

    def print_todays_tasks(self):
        """Print the tasks, else nothing to do"""

        rows = self.session.query(Table).filter(Table.deadline == self.today).all()
        print(f"Today {self.day} {self.month}:")
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for i, row in enumerate(rows, 1):
                print(f"{i}. {row}")
        print()

    def tasks_this_week(self):
        """Creating a timedelta for the week and showing the tasks to complete this week"""
        for i in range(0, 7):
            time_delta = self.today + timedelta(days=i)
            # filtering the data by the date
            rows = self.session.query(Table).filter(Table.deadline == time_delta).all()
            # showing it as Sunday 23 Dec
            print(f"{time_delta.strftime('%A %d %b')}:")
            if len(rows) == 0:
                print("Nothing to do!")
            else:
                for j, row in enumerate(rows, 1):
                    print(f"{j}. {row}")
            print()

    def all_tasks(self):
        """View all the tasks at hand and not just for the week"""
        print("All tasks:")
        rows = self.session.query(Table).order_by(Table.deadline.asc()).all()
        time_line = self.session.query(Table.deadline).order_by(Table.deadline.asc()).all()
        str_time = [time[0].strftime('%-d %b') for time in time_line]
        if len(rows) == 0:
            print("Nothing to do!")
        else:
            for i, row in enumerate(rows, 0):
                print(f'{i + 1}. {row}. {str_time[i]}')
        print()

    def missed_tasks(self):
        rows = self.session.query(Table).filter(Table.deadline < self.today).order_by(Table.deadline.asc()).all()
        time_line = self.session.query(Table.deadline).filter(Table.deadline < self.today).order_by(
            Table.deadline.asc()).all()
        str_time = [time[0].strftime('%-d %b') for time in time_line]
        if len(rows) == 0:
            print("Nothing is missed!")
        else:
            for ind, each_row in enumerate(rows):
                print(f"{ind + 1} {each_row} {str_time[ind]}")
        print()

    def delete_task(self):
        self.all_tasks()
        print("Choose the number of the task you want to delete:")
        row_to_del = int(input())
        rows = self.session.query(Table).filter(Table.deadline).order_by(Table.deadline.asc()).all()
        specific_row = rows[row_to_del - 1]
        self.session.delete(specific_row)
        self.session.commit()
        print("The task has been deleted!")

    def main_menu(self):

        self.today = datetime.today().date()
        self.day = self.today.day
        self.month = self.today.strftime('%b')
        # self.today.weekday()
        """Main Menu"""
        tasks = """1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit"""

        while (user_input := input(tasks)) != '0':
            if user_input == '1':
                print()
                self.print_todays_tasks()
            elif user_input == '2':
                print()
                self.tasks_this_week()
            elif user_input == '3':
                print()
                self.all_tasks()
            elif user_input == '4':
                print()
                self.missed_tasks()
            elif user_input == '5':
                print()
                self.add_task()
            elif user_input == '6':
                print()
                self.delete_task()
        exit("Bye!")


ToDOList().main_menu()
