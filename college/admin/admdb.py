from college import app
from flask import request, jsonify
from college.model import db, admin

# ye demo page hai data ko db me save krne k liye 

@app.route("/user/<name>/<email>", methods=["GET"])
def create_user(name, email):
    data = {"name":name, "email":email}
    user = admin(username=data['name'], password=data['email'])
    db.session.add(user)
    db.session.commit()
    return "hmm"
    #return jsonify(user.to_dict())

# READ
# @app.route("/users", methods=["GET"])
# def get_users():
#     users = User.query.all()
#     return jsonify([user.to_dict() for user in users])