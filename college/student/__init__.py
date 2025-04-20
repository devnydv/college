from flask import Blueprint

student = Blueprint("student",__name__, template_folder='templates', static_folder='static', static_url_path='/student/static')

from college.student import route