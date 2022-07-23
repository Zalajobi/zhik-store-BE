import datetime

from flask import session, request, make_response
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, get_jwt
from sqlalchemy import or_

from app.auth import auth as auth_blueprint
from app.model.Provider import ProviderTable
from app.db import db as database
from app.model.Role import RoleTable


@auth_blueprint.route('/test_jwt')
@jwt_required()
def test():
    jwt_content = get_jwt()
    jwt_identity = get_jwt_identity()
    return jwt_content
    # return session.get("active_role")


@auth_blueprint.route('/login', methods=['POST'])
def post():
    error_response = make_response('Invalid Username or Password')
    error_response.status_code = 401

    content = request.json
    print(f"Content {content}")
    provider = ProviderTable.find_by_username(content['username']) or \
        ProviderTable.find_by_email(content['username'])

    if provider is None:
        return error_response
    elif check_password_hash(provider.password, content['password']):
        role = database.session.query(RoleTable).filter_by(id=provider.role_id).first()
        additional_jwt_data = {"active_role_id": role.id, "active_role_name": role.name}
        success_response = make_response({"token": create_access_token(
            identity=provider.username, expires_delta=datetime.timedelta(hours=6, minutes=30),
            additional_claims=additional_jwt_data)})
        session["active_role"] = role.name
        success_response.status_code = 200
        return success_response

    return error_response


@auth_blueprint.route('/get_provider_role', methods=['GET'])
@jwt_required()
def provider_role():
    return f"{get_jwt()['active_role_name']}"
