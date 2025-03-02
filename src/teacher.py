class Teacher:

    def __init__(self, email, password, name):
        self.__email = email
        self.__password = password
        self.__name = name

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