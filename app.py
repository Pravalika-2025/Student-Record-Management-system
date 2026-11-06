
from flask import Flask, render_template, request, redirect, url_for
from file_handler import load_students, save_students
from student import Student

app = Flask(__name__)


@app.route("/")
def home():
    students = load_students()

    total_students = len(students)

    departments = len(set(
        student.department for student in students
    ))

    return render_template(
        "index.html",
        students=students,
        total_students=total_students,
        departments=departments
    )


@app.route("/add-student", methods=["GET", "POST"])
def add_student():

    error = None

    if request.method == "POST":

        try:
            student_id = int(request.form["student_id"])
            name = request.form["name"].strip()
            age = int(request.form["age"])
            department = request.form["department"].strip()
            marks = float(request.form["marks"])

            students = load_students()

            if not name or not department:
                raise ValueError("Name and department cannot be empty.")

            if age <= 0:
                raise ValueError("Age must be greater than zero.")

            if not 0 <= marks <= 100:
                raise ValueError("Marks must be between 0 and 100.")

            if any(s.student_id == student_id for s in students):
                raise ValueError("This Student ID already exists.")

            new_student = Student(
                student_id,
                name,
                age,
                department,
                marks
            )

            students.append(new_student)
            save_students(students)

            return redirect(url_for("home"))

        except ValueError as e:
            error = str(e)

        except (KeyError, TypeError):
            error = "Please fill in all the fields correctly."

    return render_template("add_student.html", error=error)


@app.route("/search", methods=["GET", "POST"])
def search_student():

    student = None
    message = None

    if request.method == "POST":
        try:
            student_id = int(request.form["student_id"])
            students = load_students()

            for s in students:
                if s.student_id == student_id:
                    student = s
                    break

            if student is None:
                message = "No student found with this ID."

        except ValueError:
            message = "Please enter a valid Student ID."

    return render_template(
        "search_student.html",
        student=student,
        message=message
    )


@app.route("/update-student", methods=["GET", "POST"])
def update_student():

    student = None
    message = None
    success = False

    if request.method == "POST":

        try:
            student_id = int(request.form["student_id"])
            students = load_students()

            for s in students:
                if s.student_id == student_id:
                    student = s
                    break

            if student is None:
                message = "Student not found."

            else:
                name = request.form["name"].strip()
                age = int(request.form["age"])
                department = request.form["department"].strip()
                marks = float(request.form["marks"])

                if not name or not department:
                    raise ValueError("Name and department cannot be empty.")

                if age <= 0:
                    raise ValueError("Age must be greater than zero.")

                if not 0 <= marks <= 100:
                    raise ValueError("Marks must be between 0 and 100.")

                student.name = name
                student.age = age
                student.department = department
                student.marks = marks

                save_students(students)

                message = "Student updated successfully!"
                success = True

        except ValueError as e:
            message = str(e)

        except (KeyError, TypeError):
            message = "Please enter valid student details."

    return render_template(
        "update_student.html",
        student=student,
        message=message,
        success=success
    )


@app.route("/delete-student/<int:student_id>", methods=["POST"])
def delete_student(student_id):

    students = load_students()

    updated_students = [
        student for student in students
        if student.student_id != student_id
    ]

    if len(updated_students) < len(students):
        save_students(updated_students)

    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
