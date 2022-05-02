import jsonify as jsonify
from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from model.User import Customer
from model.Address import Address
from utility.constant import BASE_URL
from utility.payload import address_paginate_object_to_json

address_blueprint = Blueprint('address', __name__, url_prefix=f'{BASE_URL}user/address')


@address_blueprint.route('/add', methods=['POST'])
@jwt_required()
def add_address():
    content = request.json
    username = get_jwt_identity()
    address = Address(perm_address=content['permAddress'], country=content['country'], state=content['state'],
                      house_number=content['houseNumber'], zip_code=content['zipCode'],
                      flat_number=content['flatNumber'], username=username)

    address.save_to_db()
    return 'New address added successfully'


@address_blueprint.route('/delete', methods=['DELETE'])
def delete_address():
    try:
        Address.delete_one_by_id(request.json['id'])
        return 'Address Deleted Successfully'
    except:
        return 'Exception occurred while deleting address'


@address_blueprint.route('/get/paginate/<page>', methods=['GET'])
@jwt_required()
def get_user_address_pagination(page):
    username = get_jwt_identity()

    address = Address.query.filter_by(username=username).order_by(Address.id.desc()).paginate(page=int(page), per_page=3, error_out=False)
    return jsonify(
        maxPage=Address.query.filter_by(username=username).count() / 3,
        address=address_paginate_object_to_json(address),
    )