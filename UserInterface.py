from student import Student
from course import Course
courses_dict = {}
students_dict = {}

def get_course_level(course_name):
    if course_name in courses_dict:
        return courses_dict[course_name].level

while True:
    print("Welcome dear lecturer! Please choose an option:")
    print("(0) - Exit")
    print("(1) - Add Course")
    print("(2) - Add Student")
    print("(3) - Add Grade To Student")
    print("(4) - Get Student Grade")
    print("(5) - Get Courses By Type")
    print("(6) - Get Deans List")

    choice = int(input())

    if choice == 0:
        print("Bye Bye")
        break

    if choice == 1:
        course_name = str(input("Please enter course name"))
        if len(course_name) == 0:
            print("Please enter course name again")
        else:
            level = input("Please enter course level")
            if level not in ["Easy", "Medium", "Hard"]:
                print("Please enter levels: Easy, Medium or Hard")
            else:
                course_number = len(courses_dict.keys()) + 1
                course = Course(course_name, level, course_number)
                if course_name in courses_dict:
                    print("The course is already exists")
                else:
                    courses_dict[course.course_name] = course
                    print("The course added successfully!")

    if choice == 2:
        id = input("Please enter student id")
        if len(id) != 9:
            print("Please enter 9 digits of id")
        elif id in students_dict:
            print("The student is already exists")
        else:
            name = input("Please enter student name")
            if len(name) == 0:
                print("You didn't enter name")
            year_of_studying = int(input("Please enter year of studying"))
            if year_of_studying not in range(1, 8):
                print("Not a possible year")
            else:
                student = Student(id, name, year_of_studying)
                students_dict[id] = student
                print("The student added successfully!")

    if choice == 3:
        id = input("Please enter student id")
        if len(id) != 9:
            print("Please enter 9 digits of id")
        elif id not in students_dict:
            print("The student does not exist")
        else:
            course_name = input("Please enter course name")
            if course_name not in courses_dict:
                print("The course does not exists")
                continue
            grade = int(input("Please enter grade"))
            if grade > 100 or grade < 0:
                print("Illegal grade")
                continue
            if course_name in students_dict[id].grades_dict:
                print("The student has already a grade")
            else:
                students_dict[id].courses_grades(course_name, grade, get_course_level(course_name))
                print("The grade is added to the student")

    if choice == 4:
        id = input("Please enter student id")
        if len(id) != 9:
            print("Please enter 9 digits of id")
        else:
            if id in students_dict:
                print(students_dict[id].grades_dict)
            else:
                print("Student does not exist")

    if choice == 5:
        level = input("Please enter a level")
        if level not in ["Easy", "Medium", "Hard"]:
            print("This is not a level")
        else:
            result = []
            for course_name in courses_dict:
                if level in courses_dict[course_name].level:
                    result.append(course_name)
                    print(result)

    if choice == 6:
        max_average = 0
        the_best_student = None
        for id in students_dict.keys():
            student_average = students_dict[id].get_average_grade()
            if student_average > max_average:
                max_average = student_average
                the_best_student = students_dict[id].name
        print(the_best_student)