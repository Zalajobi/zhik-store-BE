from flask import Blueprint

from utility.constant import HOSPITAL_BASE_URL

auth = Blueprint('auth', __name__, url_prefix=f'{HOSPITAL_BASE_URL}authentication')

from . import views
