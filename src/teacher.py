import string

import re

from exceptions.exception import NullException, InvalidPasswordLengthException, InvalidEmailPatternException, \
    InvalidNameLengthException, InvalidNameException, InvalidDetailsException, VerificationFailedException
from src.course import Course


class Teacher:

    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.__name = name
        self.students = []
        self.courses = []
        self.teachers = []
        self.__logged_in = False


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    TEACHER_DETAILS = 'user_details.txt'

    # @staticmethod
    # def hash_password(password):
    #     return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    @staticmethod
    def validate_email(email):
        if not email or not email.strip():
            raise NullException("Fields cannot be empty.")
        email_pattern = r'[A-Z][a-z][0-9][-._]+@[a-z][A-Z][0-9][-._]+\.[a-z][0-9][-._]+'

        if re.match(email_pattern, email):
            raise InvalidEmailPatternException("Invalid email address.")

    @staticmethod
    def validate_name(name):
        if not name:
            raise NullException("Fields cannot be empty.")

        names = name.split(' ')

        if len(names) < 2:
            raise InvalidNameLengthException("First name and last name is required.")

        for every_char in names:
            if every_char not in string.ascii_letters:
                raise InvalidNameException("Name must contain only alphabetic character.")

    @staticmethod
    def validate_password(password):
        if len(password) < 5:
            raise InvalidPasswordLengthException("Password must be at least 5 characters.")

        # return bcrypt.checkpw(password.encode('utf-8'), bcrypt.gensalt())


    def register_teacher(self, name: str, email: str, password:str):
        self.validate_email(email)
        self.validate_name(name)
        self.validate_password(password)
        details = name, email, password
        self.teachers.append(details)


    def create_course(self, course_code: str, course_title: str):
        if self.__logged_in == False:
            raise VerificationFailedException("You are not logged in.")
        course = Course(course_code, course_title)
        self.courses.append(course)
        self.__logged_in = True

    def login(self, name: str, password: str):
        for details in self.teachers:
            if details.name == name and details.password == password:
                return True

        raise InvalidDetailsException("Invalid details.")










