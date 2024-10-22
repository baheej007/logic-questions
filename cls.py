class Student:
    def __init__(self, rollno=None, name=None, mark=None):
        # Initializing the attributes
        self.rollno = rollno
        self.name = name
        self.mark = mark

    def show_details(self):
        # Displaying the student's details
        print(f"Roll Number: {self.rollno}")
        print(f"Name: {self.name}")
        print(f"Mark: {self.mark}\n")

# Creating an object of the Student class using the default constructor
student1 = Student()
# Assigning values to the attributes
student1.rollno = 1
student1.name = "Alice"
student1.mark = 85
# Displaying the details of student1
student1.show_details()

# Creating an object of the Student class using the parameterized constructor
student2 = Student(rollno=2, name="Bob", mark=90)
# Displaying the details of student2
student2.show_details()
