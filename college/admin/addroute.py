from college import app
from flask import render_template, request, redirect, session, url_for



@app.route("/admin/addstudent", methods = ["GET", "POST"])
def addstdn():
    form = request.form
    
    
    return render_template("addstudent.html")

@app.route("/admin/addfaculty", methods = ["GET", "POST"])
def addfaculty():
    #inser = addtablerow()
    return render_template("addfaculty.html")

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