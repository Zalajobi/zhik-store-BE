from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.dashboard import dashboard as dashboard_blueprint
from app.model.Provider import ProviderTable
from app.model.Role import RoleTable


@dashboard_blueprint.route('/doctor/data')
@jwt_required()
def get_doctors_dashboard_data():
    username = get_jwt_identity()
    provider = ProviderTable.find_by_username(username)

    return jsonify(
        username=provider.username,
        firstName=provider.first_name,
        lastName=provider.last_name,
        staffId=provider.staff_id,
    )
