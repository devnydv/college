from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty
from datetime import datetime
from tempdata import semester
@app.route("/admin/update/student/<id>", methods = ["GET", "POST"])
def updatestdn(id):
    sem = semester()
    student = Student.query.get(id)
    print(student.name)
    return render_template("addstudent.html", data= student, allsem = sem)