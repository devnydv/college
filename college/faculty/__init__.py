from flask import Blueprint

faculty = Blueprint("faculty",__name__, template_folder='templates', static_folder='static', static_url_path='/faculty/static')

from college.faculty import route