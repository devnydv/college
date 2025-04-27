from college import app
from flask import render_template, request, redirect, session, url_for



@app.route("/admin", methods = ["GET", "POST"])
def admin():
    #inser = addtablerow()
    
    return render_template("dash.html")

@app.route("/admin/student", methods = ["GET", "POST"])
def stdn():
    #inser = addtablerow()
    
    return render_template("student.html")
    

@app.route("/admin/faculty", methods = ["GET", "POST"])
def faculty():
    #inser = addtablerow()
    
    return render_template("faculty.html")


@app.route("/admin/courses", methods = ["GET", "POST"])
def cours():
    #inser = addtablerow()
    
    return render_template("courses.html")


@app.route("/admin/department", methods = ["GET", "POST"])
def dept():
    #inser = addtablerow()
    
    return render_template("department.html")



@app.route("/admin/subject", methods = ["GET", "POST"])
def sub():
    #inser = addtablerow()
    
    return render_template("subject.html")


@app.route("/admin/attendence", methods = ["GET", "POST"])
def attendence():
    #inser = addtablerow()
    
    return render_template("attendence.html")


@app.route("/admin/notice", methods = ["GET", "POST"])
def notice():
    #inser = addtablerow()
    
    return render_template("notice.html")


