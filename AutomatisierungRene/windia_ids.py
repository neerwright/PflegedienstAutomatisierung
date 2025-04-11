from enum import Enum

class WindiaWindows(Enum):
    WINDIA = 0
    LEISTUNGS_NACHWEIS = 1
    PATIENT = 2
    CATALOG = 3
    CARE_DEGREE_HISTORY = 4

class PatientWindowTabs(Enum):
    STAMM = 0
    PFLEGE = 1
    SONSTIGES = 3
    PFLEGEKASSE = 2
    ADRESSEN = 5
    KRANKENKASSE =4
    ANGEHORIGE = 7
    RECHNUNG = 6

class CatalogAutoID(Enum):
    MAIN_DROPDOWN = 52
    PRAXIS_DROPDOWN = 83
    NAME = 82
    PRICE = 80
    NUMBER = 85
    ROW = 67
class RelativesAutoID(Enum):
    NAME = 23
    SURNAME = 22
    TELEPHONE = 18
    CLOSE_BTN = 7
    
class PatientAutoID(Enum):
    NAME = 193
    SURNAME = 192
    BIRTHDAY = 168
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
    INVOICE_NAME_2 = 91
    INVOICE_STREET = 88
    INVOICE_ZIP = 87
    INVOICE_CITY = 86
    
    INSURANCE_DROPDOWN = 138
    INSURANCE_P_DROPDOWN = 39
    DOC_DROPDOWN_1 = 67
    DOC_DROPDOWN_2 = 70

    REMARKS = 50

    LEISTUNG = 6

    PG_BUTTON = 38

    PG_HISTORY_TOOLBAR_NEW = -10  #number used for the x offset in the toolbar to click on the button via coordinates
    PG_HISTORY_TOOLBAR_EDIT = -110
    PG_HISTORY_TOOLBAR_SAFE = -110
    PG_HISTORY_TOOLBAR_CLOSE = -290

