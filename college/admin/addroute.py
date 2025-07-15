from college import app
from flask import render_template, request, redirect, session, url_for, flash
from college.model import Semester, db, Student, Faculty, Notice, Subject, Result, Department
from datetime import datetime
from tempdata import semester, gender, departments, designations
from sqlalchemy.exc import IntegrityError

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
            try:
                db.session.add(student)
                db.session.commit()
                return redirect(url_for("faculty"))
            except IntegrityError:
                db.session.rollback()
                flash("Email, roll number or phone number already exists.")
                return redirect(url_for("addfaculty"))
                
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
    return  redirect(url_for("login"))


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
    global logged 
    logged = 'user_id' in session
    if logged:
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
  "Computer Science Engineering": {
    "First Semester": [
      "Engineering Mathematics I",
      "Physics",
      "Programming for Problem Solving",
      "Basic Electrical and Electronics Engineering",
      "Engineering Graphics and Workshop",
      "Communication Skills",
      "Physics Lab",
      "Programming Lab"
    ],
    "Second Semester": [
      "Engineering Mathematics II",
      "Chemistry",
      "Data Structures",
      "Digital Logic Design",
      "Environmental Studies",
      "Data Structures Lab",
      "Digital Logic Lab"
    ],
    "Third Semester": [
      "Discrete Mathematics",
      "Computer Organization and Architecture",
      "Object Oriented Programming",
      "Operating Systems",
      "Design and Analysis of Algorithms",
      "OOPs Lab",
      "OS Lab and Algorithm Lab"
    ],
    "Fourth Semester": [
      "Theory of Computation",
      "Database Management Systems",
      "Computer Networks",
      "Software Engineering",
      "DBMS Lab",
      "CN Lab",
      "Mini Project I"
    ],
    "Fifth Semester": [
      "Compiler Design",
      "Web Technologies",
      "Artificial Intelligence",
      "Professional Ethics",
      "Web Tech Lab",
      "Compiler Design Lab",
      "Minor Project II"
    ],
    "Sixth Semester": [
      "Cloud Computing and  IoT",
      "Mobile App Development and Big Data",
      "Cybersecurity",
      "Major Project Phase I",
      "Aptitude & Reasoning Skills",
      "Technical Seminar"
    ],
    "Seventh Semester": [
      "Data Science",
      "Research Methodology",
      "Industrial Management",
      "Major Project Phase II",
      "Internship and Field Work"
    ],
    "Eighth Semester": [
      "Major Project Final Submission",
      "Viva Voce",
      "Internship Report",
      "Emerging Technologies",
      "Capstone Project"
    ]
  },

  "Electronics Engineering": {
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
      "Basic Electronics Engineering",
      "Network Theory",
      "Environmental Science",
      "Basic Electronics Lab",
      "Network Lab"
    ],
    "Third Semester": [
      "Engineering Mathematics III",
      "Analog Electronics",
      "Digital Electronics",
      "Signals and Systems",
      "Electronic Measurement and Instrumentation",
      "Analog Electronics Lab",
      "Digital Electronics Lab"
    ],
    "Fourth Semester": [
      "Electromagnetic Fields",
      "Microprocessors and Microcontrollers",
      "Analog Communication",
      "Control Systems",
      "Microprocessor Lab",
      "Communication Lab",
      "Mini Project I"
    ],
    "Fifth Semester": [
      "Digital Communication",
      "VLSI Design",
      "Embedded Systems",
      "Antenna and Wave Propagation",
      "VLSI Lab",
      "Digital Communication Lab",
      "Minor Project II"
    ],
    "Sixth Semester": [
      "Microwave Engineering",
      "Digital Signal Processing",
      "Industrial Automation and Robotics",
      "IoT and Embedded Systems",
      "DSP Lab",
      "Microwave Lab",
      "Technical Seminar"
    ],
    "Seventh Semester": [
      "Wireless and Mobile Communication",
      "Optical Communication",
      "Machine Learning",
      "Major Project Phase I",
      "Internship and Technical Seminar"
    ],
    "Eighth Semester": [
      "Satellite Communication and Advanced VLSI",
      "Major Project Final Phase",
      "Viva Voce",
      "Internship Report",
      "Emerging Technologies in Electronics"
    ]
  },

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

  "Civil Engineering": {
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
      "Programming for Problem Solving",
      "Engineering Graphics",
      "Environmental Science",
      "Programming Lab",
      "Engineering Graphics Lab"
    ],
    "Third Semester": [
      "Engineering Mathematics III",
      "Building Materials & Construction",
      "Strength of Materials",
      "Surveying I",
      "Fluid Mechanics",
      "Materials Testing Lab",
      "Surveying Lab"
    ],
    "Fourth Semester": [
      "Structural Analysis I",
      "Concrete Technology",
      "Transportation Engineering I",
      "Geotechnical Engineering I",
      "Surveying II",
      "Concrete Lab",
      "Soil Mechanics Lab",
      "Mini Project I"
    ],
    "Fifth Semester": [
      "Structural Analysis II",
      "Design of Reinforced Concrete Structures",
      "Geotechnical Engineering II",
      "Transportation Engineering II",
      "Construction Planning & Management",
      "Geotech Lab II",
      "Structural Design Lab",
      "Minor Project II"
    ],
    "Sixth Semester": [
      "Design of Steel Structures",
      "Water Supply & Wastewater Engineering",
      "Environmental Engineering",
      "Estimation, Costing & Valuation",
      "Open Channel Flow ",
      "Environmental Engg. Lab",
      "CAD in Civil Lab",
      "Industrial Training"
    ],
    "Seventh Semester": [
      "Irrigation & Hydraulic Structures",
      "Advanced Foundation Engineering ",
      "Remote Sensing & GIS",
      "Ethics",
      "Major Project Phase I",
      "Technical Seminar"
    ],
    "Eighth Semester": [
      "Green Building Technologies",
      "Major Project Final Submission",
      "Viva Voce",
      "Internship Report",
      "Emerging Trends in Civil Engineering"
    ]
  }
}

@app.route("/admin/data", methods = ["GET", "POST"])
def add_data():
    def addsemester():
        for sem in allsem:
            semester = Semester(name=sem)
            db.session.add(semester)
        db.session.commit()
    addsemester()

    def adddep():
      dept_data = ['Computer Science Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Electronics Engineering']
      for dept in dept_data:
          departments = Department(
              name=dept,
              hod=1
          )
          db.session.add(departments)
      db.session.commit()
    adddep()
    for dept in dep :
        for semester, subjects in data[dept].items():
            for subject in subjects:
                new_subject = Subject(
                    name=subject,
                    semester=semester,
                    dep_id= dep.index(dept) + 1  # Assuming department IDs start from 1
                )
                db.session.add(new_subject)
        db.session.commit()
    return "Data added successfully"




