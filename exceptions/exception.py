class InvalidCourseCodeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidCourseTitleException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseIsFullException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class StudentAlreadyEnrolledException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseAlreadyRegisteredException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NullException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)