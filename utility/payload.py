def address_object_to_json(customer_address):
    user_address = []
    for address in customer_address:
        user_address.append({
            "id": address.id,
            "permAddress": address.perm_address,
            "country": address.country,
            "state": address.state,
            "houseNumber": address.house_number,
            "flatNumber": address.flat_number,
            "zipCode": address.zip_code
        })
    return user_address


def address_paginate_object_to_json(address_item):
    user_address = []
    for address in address_item.items:
        user_address.append({
            "id": address.id,
            "permAddress": address.perm_address,
            "country": address.country,
            "state": address.state,
            "houseNumber": address.house_number,
            "flatNumber": address.flat_number,
            "zipCode": address.zip_code
        })

    return user_address
