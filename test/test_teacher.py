import unittest

from src.teacher import Teacher


class MyTeacherTestCase(unittest.TestCase):
    def test_that_teacher_can_register_with_valid_details(self):
        teacher = Teacher("Firstname lastName", "email@gmail.com", "pass")
        teacher.register_teacher("Dr Favour", "FavourIgwe@gmail.com", "password")
        self.assertEqual(1, teacher.number_of_teachers())
        teacher.register_teacher("Dr Hamid", "HamidAbari@gmail.com", "password1")
        self.assertEqual(2, teacher.number_of_teachers())
