import json

from flask import Flask, send_from_directory, jsonify
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import cloudinary
from cloudinary.uploader import upload
from imagekitio import ImageKit
import os

from customers.views.address import address_blueprint
from customers.views.customer import user_blueprint
from db import db
from utility.constant import DATABASE_URL, SECRET_KEY
from utility.environ import set_environment_variables

# Models
from model.User import Customer
from model.Address import Address
from model.Socials import Socials
from model.Product import Product, ProductImages

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
set_environment_variables()


# cloudinary.config(cloud_name='zalajobi', api_key='419976814271589', api_secret='tSbI9om-kAb9aqd-Xa4hejtCSaE')
cloudinary.config(cloud_name=os.getenv('CLOUDINARY_NAME'), api_key=os.getenv('CLOUDINARY_KEY'), api_secret=os.getenv('SECRET_KEY'))
imagekit = ImageKit(private_key=os.getenv('IMAGEKIT_PRIVATE_KEY'), public_key=os.getenv('IMAGEKIT_PUBLIC_KEY'), url_endpoint=os.getenv('IMAGEKIT_URL_ENDPOINT'))


@app.route('/', methods=['GET'])
def upload_file():
    # image = send_from_directory('static', 'image/default_profile_pic.jpeg')

    # imagekit_url = imagekit.upload(
    #     file=open('static/image/default_profile_pic.jpeg', "rb"),
    #     file_name="profile_pic.jpg",
    #     options={
    #         "response_fields": ["is_private_file", "tags"],
    #         "tags": ["profile_pic", "username"]
    #     },
    # )

    # open_json = open('static/data/json/address_data.json')
    # data = json.load(open_json)
    #
    # all_customer = Customer.get_all_customers()
    #
    # for customer in all_customer:
    #     for all_address in data:
    #         address = Address(perm_address=all_address['perm_address'], country=all_address['country'],
    #                           state=all_address['state'],house_number=all_address['house_number'],
    #                           flat_number=all_address['flat_number'],zip_code=all_address['zip_code'],
    #                           username=customer.username)
    #         address.save_to_db()
    #
    #         print(f"Username {customer.username} Permanent Address {address.perm_address}")


    # return jsonify(imagekit_url)
    return 'Welcome to ZhikStores'


def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001, debug=True)
