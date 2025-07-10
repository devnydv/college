from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}




class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, db.ForeignKey('semester.id'), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String, nullable=False)
    department = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "roll": self.roll,
            "email": self.email,
            "phome": self.phone,
            "semmester": self.semmester,
            "dob": self.dob,
            'gender': self.gender,
            'department': self.department,
            "address": self.address,
            }
    

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    facultyid = db.Column(db.String(100), unique=True, nullable=False)
    education = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    department = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    doj = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
   
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.name,
            "facultyid": self.facultyid,
            "education": self.education,
            "email": self.email,
            "phone": self.phone,
            'department': self.department,
            'role': self.role,
            "dob": self.dob,
            "doj": self.doj,
            'gender': self.gender,
            "address": self.address,
            }

class Notice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "date": self.date
        }
    

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    hod = db.Column(db.String(100), nullable=False)
    subjects = db.relationship('Subject', backref='subject_', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "hod": self.hod
        }
    

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    semester = db.Column(db.String(100), nullable=False)
    dep_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "semester": self.semester,
            "dep_id": self.dep_id
        }

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mark = db.Column(db.Integer, nullable=False)
    outoff = db.Column(db.Integer, nullable=False)
    attendance = db.Column(db.Integer, nullable=False)
    remark = db.Column(db.String(100), nullable=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    semester = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "mark": self.mark,
            "outoff": self.outoff,
            "remark": self.remark,
            "student_id": self.student_id,
            "semester": self.semester,
            "status": self.status
        }
    

class Semester(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    students = db.relationship('Student', backref='semester_', lazy=True)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }