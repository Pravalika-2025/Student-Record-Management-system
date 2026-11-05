class Student:
    def __init__(self, student_id, name, age, department, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.marks = marks

    def display(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Marks:", self.marks)