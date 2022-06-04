from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.dashboard import dashboard as dashboard_blueprint
from app.model.Provider import ProviderTable
from app.model.Role import RoleTable


@dashboard_blueprint.route('/doctor/data')
@jwt_required()
def get_doctors_sidebar_dashboard_data():
    username = get_jwt_identity()
    provider = ProviderTable.find_by_username(username)

    return jsonify(
        username=provider.username,
        firstName=provider.first_name,
        lastName=provider.last_name,
        staffId=provider.staff_id,
    )


@dashboard_blueprint.route('/doctor/get_profile/data')
@jwt_required()
def get_doctors_dashboard_profile_data():
    provider = ProviderTable.find_by_username(get_jwt_identity())

    return jsonify(
        title=provider.title,
        firstName=provider.first_name,
        lastName=provider.last_name,
    )
