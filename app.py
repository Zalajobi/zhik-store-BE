from flask import Flask, send_from_directory
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import json

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
    # open_json = open('utility/zalajobi.json')
    # data = json.load(open_json)
    # image = send_from_directory('static', 'image/default_profile_pic.jpeg')
    # image_url = 'https://ik.imagekit.io/zalajobi/zhik-store/default_profile_pic_y4-z9eBo7.jpeg?ik-sdk-version=javascript-1.4.3&updatedAt=1651485516772'

    # for all_address in data:
    #     address = Address(perm_address=all_address['perm_address'], country=all_address['country'], state=all_address['state'],
    #                       house_number=all_address['house_number'], flat_number=all_address['flat_number'],
    #                       zip_code=all_address['zip_code'], username='zalajobi')
    #     address.save_to_db()
    return 'Welcome to ZhikStores'


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001, debug=True)
