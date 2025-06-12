from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty
from datetime import datetime
from tempdata import semester, departments, designations

designs = designations()

@app.route("/admin/update/student/<id>", methods = ["GET", "POST"])
def updatestdn(id):
    if request.method == "POST":
        data = request.form
        student = Student.query.get(id)
        student.name= data['name'],
        student.roll= int(data['roll']),
        student.email=data['email'],
        student.phone= data['phone'],
        student.semester= data['year'],
        date = datetime.strptime(data['dob'], '%Y-%m-%d').date(),
        student.dob= date
        student.gender= data['gender'],
        student.department= data['department'],
        student.address= data['address']
        db.session.commit()
        return 'hmm'
    sem = semester()
    dep = departments()
    student = Student.query.get(id)
    print(student.name)
    return render_template("addstudent.html", data= student, allsem = sem, departments= dep)


@app.route("/admin/update/faculty/<id>", methods = ["GET", "POST"])
def updatefaculty(id):
    sem = semester()
    dep = departments()
    faculty = Faculty.query.get(id)
    
    return render_template("addfaculty.html", data= faculty, departments= dep, designations = designs)