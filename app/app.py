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
