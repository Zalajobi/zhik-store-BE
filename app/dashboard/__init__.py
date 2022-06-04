from flask import Blueprint

from utility.constant import HOSPITAL_BASE_URL

dashboard = Blueprint('dashboard', __name__, url_prefix=f'{HOSPITAL_BASE_URL}dashboard')

from .views import *
