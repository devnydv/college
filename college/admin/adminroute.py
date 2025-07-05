from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty, Notice
from tempdata import departments
from sqlalchemy import desc

dep = departments()

@app.route("/admin", methods = ["GET", "POST"])
def admin():
    total_student = Student.query.count()
    total_faculty = Faculty.query.count()
    notices = Notice.query.order_by(desc(Notice.id)).limit(3).all()
    
    global logged
    logged = 'user_id' in session
    if logged:
    #inser = addtablerow()
        return render_template("dash.html", total_student=total_student, total_faculty=total_faculty, notices=notices, departments=dep)
    else:
        return redirect(url_for("login"))

@app.route("/admin/student", methods = ["GET", "POST"])
def stdn():
    logged = 'user_id' in session
    if logged:
    #inser = addtablerow()
        users = Student.query.all()
        for user in users:
            print(user.semester_.name)
        return render_template("student.html", students= users, departments= dep)
    else:
        return redirect(url_for("login"))
    
    
    

@app.route("/admin/faculty", methods = ["GET", "POST"])
def faculty():
    logged = 'user_id' in session
    if logged:
        users = Faculty.query.all()
    #inser = addtablerow()
        return render_template("faculty.html", faculties= users, departments= dep)
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
        users = Faculty.query.filter_by(role="Head of the Department").all()
        print(users)
        return render_template("department.html", hod = users)
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
    
    


