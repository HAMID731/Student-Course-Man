from exceptions.exception import InvalidCourseCodeException, InvalidCourseTitleException, \
    StudentAlreadyEnrolledException, CourseAlreadyRegisteredException, NullException


class Course:

    def __init__(self, course_code: str, title: str):
        self.validate_course_code(course_code)
        self.validate_title(title)
        self.__course_code = course_code
        self.__title = title
        self.__enrolled_students = []


    @property
    def course_code(self):
        return self.__course_code

    @course_code.setter
    def course_code(self, course_code):
        self.__course_code = course_code

    @property
    def title(self):
        return self.__title

    @property
    def enrolled_students(self):
        return self.__enrolled_students

    @title.setter
    def title(self, title):
        self.__title = title

    @staticmethod
    def validate_course_code(course_code) -> bool:
        if not course_code:
            raise NullException("Course Code is required")
        if not isinstance(course_code, str) or len(course_code) != 3 or not course_code.isdigit():
            raise InvalidCourseCodeException("Course code must be a 3-digit number")
        return True

    @staticmethod
    def validate_title(title) -> bool:
        if not title:
            raise NullException("Fill the title field")
        if not isinstance(title, str) or not title.isalpha():
            raise InvalidCourseTitleException("title is not valid")
        return True

    def add_student(self, student: str):
        if student in self.__enrolled_students:
            raise StudentAlreadyEnrolledException("Student is already enrolled in this course")
        self.enrolled_students.append(student)

    def remove_student(self, student):
        if not student in self.__enrolled_students:
            raise CourseAlreadyRegisteredException("Course is already registered")
        self.enrolled_students.remove(student)

    def number_of_enrolled_students(self):
        return len(self.__enrolled_students)

    def __repr__(self):
        return (f"Course = {self.course_code}, "
                f"Title =  {self.title})")





