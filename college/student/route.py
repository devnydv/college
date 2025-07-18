from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty, Notice, Result
from sqlalchemy import desc

@app.route("/studentprofile/<id>", methods = ["GET", "POST"])
def student_profile(id):
    global logged 
    logged = 'student' in session
    if logged:
        student = Student.query.get(id)
        notices = Notice.query.order_by(desc(Notice.id)).limit(3).all()
        result = Result.query.filter_by(student_id=id).all()

        if not student:
            return "Student not found", 404
        return render_template("student-profile.html", student=student, id=id, results=result, logged_in=True, notices=notices)
    return redirect(url_for("login"))

