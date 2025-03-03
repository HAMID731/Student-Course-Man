import unittest

from exceptions.exception import NullException, InvalidNameException, InvalidNameLengthException, \
    InvalidEmailPatternException, InvalidPasswordLengthException
from src.teacher import Teacher


class MyTeacherTestCase(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher("Firstname lastName", "email@gmail.com", "passw")

    def test_that_two_teachers_can_register_with_valid_details(self):
        self.teacher.register_teacher("Dr Favour", "FavourIgwe12@gmail.com", "password")
        self.assertEqual(1, self.teacher.number_of_teachers())
        self.teacher.register_teacher("Dr Hamid", "HamidAbari@gmail.com", "password1")
        self.assertEqual(2, self.teacher.number_of_teachers())

    def test_that_a_teacher_cannot_register_with_empty_name_field(self):
        with self.assertRaises(NullException):
            self.teacher.register_teacher("", "FavourIgwe@gmail.com", "password")

    def test_that_a_teacher_cannot_register_with_special_characters_present_in_name(self):
        with self.assertRaises(InvalidNameException):
            self.teacher.register_teacher("Dr$$$ Favour", "FavourIgwe@gmail.com", "password")

    def test_that_a_teacher_cannot_register_with_first_name_or_last_name_only_name_field(self):
        with self.assertRaises(InvalidNameLengthException):
            self.teacher.register_teacher("Dr", "FavourIgwe@gmail.com", "password")

    def test_that_a_teacher_cannot_register_with_empty_email_field(self):
        with self.assertRaises(NullException):
            self.teacher.register_teacher("Dr Favour", "", "password")

    def test_that_a_teacher_cannot_register_with_empty_password_field(self):
        with self.assertRaises(NullException and InvalidPasswordLengthException):
            self.teacher.register_teacher("Dr Favour", "FavourIgwe@gmail.com", "")

    def test_that_a_teacher_cannot_register_with_invalid_email_pattern(self):
        with self.assertRaises(InvalidEmailPatternException):
            self.teacher.register_teacher("Dr Favour", "@FavourIgwe@gmail.com", "password")

    def test_that_a_teacher_cannot_register_with_incomplete_password_length(self):
        with self.assertRaises(InvalidPasswordLengthException):
            self.teacher.register_teacher("Dr Favour", "FavourIgwe@gmail.com", "pass")

    def test_that_teacher_login_with_correct_details(self):
        self.teacher.register_teacher("Dr Favour", "FavourIgwe@gmail.com", "password")
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)

    def test_that_a_teacher_can_create_course(self):
        self.teacher.register_teacher("Dr Favour", "FavourIgwe@gmail.com", "password")
        self.assertFalse(self.teacher.login_status())
        login = self.teacher.login("FavourIgwe@gmail.com", "password")
        self.assertTrue(login)
        self.teacher.create_course("201", "English")
        self.assertEqual(1, self.teacher.number_of_courses_created())
        self.teacher.create_course("202", "Maths")
        self.assertEqual(2, self.teacher.number_of_courses_created())

