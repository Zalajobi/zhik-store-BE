from flask import Flask, session
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_session import Session
from db import db

# Blueprint
from customers.views.address import address_blueprint
from customers.views.customer import user_blueprint
# from admin.views.providers import admin_provider_blueprint as admin_blueprint
from admin import admin as admin_blueprint

# utilities
from utility.constant import DATABASE_URL, SECRET_KEY, JWT_SECRET_KEY
from utility.environ import set_environment_variables

# Models
from model.enum_static import Hostpital_Department, HospitalUnit, ProviderRoles
from model.User import Customer
from model.Address import Address
from model.Socials import Socials
from model.Product import Product, ProductImages
from model.Provider import ProviderTable
from model.Departments import DepartmentTable
from model.Unit import UnitTable
from model.Role import RoleTable
from utility.libraries import setup_imageKit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/zhik-store'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = SECRET_KEY
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)
Session(app)


@app.before_first_request
def create_tables():
    db.create_all()


# Blueprints
app.register_blueprint(user_blueprint)
app.register_blueprint(address_blueprint)
app.register_blueprint(admin_blueprint)
set_environment_variables()

# Third Party Libraries
setup_imageKit()


@app.route('/', methods=['GET'])
def upload_file():
    # roles = HospitalUnit
    #
    # for dept in roles:
    #     hospital_unit = UnitTable(name=dept.value)
    #     hospital_unit.save_to_db()
    #
    #     print(f"Saved {hospital_unit.name} to Database")

    return 'Welcome to ZhikStores'


def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001, debug=True)
