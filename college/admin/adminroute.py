from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty, Notice
from tempdata import departments

dep = departments()

@app.route("/admin", methods = ["GET", "POST"])
def admin():
    global logged 
    logged = 'user_id' in session
    if logged:
    #inser = addtablerow()
        
        return render_template("dash.html")
    else:
        return redirect(url_for("login"))

@app.route("/admin/student", methods = ["GET", "POST"])
def stdn():
    logged = 'user_id' in session
    if logged:
    #inser = addtablerow()
        users = Student.query.all()
        return render_template("student.html", students= users, departments= dep)
    else:
        return redirect(url_for("login"))
    
    
    

@app.route("/admin/faculty", methods = ["GET", "POST"])
def faculty():
    logged = 'user_id' in session
    if logged:
        users = Faculty.query.all()
    #inser = addtablerow()
        return render_template("faculty.html", faculties= users)
    else:
        return redirect(url_for("login"))
    


@app.route("/admin/courses", methods = ["GET", "POST"])
def cours():
    logged = 'user_id' in session
    if logged:
    #inser = addtablerow()
        return render_template("courses.html", departments= dep)
    else:
        return redirect(url_for("login"))
    
    


@app.route("/admin/department", methods = ["GET", "POST"])
def dept():
    logged = 'user_id' in session
    if logged:
    #inser = addtablerow()
        return render_template("department.html")
    else:
        return redirect(url_for("login"))
    
    






@app.route("/admin/attendence", methods = ["GET", "POST"])
def attendence():
    logged = 'user_id' in session
    if logged:
    #inser = addtablerow()
        return render_template("attendence.html")
    else:
        return redirect(url_for("login"))
    
    


@app.route("/admin/notice", methods = ["GET", "POST"])
def notice():
    logged = 'user_id' in session
    if logged:
        notices = Notice.query.all()
        
        return render_template("notice.html", notices=notices, data= False)
    else:
        return redirect(url_for("login"))
    
    


