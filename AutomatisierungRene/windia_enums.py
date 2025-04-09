from enum import Enum

class WindiaWindows(Enum):
    WINDIA = 0
    LEISTUNGS_NACHWEIS = 1
    PATIENT = 2
    CATALOG = 3


class CatalogAutoID(Enum):
    MAIN_DROPDOWN = 52
    PRAXIS_DROPDOWN = 83
    NAME = 82
    PRICE = 80
    NUMBER = 85
    ROW = 67
    
    
class PatientAutoID(Enum):
    NAME = 193
    SURNAME = 192
    BIRTHDAY = 165
    ANREDE = 150
    STREET = 157
    ZIP = 158
    CITY = 156
    TELEPHONE = 151
    BEGINNING_DATE = 166
    END_DATE = 167
    ADMISSION_DATE = 165
    INSURANVE_NUMBER = 137
    
    GENDER = -1
    INVOICE_ANREDE = 92
    INVOICE_NAME_1 = 89
    INVOICE_NAME_2 = 81
    INVOICE_STREET = 88
    INVOICE_ZIP = 87
    INVOICE_CITY = 86
    
    INSURANCE_DROPDOWN = 138
    INSURANCE_P_DROPDOWN = 39