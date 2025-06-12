from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty
from datetime import datetime
from tempdata import semester, departments, designations

designs = designations()
sem = semester()
dep = departments()

@app.route("/admin/update/student/<id>", methods = ["GET", "POST"])
def updatestdn(id):
    if request.method == "POST":
        data = request.form
        student = Student.query.get(id)
        student.name= data['name']
        student.roll= int(data['roll'])
        student.email=data['email']
        student.phone= data['phone']
        student.semester= data['year']
        date = datetime.strptime(data['dob'], '%Y-%m-%d').date()
        student.dob= date
        student.gender= data['gender']
        student.department= data['department']
        student.address= data['address']
        db.session.commit()
        url_for("stdn")
    
    student = Student.query.get(id)
    
    return render_template("addstudent.html", data= student, allsem = sem, departments= dep)


@app.route("/admin/update/faculty/<id>", methods = ["GET", "POST"])
def updatefaculty(id):
    if request.method == "POST":
        data = request.form
        print(data)
        faculty = Faculty.query.get(id)
        faculty.name = data['name']
        faculty.facultyid = data['facultyid']
        faculty.education = data['education']
        faculty.email =data['email']
        faculty.phone = data['phone']
        faculty.department = data['department']
        faculty.role = data['role']
        faculty.dob = datetime.strptime(data['dob'], '%Y-%m-%d').date()
        faculty.doj = datetime.strptime(data['doj'], '%Y-%m-%d').date()
        faculty.gender = data['gender']
        faculty.address = data['address']
        db.session.commit()
        url_for("faculty")
    faculty = Faculty.query.get(id)
    return render_template("addfaculty.html", data= faculty, departments= dep, designations = designs)