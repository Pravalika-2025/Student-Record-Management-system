
from student import Student
from file_handler import save_students, load_students

# Load existing records
students = load_students()

while True:

    print("\n===================================")
    print("   STUDENT RECORD MANAGEMENT SYSTEM")
    print("===================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    print("===================================")

    choice = input("Enter your choice: ").strip()

    # 1. ADD STUDENT
    if choice == "1":
        try:
            student_id = int(input("Enter Student ID: "))

            if any(s.student_id == student_id for s in students):
                print("Student ID already exists!")

            else:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                department = input("Enter Department: ")
                marks = float(input("Enter Marks: "))

                student = Student(
                    student_id, name, age, department, marks
                )

                students.append(student)
                save_students(students)

                print("Student added successfully!")

        except ValueError:
            print("Invalid input! Enter correct values.")

    # 2. VIEW STUDENTS
    elif choice == "2":

        if not students:
            print("No student records found.")

        else:
            print("\n----- STUDENT RECORDS -----")

            for student in students:
                print("-------------------------")
                student.display()

    # 3. SEARCH STUDENT
    elif choice == "3":
        try:
            search_id = int(input("Enter Student ID to search: "))
            found = False

            for student in students:
                if student.student_id == search_id:
                    print("\nStudent Found!")
                    student.display()
                    found = True
                    break

            if not found:
                print("Student not found.")

        except ValueError:
            print("Please enter a valid Student ID.")

    # 4. UPDATE STUDENT
    elif choice == "4":
        try:
            update_id = int(input("Enter Student ID to update: "))
            found = False

            for student in students:
                if student.student_id == update_id:

                    print("\nExisting Details:")
                    student.display()

                    print("\nEnter Updated Details:")

                    new_name = input("Enter New Name: ")
                    new_age = int(input("Enter New Age: "))
                    new_department = input("Enter New Department: ")
                    new_marks = float(input("Enter New Marks: "))

                    student.name = new_name
                    student.age = new_age
                    student.department = new_department
                    student.marks = new_marks

                    save_students(students)

                    print("Student updated successfully!")
                    found = True
                    break

            if not found:
                print("Student not found.")

        except ValueError:
            print("Invalid input! Please enter correct values.")

    # 5. DELETE STUDENT
    elif choice == "5":
        try:
            delete_id = int(input("Enter Student ID to delete: "))
            found = False

            for student in students:
                if student.student_id == delete_id:

                    students.remove(student)
                    save_students(students)

                    print("Student deleted successfully!")
                    found = True
                    break

            if not found:
                print("Student not found.")

        except ValueError:
            print("Please enter a valid Student ID.")

    # 6. EXIT
    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")
