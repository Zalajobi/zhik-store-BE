import datetime

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from utility.constant import BASE_URL
from model.User import Customer
from model.Address import Address
from utility.payload import address_object_to_json
from db import db

user_blueprint = Blueprint('authentication', __name__, url_prefix=f'{BASE_URL}user')


@user_blueprint.route('/login', methods=['POST'])
def login():
    current_customer = Customer.find_by_username(request.form['username']) or \
                       Customer.find_by_email(request.form['username'])
    if current_customer is None:
        return 'Invalid Username or Email, Please check credentials'
    elif check_password_hash(current_customer.password, request.form['password']):
        return jsonify(access_token=create_access_token(identity=current_customer.username,
                                                        expires_delta=datetime.timedelta(hours=6, minutes=30)))


@user_blueprint.route('/signup', methods=['POST'])
def signup():
    current_customer = Customer.find_by_username(request.form['username']) or \
                       Customer.find_by_email(request.form['username'])
    if current_customer is not None:
        return f"User with {request.form['username']} or {request.form['email']} already exists, Try Again..."
    else:
        hashed_passwd = generate_password_hash(request.form['password'])

        customer = Customer(username=request.form['username'], title=request.form['title'], email=request.form['email'],
                            phone=request.form['phone'], first_name=request.form['first_name'], last_name=request.form['last_name'],
                            middle_name=request.form['middle_name'], gender=request.form['gender'], password=hashed_passwd)
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
        addresses=address_object_to_json(customer_addresses),
    )


@user_blueprint.route('/address/add', methods=['POST'])
@jwt_required()
def add_address():
    username = get_jwt_identity()
    address = Address(perm_address=request.form['address'], country=request.form['country'], state=request.form['state'],
                      house_number=request.form['house_number'], zip_code=request.form['zip_code'],
                      flat_number=request.form['flat_number'], username=username)

    address.save_to_db()
    return 'New address added successfully'


@user_blueprint.route('/hello', methods=['GET'])
def hello():
    return "HELLO WORLD"
