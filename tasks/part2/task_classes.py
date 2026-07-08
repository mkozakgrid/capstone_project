import datetime

class Teacher:
    def __init__(self, last_name: str, first_name: str): 
        self.last_name = last_name
        self.first_name = first_name
    def create_homework(self, task_text: str, days_to_complete: int):
        return Homework(task_text, datetime.timedelta(days=days_to_complete), datetime.datetime.now()) 

class Homework:
    def __init__(self, text: str, days_to_complete: int):
        self.task_text = text
        self.deadline = datetime.timedelta(days=days_to_complete)
        self.created = datetime.datetime.now()
    def is_active(self): 
        return datetime.datetime.now() < self.created + self.deadline

class Student:
    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name
    def do_homework(self, homework: Homework): 
        if homework.is_active():
            return homework
        else:
            print("You are late")
            return None

