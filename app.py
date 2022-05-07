from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from email.message import EmailMessage

from customers.views.address import address_blueprint
from customers.views.customer import user_blueprint
from db import db
from service.mailTemplates import reset_password_email_template
from service.sendMail import sendmail
from utility.constant import DATABASE_URL, SECRET_KEY, MAIL_USERNAME, MAIL_PASSWORD, JWT_SECRET_KEY
from utility.environ import set_environment_variables

# Models
from model.User import Customer
from model.Address import Address
from model.Socials import Socials
from model.Product import Product, ProductImages
from utility.libraries import setup_imageKit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = SECRET_KEY
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

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

# Third Party Libraries
setup_imageKit()


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

    # open_json = open('static/data/json/product.json')
    # data = json.load(open_json)
    #
    # for product in data:
    #     new_product = Product(seller_username='zalajobi', name=product['name'], categories=product['categories'],
    #                           price=product['price'], discount=product['discount'], dimension='200*200',
    #                           description=product['description'], weight=product['weight'],
    #                           short_description=product['short_description'])
    #
    #     new_product.save_to_db()
    #
    #     print(f"Product Name {new_product.name} Price{new_product.price}")
    # msg = Message('mail title', sender='igbalajobi.shikruiiahr@student.funaab.edu.ng', recipients=['zalajobi@gmail.com'])
    # msg.body = 'Body of the email to send'
    # mail.send(msg)

    # Send Email Works
    # smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # smtp_server.ehlo()
    # smtp_server.login('zhikrullah.ranti@gmail.com', 'nqisvjygyhtspqvh')
    # smtp_server.sendmail('zhikrullah.ranti@gmail.com', 'zalajobi@gmail.com', 'Mail Sent from ZhikStore')

    msg = EmailMessage()

    msg['Subject'] = 'Reset Password'
    msg['FROM'] = 'zhikrullah.ranti@gmail.com'
    msg['To'] = 'zalajobi@gmail.com'
    msg.set_content(reset_password_email_template('http://localhost:3000/login'), subtype='html')
    sendmail(msg)
    return 'Mail Sent...'

    # return 'Welcome to ZhikStores'


def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001, debug=True)
