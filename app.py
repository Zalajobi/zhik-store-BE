from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from customers.views.address import address_blueprint
from customers.views.customer import user_blueprint
from db import db
from utility.constant import DATABASE_URL, SECRET_KEY
from model.User import Customer
from model.Address import Address

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = SECRET_KEY

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
CORS(app)


@app.before_first_request
def create_tables():
    db.create_all()


# Blueprints
app.register_blueprint(user_blueprint)
app.register_blueprint(address_blueprint)


@app.route('/')
def intro():
    # address = Address(username="zalajobi", perm_address="47, Aderibigbe Street", country="Nigeria", state="Lagos",
    #                   house_number="47", flat_number="3", zip_code="101241")
    # address.save_to_db()
    return 'Welcome to ZhikStores'


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001, debug=True)
