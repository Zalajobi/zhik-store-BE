import datetime

from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from email.message import EmailMessage
from werkzeug.security import generate_password_hash

from model.User import Customer
from model.Address import Address
from service.mailTemplates import reset_password_email_template
from service.sendMail import sendmail
from utility.constant import BASE_URL, DEFAULT_PROFILE_IMG, MAIL_PASSWORD, MAIL_USERNAME
from utility.libraries import setup_imageKit
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

    return "Invalid Username/Email or Password, Please check credentials"


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
    imagekit = setup_imageKit()

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


@user_blueprint.route('/password/reset', methods=['POST'])
def reset_password():
    msg = EmailMessage()
    email = request.json['email']
    reset_password_account = Customer.find_by_email(email)
    if reset_password_account is not None:
        password_reset_token = create_access_token(identity=email,
                                                   expires_delta=datetime.timedelta(hours=6, minutes=30))
        msg['Subject'] = 'Reset Password'
        msg['FROM'] = 'zhikrullah.ranti@gmail.com'
        msg['To'] = email
        msg.set_content(reset_password_email_template(f'http://localhost:3000/user/edit/password?token={password_reset_token}'), subtype='html')
        sendmail(msg)
        return jsonify(resetToken=password_reset_token)
    return f"No user with {email}"


@user_blueprint.route('/password/reset/email_reset', methods=['POST'])
@jwt_required()
def reset_password_via_email():
    email = get_jwt_identity()
    password = request.json['password']

    try:
        reset_password_account = Customer.find_by_email(email)
        reset_password_account.password = generate_password_hash(password)
        db.session.commit()
        return 'Password reset successful'
    except:
        return 'Encountered error while updating password'


@user_blueprint.route('/hello', methods=['GET'])
def hello():
    return "HELLO WORLD"
