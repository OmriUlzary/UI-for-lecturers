# UI-for-lecturers

Analysis complexity running time of the functions in part A:
Doubly linked list 	Linked list 	Function
θ1
θ1
count(self)
On
θn
get_sub_item(self, items)
On
On
search_value(self, value)
θ1
θ1
is_even(self)
θn
θn
split_linked_list(self, index)
O1
O1
Add_new_head(self, index)
O1
θn
Add_at_end(self, index)
θn
θn
Serialize(self)
θn
θn
_str_(self)
θn
θn
save_to_file()





 



3.
Part B – Grading System Data Structure
In this part of the assignment, we were asked to build a new grading system that should serve the lecturers in "Shenkar" college for the students of industrial engineering and management. we built two classes: student and course which help the main (user interface) to operate the system. 
We implemented the data structure of the system using dictionaries. When choosing function number 1 in the user interface, the user chooses to add a course to the global courses dictionary. This dictionary is mapped in that the dictionary key is the course name and the dictionary value is the object course created in the course class. This object gets the attributes: course name, level, and course number.
When the user selects function number 2 in the user interface, the option opens to add a student to the global students dictionary. This dictionary is mapped in that its key is the student id and the dictionary values are the student object created in the student class with the attributes: name, id, and year of studying.
We chose to use this data structure because of its running time for insert and search is constant O(1). In addition, the dictionary is spent less memory volume relative to other data structures.

Illustration of the data structure:

Value
Key
Algo, Easy, 1	Algo
Math, Hard, 2	Math
Bi, Medium, 3	Bi
  


Value	Key
311144356, Omri, 3	311144356
312535669, Matan, 3	312535669
315371583, Shir, 3	315371583
  









4.
Part B – Grading System Time Complexity
There are 7 buttons from 0 to 6 the user can press and use those options. In each option we will analyze the process and determine the time complexity.
Input 0 ("Exit") – by pressing this button the program print "bye-bye" and the use of the interface will stop.                                                                                                                                                                           Time complexity – θ(1).
Input 1 ("Add Course") – The lecturer provides the course name and the level of the course.  The system checks edge cases before adding the course to the dictionary which called "courses" and finally if there are no problems with the lecturer input, the course will be added to the courses dictionary. 
Time complexity – O(1).                                                                                                                                               Explanation: The searching, checking, and adding the course to "courses" dictionary takes only O(1) time complexity because we do that on a hash table.
Input 2 ("Add Student") – The lecturer provides student id, the name, and the school year of the student. The system checks edge cases before adding the student to the "students" dictionary. If all the inputs are legal, the system will add the student to the dictionary.
Time complexity – O(1).                                                                                                                                                     Explanation: The searching, checking, and adding the student in the "students" dictionary takes only O(1) time complexity because we do that on a hash table.
Input 3 ("Add Grade To Student") – The lecturer provides id student, course name and the grade of the student. if the inputs are legal, the system adds a grade by the function "courses_grade()" we built in student class which gets course name, grade and course level. The level is provided by the function "get_course_level()". Finally, by using the "courses_grade()" function, the grade of the student will be added to the grade dictionary we made in student class.
Time complexity – O(1).                                                                                                                                               Explanation: All the checking and searching in the dictionary cost O(1) because we do that on hash table and the general checking costs O(1) as well. In addition, by adding the grade to the student, the functions "get_course_level()" and  "courses_grade()" costs O(1).
Input 4 ("Get Student Grade") – The lecturer provides the id of the student and gets the dictionary we built in student class which called "grades_dict" which including all the course names and the grades of each course.
Time complexity – O(1).                                                                                                                              Explanation: The checking the legally and the existing of the id in students dictionary costs O(1) and also the printing of the corresponding dictionary. 
Input 5 ("Get Courses By Type") – The lecturer provides a level and receives all the courses at the same level. The system checks the legality of the input, after that it runs on every course in the courses dictionary and adds the courses with the same level to a list called "result".
Time complexity – θ(m).                                                                                                                                       Explanation: By running on every course in the courses dictionary, the system will check the matching between the input to the level in each course. Because of that, it will cost the system time complexity of θ(m) because the system in any case, runs all courses in the dictionary. 
Input 6 ("Get Deans List") - The system runs over all the students in the student dictionary. It calculates the average grade of each student with "get_average_grade()" function we made in student class. The system compares the grade average between the student it just calculated his grade to the student who known as the student with the highest average grade and the same thing will continue until the system runs over all the students.
Time complexity -  θ(nm)                                                                                                                                            Explanation: The system runs in any case on n students and for each student, it runs for m courses to calculate each student grade average. Because of that, it runs θ(nm). 
Total interface complexity – O(nm) 
Explanation: The system can add n students and m courses. Lecturers can add 2t grades to students, the system can provide m courses of each level and can provide the grades of n students. The sum of all of this is n+m+t. However, the system provides the student with the best grades average with a complexity of n*m as well. After all those calculations and with the assumption that there are more courses and students in comparison to lecturers, we conclude that the time complexity of the whole interface is O(nm).      
