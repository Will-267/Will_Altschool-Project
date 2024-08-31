# Base class Person
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def __str__(self):
        return f'Name: {self.name}, ID: {self.id_number}'

# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number)
        self.major = major

    def __str__(self):
        return f'{super().__str__()}, Major: {self.major}'

# Instructor class inheriting from Person
class Instructor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self):
        return f'{super().__str__()}, Department: {self.department}'

# Course class to represent a course with a list of enrolled students
class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name
        self.course_id = course_id
        self.enrolled_students = []  # List to track enrolled students

    def add_student(self, student):
        self.enrolled_students.append(student)

    def remove_student(self, student):
        self.enrolled_students.remove(student)

    def __str__(self):
        student_list = ', '.join([student.name for student in self.enrolled_students])
        return f'Course Name: {self.course_name}, Course ID: {self.course_id}, Enrolled Students: {student_list}'

# Enrollment class to represent the enrollment of a student in a course
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None  # Grade is initially None

    def assign_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f'Student: {self.student.name}, Course: {self.course.course_name}, Grade: {self.grade}'

# Student Management System class to manage students, instructors, courses, and enrollments
class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store students with their ID numbers
        self.instructors = {}  # Dictionary to store instructors with their ID numbers
        self.courses = {}  # Dictionary to store courses with their course IDs
        self.enrollments = []  # List to store enrollments

    # Methods to add, remove, and update students
    def add_student(self, student):
        self.students[student.id_number] = student

    def remove_student(self, id_number):
        if id_number in self.students:
            del self.students[id_number]

    def update_student(self, id_number, name=None, major=None):
        if id_number in self.students:
            if name:
                self.students[id_number].name = name
            if major:
                self.students[id_number].major = major

    # Methods to add, remove, and update instructors
    def add_instructor(self, instructor):
        self.instructors[instructor.id_number] = instructor

    def remove_instructor(self, id_number):
        if id_number in self.instructors:
            del self.instructors[id_number]

    def update_instructor(self, id_number, name=None, department=None):
        if id_number in self.instructors:
            if name:
                self.instructors[id_number].name = name
            if department:
                self.instructors[id_number].department = department

    # Methods to add, remove, and update courses
    def add_course(self, course):
        self.courses[course.course_id] = course

    def remove_course(self, course_id):
        if course_id in self.courses:
            del self.courses[course_id]

    def update_course(self, course_id, course_name=None):
        if course_id in self.courses and course_name:
            self.courses[course_id].course_name = course_name

    # Method to enroll students in courses
    def enroll_student_in_course(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            course.add_student(student)
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)
            return enrollment
        else:
            print(f"Enrollment failed: Student ID {student_id} or Course ID {course_id} does not exist.")

    # Method to assign grades to students
    def assign_grade(self, student_id, course_id, grade):
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id and enrollment.course.course_id == course_id:
                enrollment.assign_grade(grade)
                break

    # Method to retrieve a list of students enrolled in a specific course
    def get_students_in_course(self, course_id):
        if course_id in self.courses:
            return self.courses[course_id].enrolled_students
        return []

    # Method to retrieve a list of courses a specific student is enrolled in
    def get_courses_for_student(self, student_id):
        if student_id in self.students:
            courses = [enrollment.course for enrollment in self.enrollments if enrollment.student.id_number == student_id]
            return courses
        return []