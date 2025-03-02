import unittest

from exceptions.exception import NullException, InvalidNameException, InvalidNameLengthException
from src.teacher import Teacher


class MyTeacherTestCase(unittest.TestCase):

    def setUp(self):
        self.teacher = Teacher("Firstname lastName", "email@gmail.com", "pass")

    def test_that_two_teachers_can_register_with_valid_details(self):
        self.teacher.register_teacher("Dr Favour", "FavourIgwe@gmail.com", "password")
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
