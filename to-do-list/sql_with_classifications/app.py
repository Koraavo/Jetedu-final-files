from sqlalchemy.orm import sessionmaker
from model import Task


class App:
    EXIT = 0
    ACTIVE = 1
    TODAY_TASKS = 2
    ADD_TASK = 3

    def __init__(self, engine):
        self.session = sessionmaker(bind=engine)()
        self.status = self.ACTIVE

    def run(self):
        while self.status != self.EXIT:
            self.display()
            self.choose_menu()

    @staticmethod
    def display():
        print("1) Today's tasks")
        print("2) Add task")
        print("0) Exit")

    def choose_menu(self):
        choice = input()
        print()

        if choice == '0':
            self.status = self.EXIT
        elif choice == '1':
            self.today_tasks()
        elif choice == '2':
            self.add_task()
        else:
            print("Invalid input. Try again.")

        print()

    def today_tasks(self):
        print("Today:")
        tasks = self.session.query(Task).all()

        if len(tasks) == 0:
            print("Nothing to do!")
        else:
            print(*[f"{pos}. {task}" for pos, task in enumerate(tasks, start=1)], sep="\n")

    def add_task(self):
        print("Enter task")
        task = Task(task=input())

        self.session.add(task)
        self.session.commit()

        print("The task has been added!")