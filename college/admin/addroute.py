from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty
from datetime import datetime
from tempdata import semester, gender, departments, designations

allsem =  semester()
dep = departments()
designs = designations()
@app.route("/admin/addstudent", methods = ["GET", "POST"])
def addstdn():
    global logged 
    logged = 'user_id' in session
    if logged:
        if request.method == "POST":
            data = request.form
            student = Student(name= data['name'],
            roll= int(data['roll']),
            email=data['email'],
            phone= data['phone'],
            semester= data['year'],
            dob= datetime.strptime(data['dob'], '%Y-%m-%d').date(),
            gender= data['gender'],
            department= data['department'],
            address= data['address'])
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('stdn'))
        return render_template("addstudent.html", data = False, allsem = allsem, departments = dep)
    return  redirect(url_for("login"))

@app.route("/admin/addfaculty", methods = ["GET", "POST"])
def addfaculty():
    logged = 'user_id' in session
    if logged:
        if request.method == "POST":
            data = request.form
            student = Faculty(name= data['name'],
            facultyid= int(data['facultyid']),
            email=data['email'],
            phone= data['phone'],
            education= data['education'],
            department= data['department'],
            role= data['role'],
            dob= datetime.strptime(data['dob'], '%Y-%m-%d').date(),
            doj= datetime.strptime(data['doj'], '%Y-%m-%d').date(),
            gender= data['gender'],
            address= data['address'])
            db.session.add(student)
            db.session.commit()
            return redirect(url_for("faculty"))
    #inser = addtablerow()
        return render_template("addfaculty.html", data =False, departments = dep, designations = designs)
    return  redirect(url_for("login"))


@app.route("/admin/addcourse", methods = ["GET", "POST"])
def addcourse():
    #inser = addtablerow()
    return render_template("addcourse.html")

@app.route("/admin/adddepartment", methods = ["GET", "POST"])
def adddepartment():
    #inser = addtablerow()
    return render_template("adddepartment.html")



@app.route("/admin/addattendece", methods = ["GET", "POST"])
def addatt():
    #inser = addtablerow()
    return render_template("adddepartment.html")

@app.route("/admin/addnotice", methods = ["GET", "POST"])
def addnotice():
    #inser = addtablerow()
    return render_template("addnotice.html")