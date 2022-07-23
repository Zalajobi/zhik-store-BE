from flask import jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.dashboard import dashboard as dashboard_blueprint
from app.model.Provider import ProviderTable
from app.model.Patient import PatientTable
from app.model.Role import RoleTable
from app.db import db as database
from app.dashboard.util import paginate_doctor_primary_patient_object_to_json


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
    patient_count = database.session.query(PatientTable).filter(PatientTable.consultant_id == provider.id).count()
    # patient_consultant = database.session.query(PatientTable).filter(PatientTable.consultant_id == provider.id)\
    #     .paginate(patient)

    return jsonify(
        title=provider.title,
        firstName=provider.first_name,
        lastName=provider.last_name,
        patientsCount=patient_count
    )


@dashboard_blueprint.route('/doctor/primary-patient/paginate/<per_page>/<page>')
@jwt_required()
def get_paginated_primary_patient_data(per_page, page):
    provider = ProviderTable.find_by_username(get_jwt_identity())
    patient_consultant = database.session.query(PatientTable).filter(PatientTable.consultant_id == provider.id)\
        .order_by(PatientTable.first_name)\
        .paginate(page=int(page) + 1, per_page=int(per_page), error_out=False)

    return jsonify(
        primaryPatient=paginate_doctor_primary_patient_object_to_json(patient_consultant, "{0} {1} {2}".format(
            provider.title, provider.first_name, provider.last_name
        ))
    )
