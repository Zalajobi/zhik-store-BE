import json
from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_session import Session
from app.db import db

# Blueprint
from app.customers.views.address import address_blueprint
from app.customers.views.customer import user_blueprint
from app.admin import admin as admin_blueprint
from app.auth import auth as auth_blueprint
from app.dashboard import dashboard as dashboard_blueprint

# utilities
from utility.constant import SECRET_KEY, JWT_SECRET_KEY
from utility.environ import set_environment_variables

# Models
from app.model.Unit import UnitTable
from app.model.Departments import DepartmentTable
from app.model.Role import RoleTable
from app.model.Provider import ProviderTable
from app.model.Product import ProductImages, Product
from app.model.Socials import Socials
from app.model.Address import Address
from app.model.User import Customer
from app.model.Registration import RegistrationTable
from app.model.Patient import PatientTable

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
app.register_blueprint(auth_blueprint)
app.register_blueprint(dashboard_blueprint)

set_environment_variables()

# Third Party Libraries
setup_imageKit()


@app.route('/', methods=['GET'])
def upload_file():
    # open_json = open('static/data/json/patients3.json')
    # data = json.load(open_json)
    #
    # provider = ProviderTable.find_by_username("zalajobi")
    # unit = db.session.query(UnitTable).first()
    # registration = db.session.query(RegistrationTable).first()
    #
    # for patient in data:
    #     new_patient = PatientTable(
    #         patient_hospital_id=patient['patient_hospital_id'],
    #         first_name=patient['first_name'],
    #         last_name=patient['last_name'],
    #         middle_name=patient['middle_name'],
    #         email=patient['email'],
    #         phone_number=patient['phone_number'],
    #         gender=patient['gender'],
    #         title=patient['title'],
    #         dob=patient['dob'],
    #         next_of_kin_name=patient['next_of_kin_name'],
    #         next_of_kin_phone=patient['next_of_kin_phone'],
    #         next_of_kin_address=patient['next_of_kin_address'],
    #         next_of_kin_gender=patient['next_of_kin_gender'],
    #         perm_address=patient['perm_address'],
    #         city_name=patient['city_name'],
    #         state=patient['state'],
    #         zip_code=patient['zip_code'],
    #         nationality=patient['nationality'],
    #         consultant_id=provider.id,
    #         unit_id=unit.id,
    #         registration='Personal Card',
    #         patient_type='NEW',
    #         marital_status='Single',
    #         religion='Islam',
    #         occupation='Software Engineer',
    #         next_of_kin_relationship='Brother',
    #         next_of_kin_occupation='Software Engineer',
    #     )
    #
    #     new_patient.save_to_db()
    #     print(f"Username {new_patient.first_name} Permanent Address {new_patient.last_name}")

    # for customer in all_customer:
    #     for all_address in data:
    #         address = Address(perm_address=all_address['perm_address'], country=all_address['country'],
    #                           state=all_address['state'],house_number=all_address['house_number'],
    #                           flat_number=all_address['flat_number'],zip_code=all_address['zip_code'],
    #                           username=customer.username)
    #         address.save_to_db()
    #
    #         print(f"Username {customer.username} Permanent Address {address.perm_address}")
    return f'Welcome'


def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001, debug=True)
