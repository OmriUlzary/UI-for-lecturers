
class Student:
    def __init__(self, id, name, year_of_studying):
        self.id = id
        self.name = name
        self.year_of_studying = year_of_studying
        self.grades_dict = {}

    def __str__(self):
        return "id:" + str(self.id) + " " + "name:" + str(self.name) + " " + "year_of_studying:" + str(self.year_of_studying)

    def courses_grades(self, course_name, grade, level):
        if level not in ["Easy", "Medium", "Hard"]:
            return "Error"
        elif level == "Easy":
            grade = grade
        elif level == "Medium":
            grade *= 1.1
        else:
            grade *= 1.25
        if grade > 100:
            grade = 100
        self.grades_dict[course_name] = grade
        return self.grades_dict


    def get_average_grade(self):
        sum = 0
        for course in self.grades_dict.keys():
            sum += self.grades_dict[course]
        return sum / len(self.grades_dict.keys())



