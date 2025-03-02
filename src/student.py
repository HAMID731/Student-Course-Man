from src.teacher import Teacher


class Student(Teacher):

    def __init__(self, email, password, name, admin_password):
        super().__init__(email, password, name)
        self.__courses = []



