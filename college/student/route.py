from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty, Notice

@app.route("/studentprofile/<id>", methods = ["GET", "POST"])
def student_profile(id):
    student = Student.query.get(id)
    print(student)
    if not student:
        return "Student not found", 404
    return render_template("student-profile.html", student=student, id=id)
