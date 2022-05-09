import enum


class RoleNames(enum.Enum):
    ADMIN = 'admin'
    DOCTOR = "doctor"
    NURSE = "nurse"
    RECORD_OFFICER = "record officer"
    PHARMACIST = "pharmacist"
    LABORATORY_TECHNICIAN = "laboratory technician"
    RADIOLOGY_TECHNICIAN = "radiology technician"
    MEDICAL_STORE_MANAGER = "medical store manager"
    CASHIER = "cashier"
    PHYSIOTHERAPIST = "physiotherapist"
    PHLEBOTOMIST = "phlebotomist"
    UNALLOCATED = "unknown"