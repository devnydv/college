from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}
    
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
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
    facultyid = db.Column(db.Integer, nullable=False)
    education = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    department = db.Column(db.Integer, nullable=False)
    role = db.Column(db.Integer, nullable=False)
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