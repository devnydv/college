from flask import Blueprint

admin = Blueprint("admin",__name__, template_folder='templates', static_folder='static', static_url_path='/admin/static')

from college.admin import adminroute
from college.admin import addroute
from college.admin import admdb
from college.admin import update
from college.admin import delete