from flask import Blueprint

from utility.constant import HOSPITAL_BASE_URL

admin = Blueprint('admin', __name__, url_prefix=f'{HOSPITAL_BASE_URL}admin')

from .views import *
