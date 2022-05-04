import datetime
import os
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from imagekitio import ImageKit

from model.User import Customer
from model.Address import Address
from utility.constant import BASE_URL, DEFAULT_PROFILE_IMG
from utility.payload import address_object_to_json
from db import db

# from app import imagekit

user_blueprint = Blueprint('authentication', __name__, url_prefix=f"{BASE_URL}user")


@user_blueprint.route('/login', methods=['POST'])
def login():
    content = request.json

    current_customer = Customer.find_by_username(content['username']) or \
                       Customer.find_by_email(content['username'])

    if current_customer is None:
        return 'Invalid Username or Email, Please check credentials'
    elif check_password_hash(current_customer.password, content['password']):
        return jsonify(access_token=create_access_token(identity=current_customer.username,
                                                        expires_delta=datetime.timedelta(hours=6, minutes=30)))


@user_blueprint.route('/signup', methods=['POST'])
def signup():
    content = request.json
    current_customer = Customer.find_by_username(content['username']) or \
                       Customer.find_by_email(content['username'])

    if current_customer is not None:
        return f"User with {content['username']} or {content['email']} already exists, Try Again..."
    else:
        customer = Customer(username=content['username'], title=content['title'], email=content['email'],
                            phone=str(content['phone']), first_name=content['first_name'], dob=content['dob'],
                            last_name=content['last_name'], middle_name=content['middle_name'],
                            gender=content['gender'], password=content['password'],
                            profile_image_url=DEFAULT_PROFILE_IMG)
        customer.save_to_db()
        return 'Signup Successful'


@user_blueprint.route('/profile/view', methods=['GET'])
@jwt_required()
def get_user_profile():
    username = get_jwt_identity()
    customer = Customer.find_by_username(username)
    customer_addresses = Address.find_all_by_username(username)
    return jsonify(
        title=customer.title,
        username=customer.username,
        email=customer.email,
        firstName=customer.first_name,
        lastName=customer.last_name,
        middleName=customer.middle_name,
        dateOfBirth=customer.dob,
        gender=customer.gender,
        phoneNumber=customer.phone,
        profilePicture=customer.profile_image_url,
        addresses=address_object_to_json(customer_addresses),
    )


@user_blueprint.route('/profile/picture/upload', methods=['POST'])
@jwt_required()
def upload_profile_picture():
    username = get_jwt_identity()
    image_file = request.files['image']
    imagekit = ImageKit(private_key=os.getenv('IMAGEKIT_PRIVATE_KEY'), public_key=os.getenv('IMAGEKIT_PUBLIC_KEY'),
                        url_endpoint=os.getenv('IMAGEKIT_URL_ENDPOINT'))

    customer = Customer.find_by_username(username)

    try:
        imagekit_url = imagekit.upload(
            file=image_file,
            file_name="profile_pic.jpg",
            options={
                "response_fields": ["is_private_file", "tags"],
                "tags": ["profile_pic", "username"]
            },
        )
        customer.profile_image_url = imagekit_url['response']['url']
        db.session.commit()
        return "Image upload Successful"
    except:
        print('Image Upload Failed')

    return "Image Upload Failed"


@user_blueprint.route('/hello', methods=['GET'])
def hello():
    return "HELLO WORLD"
