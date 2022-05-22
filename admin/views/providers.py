from flask import jsonify, request

from db import db as database

from admin import admin as admin_blueprint
from model.Departments import DepartmentTable
from model.Provider import ProviderTable
from model.Role import RoleTable
from model.Unit import UnitTable
from admin.utils import generate_random_password
from model.enum_static import ProviderRoles


@admin_blueprint.route('/provider/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        roles = []
        units = []
        departments = []

        provider_roles = database.session.query(RoleTable).filter(RoleTable.name != ProviderRoles.ADMIN.value).order_by(RoleTable.name.asc()).all()
        unit_table = database.session.query(UnitTable).order_by(UnitTable.name.asc()).all()
        department_table = database.session.query(DepartmentTable).order_by(DepartmentTable.name.asc()).all()

        for role in provider_roles:
            roles.append(role.name)

        for unit in unit_table:
            units.append(unit.name)

        for department in department_table:
            departments.append(department.name)

        return jsonify(
            roles=roles,
            units=units,
            departments=departments,
            randomPassword=generate_random_password(10)
        )
    else:
        try:
            content = request.json
            role = database.session.query(RoleTable.id).filter_by(name=content['role']).first()
            unit = database.session.query(UnitTable.id).filter_by(name=content['unit']).first()
            department = database.session.query(DepartmentTable.id).filter_by(name=content['department']).first()

            new_provider = ProviderTable(
                email=content['email'],
                phone_number=content['phone'],
                username=content['username'],
                first_name=content['firstname'],
                middle_name=content['middlename'],
                last_name=content['lastname'],
                dob=str(content['birthday']),
                gender=content['gender'],
                title=content['title'],
                staff_id=content['staffId'],
                street_address=content['address'],
                city=content['city'],
                state=content['state'],
                country=content['country'],
                zipcode=int(content['zipcode']),
                department_id=department.id,
                unit_id=unit.id,
                role_id=role.id,
                password=generate_random_password(8)
            )
            new_provider.save_to_db()

            return 'Successful'
        except Exception as e:
            return f"Provider with StaffID, Email, or Username already exists"


@admin_blueprint.route('/')
def test():
    return 'Admin Route'
