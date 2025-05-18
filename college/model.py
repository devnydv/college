from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "password": self.password}
    
class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    roll = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    dob = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Integer, primary_key=True)
   