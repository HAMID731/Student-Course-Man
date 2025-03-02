from exceptions.exception import InvalidCourseCodeException, InvalidCourseTitleException, \
    StudentAlreadyEnrolledException, CourseAlreadyRegisteredException


class Course:

    def __init__(self, course_code: int, title: str):
        self.validate_course_code(course_code)
        self.__course_code = course_code
        self.__title = title
        self.enrolled_students = []


    @property
    def course_code(self):
        return self.__course_code

    @course_code.setter
    def course_code(self, course_code):
        self.__course_code = course_code

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @staticmethod
    def validate_course_code(course_code) -> bool:
        if not isinstance(course_code, int):
            raise InvalidCourseCodeException("course code is not valid")
        return True

    @staticmethod
    def validate_title(title) -> bool:
        if not isinstance(title, str):
            raise InvalidCourseTitleException("title is not valid")
        return True

    def add_student(self, student):
        if student in self.enrolled_students:
            raise StudentAlreadyEnrolledException("Student is already enrolled in this course")
        self.enrolled_students.append(student)

    def remove_student(self, student):
        if student in self.enrolled_students:
            raise CourseAlreadyRegisteredException("Course is already registered")
        self.enrolled_students.remove(student)

    def number_of_enrolled_students(self):
        return len(self.enrolled_students)

    def __repr__(self):
        return (f"Course = {self.course_code}, "
                f"Title =  {self.title})")





