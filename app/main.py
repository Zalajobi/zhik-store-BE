from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from email.message import EmailMessage

from app.customers.views.address import address_blueprint
from app.customers.views.customer import user_blueprint
from app.db import db
from app.service.mailTemplates import reset_password_email_template
from app.service.sendMail import sendmail
from app.utility.constant import DATABASE_URL, SECRET_KEY, MAIL_USERNAME, JWT_SECRET_KEY
from app.utility.environ import set_environment_variables

# Models
from app.model.User import Customer
from app.model.Address import Address
from app.utility.libraries import setup_imageKit

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
    return 'Welcome to ZhikStores'


def dump_response(response):
    print("Upload response:")
    for key in sorted(response.keys()):
        print("  %s: %s" % (key, response[key]))


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5001, debug=True)
