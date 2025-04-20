from flask import Blueprint

basic = Blueprint("basic", __name__, template_folder='templates', static_folder='static', static_url_path='/basic/static')

from college.basic import mainroute