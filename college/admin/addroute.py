from college import app
from flask import render_template, request, redirect, session, url_for
from college.model import db, Student, Faculty, Notice, Subject, Result, Department
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
            student = Student(
            name= data['name'],
            roll= int(data['roll']),
            email=data['email'],
            phone= data['phone'],
            semester= 1,
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


@app.route("/admin/addnotice", methods = ["GET", "POST"])
def addnotice():
    logged = 'user_id' in session
    if logged:
        if request.method == "POST":
            data = request.form
           
            notice = Notice(title= data['title'],
            content= data['content'],
            date=datetime.now().replace(microsecond=0))
            db.session.add(notice)
            db.session.commit()
            return redirect(url_for("notice"))
    return render_template("addnotice.html", data = False)

@app.route("/admin/addcourse", methods = ["GET", "POST"])
def addcourse():
    #inser = addtablerow()
    return render_template("addcourse.html")

@app.route("/admin/adddepartment", methods = ["GET", "POST"])
def adddepartment():
    #inser = addtablerow()
    return render_template("adddepartment.html")



@app.route("/admin/addresult/<id>", methods = ["GET", "POST"])
def addresult(id):
    student = Student.query.get(id)
    if request.method == "POST":
        data = request.form
        
        result = Result(
            mark=data['mark'],
            outoff=data['outoff'],
            remark=data['remark'],
            attendance=data['attendance'],
            student_id= id,
            semester=student.semester,
            status=True if int(data['mark'])/ int(data['outoff']) * 100  >= 35 else False
            )
        
        db.session.add(result)
        if int(data['mark'])/ int(data['outoff']) * 100 >= 35:
            student.semester += 1
            db.session.add(student)
        db.session.commit()
        return redirect(url_for('stdn'))
    
    result = Result.query.filter_by(student_id=id)
    if not result:
        result = None
    
    return render_template("addresult.html", student=student, result = result)






data = {
    "Mechanical Engineering": {
    "First Semester": [
      "Engineering Mathematics I",
      "Physics",
      "Basic Electrical & Electronics Engineering",
      "Engineering Mechanics",
      "Communication Skills",
      "Physics Lab",
      "Basic Engineering Lab",
      "Workshop Practice"
    ],
    "Second Semester": [
      "Engineering Mathematics II",
      "Chemistry",
      "Engineering Thermodynamics",
      "Computer Programming",
      "Engineering Graphics",
      "Programming Lab",
      "Thermodynamics Lab"
    ],
    "Third Semester": [
      "Engineering Mathematics III",
      "Fluid Mechanics",
      "Material Science",
      "Manufacturing Processes",
      "Machine Drawing",
      "Fluid Mechanics Lab",
      "Manufacturing Lab"
    ],
    "Fourth Semester": [
      "Applied Thermodynamics",
      "Strength of Materials",
      "Kinematics of Machines",
      "Electrical Machines & Controls",
      "Measurement & Metrology",
      "Mechanics of Solids Lab",
      "Thermal Lab",
      "Mini Project I"
    ],
    "Fifth Semester": [
      "Dynamics of Machines",
      "Heat & Mass Transfer",
      "Design of Machine Elements",
      "CNC & Automation",
      "HMT Lab",
      "Dynamics Lab",
      "Minor Project II"
    ],
    "Sixth Semester": [
      "Internal Combustion Engines",
      "Refrigeration & Air Conditioning",
      "Finite Element Method (FEM)",
      "Operations Research",
      "IC Engine Lab",
      "CAD Lab",
      "Technical Seminar"
    ],
    "Seventh Semester": [
      "Power Plant Engineering",
      "Industrial Engineering & Management",
      "Additive Manufacturing ",
      "Major Project Phase I",
      "Industry Interaction"
    ],
    "Eighth Semester": [
      "Renewable Energy Systems ",
      "Project Phase II & Final Report",
      "Comprehensive Viva",
      "Internship Presentation",
      "Emerging Trends in Mechanical Engineering"
    ]
  },
}

@app.route("/admin/demo", methods = ["GET", "POST"])
def demo():
    
    for semester, subjects in data["Mechanical Engineering"].items():
        print(semester, subjects)
        for subject in subjects:
            new_subject = Subject(
                name=subject,
                semester=semester,
                dep_id=2  # Assuming department ID is 2 for Mechanical Engineering
            )
            db.session.add(new_subject)
    db.session.commit()
    return "Subjects added successfully"

@app.route("/admin/dept", methods = ["GET", "POST"])
def deptm():
    dept_data = ['Computer Science Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Electronics Engineering']
    for dept in dept_data:
        departments = Department(
            name=dept,
            hod=1
        )
        db.session.add(departments)
    db.session.commit()
    return "Departments added successfully"