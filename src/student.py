from src.teacher import Teacher


class Student(Teacher):

    def __init__(self, email, password, name, admin_password):
        super().__init__(email, password, name)
        self.__admin_password = admin_password
        self.__courses = []

    @property
    def admin_password(self):
        return self.__admin_password

    @admin_password.setter
    def admin_password(self, password):
        self.__admin_password = password