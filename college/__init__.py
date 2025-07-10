from flask import Flask, jsonify
from college.model import db, admin

app = Flask(__name__)
app.secret_key ="veryverysecretkey"


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db
db.init_app(app)


with app.app_context():
    db.create_all()
#from college.basic import basic