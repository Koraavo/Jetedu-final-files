from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

# Write your code here
Base = declarative_base()


class Table(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    task = Column(String, default="Task")
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


class ToDoList:
    def __init__(self):
        self.engine = create_engine("sqlite:///todo.db?check_same_thread=False")
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def main_function(self):
        while True:
            option = int(input("1) Today's tasks\n2) Add task\n0) Exit\n"))

            if option == 0:
                exit("Bye!")
            elif option == 1:
                rows = self.session.query(Table).all()
                print("\nToday:")

                if len(rows) == 0:
                    print("Nothing to do!")
                else:
                    for i, j in enumerate(rows):
                        print(f"{i + 1}. {j}")
                    print()
            else:
                add_task = input("\nEnter task\n")
                new_row = Table(task=add_task)
                self.session.add(new_row)
                self.session.commit()
                print("The task has been added!\n")


if __name__ == '__main__':
    ToDoList().main_function()