class Course:
    def __init__(self, course_name, level, course_number):
        self.course_name = course_name
        self.level = level
        self.course_number = course_number

    def __str__(self):
        return "course_number:" + str(self.course_number) + " " + "name:" + str(self.course_name) + " " + "level:" + str(self.level)



