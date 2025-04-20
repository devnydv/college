from flask import Blueprint

basic = Blueprint("basic", __name__, template_folder='templates')

from college.basic import mainroute