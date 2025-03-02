import unittest

from exceptions.exception import InvalidCourseCodeException, InvalidCourseTitleException, \
    StudentAlreadyEnrolledException, NullException
from src.course import Course


class MyCourseTestCase(unittest.TestCase):

    def test_that_course_can_be_created(self):
        course = Course("201", "English")
        self.assertEqual(course.course_code, "201")
        self.assertEqual(course.title, "English")
        self.assertEqual(course.number_of_enrolled_students(), 0)

    def test_that_course_code_as_string_raises_invalid_course_code_exception(self):
        with self.assertRaises(InvalidCourseCodeException):
            course = Course("2ww01", "English")

    def test_that_course_title_as_int_raises_invalid_course_title_exception(self):
        with self.assertRaises(InvalidCourseTitleException):
            course = Course("201", "English101")

    def test_that_invalid_course_code_length_exception(self):
        with self.assertRaises(InvalidCourseCodeException):
            course = Course("205161", "English")

    def test_that_course_can_be_added_by_students(self):
        course = Course("201", "English")
        self.assertEqual(course.number_of_enrolled_students(), 0)
        course.add_student("Hamid")
        self.assertEqual(course.number_of_enrolled_students(), 1)
        self.assertIn("Hamid", course.enrolled_students)

    def test_that_course_cannot_add_student_that_already_registered_duplicate(self):
        course = Course("201", "English")
        course.add_student("Favour")
        self.assertEqual(course.number_of_enrolled_students(), 1)
        self.assertIn("Favour", course.enrolled_students)
        with self.assertRaises(StudentAlreadyEnrolledException):
            course.add_student("Favour")

    def test_that_course_can_be_removed_by_students(self):
        course = Course("201", "English")
        self.assertEqual(course.number_of_enrolled_students(), 0)
        course.add_student("Hamid")
        self.assertEqual(course.number_of_enrolled_students(), 1)
        course.remove_student("Hamid")
        self.assertEqual(course.number_of_enrolled_students(), 0)

    def test_number_of_students_enrolled_in_the_course(self):
        course = Course("201", "English")
        self.assertEqual(course.number_of_enrolled_students(), 0)
        course.add_student("Hamid")
        self.assertEqual(course.number_of_enrolled_students(), 1)
        course.add_student("Favour")
        self.assertEqual(course.number_of_enrolled_students(), 2)
        course.add_student("Bibi")
        self.assertEqual(course.number_of_enrolled_students(), 3)

    def test_that_empty_course_code_raises_null_exception(self):
        with self.assertRaises(NullException):
            course = Course("", "English")

    def test_that_empty_course_title_raises_null_exception(self):
        with self.assertRaises(NullException):
            course = Course("201", "")

