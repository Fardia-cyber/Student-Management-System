import numpy as np

# Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = np.array([])  # Initialize an empty numpy array for grades

    def add_grades(self, grades):
        """
        Adds a list of grades to the student's grades.
        """
        self.grades = np.append(self.grades, grades)

    def calculate_average(self):
        """
        Returns the average of the student's grades using numpy.
        """
        return np.mean(self.grades) if self.grades.size > 0 else 0

    def determine_grade(self):
        """
        Determines the final letter grade based on the average.
        """
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_student_info(self):
        """
        Displays the student's name, ID, grades, and final grade.
        """
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Grades: {self.grades}")
        print(f"Average Grade: {self.calculate_average():.2f}")
        print(f"Final Grade: {self.determine_grade()}")
        print("-" * 30)

# School class
class School:
    def __init__(self):
        self.students = []
        self.courses = []  # Initialize an empty list for courses

    def add_student(self, student):
        """
        Adds a student to the school.
        """
        self.students.append(student)

    def display_all_students(self):
        """
        Displays information for all students in the school.
        """
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            student.display_student_info()

    def calculate_class_average(self):
        """
        Calculates the average grade for the whole class.
        """
        if not self.students:
            return 0
        total_average = np.mean([student.calculate_average() for student in self.students])
        return total_average

    def add_course(self, course_name):
        """
        Adds a new course to the school.
        """
        self.courses.append(course_name)
        print(f"Course '{course_name}' added successfully!")

    def display_courses(self):
        """
        Displays all available courses.
        """
        if not self.courses:
            print("No courses available.")
        else:
            print("Available Courses:")
            for course in self.courses:
                print(f"- {course}")

# Authentication system
class Authentication:
    def __init__(self):
        self.users = {"admin": "admin123"}  # Default admin credentials

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in self.users and self.users[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid credentials.")
            return False

    def register(self):
        username = input("Enter new username: ")
        if username in self.users:
            print("Username already exists.")
            return False
        password = input("Enter new password: ")
        self.users[username] = password
        print("Registration successful!")
        return True

# Main interaction
def main():
    school = School()
    auth = Authentication()

    while True:
        print("\nWelcome to the Student Management System")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            if auth.login():
                while True:
                    print("\nStudent Grading System")
                    print("1. Add Student")
                    print("2. View All Students")
                    print("3. Class Average")
                    print("4. Add Course")
                    print("5. View Courses")
                    print("6. Logout")

                    sub_choice = input("Choose an option: ")

                    if sub_choice == "1":
                        name = input("Enter student's name: ")
                        student_id = input("Enter student's ID: ")
                        student = Student(name, student_id)

                        while True:
                            grades_input = input(f"Enter grades for {name} separated by space: ")
                            try:
                                grades = list(map(float, grades_input.split()))
                                student.add_grades(grades)
                                break
                            except ValueError:
                                print("Invalid input. Please enter numeric values for grades.")

                        school.add_student(student)
                        print(f"Student {name} added successfully!")

                    elif sub_choice == "2":
                        print("\nAll Students Information:")
                        school.display_all_students()

                    elif sub_choice == "3":
                        class_avg = school.calculate_class_average()
                        print(f"Class Average: {class_avg:.2f}")

                    elif sub_choice == "4":
                        course_name = input("Enter the course name: ")
                        school.add_course(course_name)

                    elif sub_choice == "5":
                        school.display_courses()

                    elif sub_choice == "6":
                        print("Logging out...")
                        break

                    else:
                        print("Invalid choice. Please try again.")

        elif choice == "2":
            auth.register()

        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
