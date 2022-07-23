from datetime import datetime
from dateutil.relativedelta import relativedelta
from app.model.Unit import UnitTable
from app.db import db as database


def paginate_doctor_primary_patient_object_to_json(paginate_obj, consultant):

    patient_item = []
    for patient in paginate_obj.items:
        unit = database.session.query(UnitTable).filter(UnitTable.id == patient.unit_id).first()

        patient_item.append({
            "id": patient.id,
            "name": f"{patient.title} {patient.first_name} {patient.last_name}",
            "age": relativedelta(datetime.today(), patient.dob).years,
            "lastSeen": datetime.today().strftime('%Y-%m-%d'),
            "consultant": consultant,
            "unit": unit.name,
            "status": patient.status,
            "gender": patient.gender,
        })

    return patient_item
