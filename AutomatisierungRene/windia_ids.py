from enum import Enum

class WindiaWindows(Enum):
    WINDIA = 0
    LEISTUNGS_NACHWEIS = 1
    PATIENT = 2
    CATALOG = 3
    CARE_DEGREE_HISTORY = 4
    AUSDRUCK_LN = 5

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
    #CLOSE_BTN = 7
    
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
    DOC_ADD_FOLDER = 1001

    REMARKS = 50

    LEISTUNG = 6

    SZ_PANE = 147
    #PG_BUTTON = 38

    PG_HISTORY_TOOLBAR_NEW = -10  #number used for the x offset in the toolbar to click on the button via coordinates
    PG_HISTORY_TOOLBAR_EDIT = -110
    PG_HISTORY_TOOLBAR_SAFE = -110
    PG_HISTORY_TOOLBAR_CLOSE = -290

    #OK_BUTTON = 2
    

class LN_ids(Enum):
    #EINSTELLUNG_BTN = 73
    #LN_PRINT_once = 88
    UNDER_VH_BUTTON_EDIT = 105
    #CANCEL_BTN = 61
    LN_MONTH = 120
    
class Windia_Buttons(Enum):
    LN_CANCEL_BTN = 61 #
    LN_EINSTELLUNG_BTN = 73 # 
    LN_PRINT_ONCE_BTN = 88 # 
    PG_BTN = 38 #
    OK_BUTTON_BTN = 2 #
    RELATIVE_CLOSE_BTN = 7
    SAVE_BUTTON_BTN = 6 #

class DocAutoIds(Enum):
    RIGHT_ARROW_NEXT_TO_NEW = 39 
    TITEL = 22
    SURNAME = 4
    NAME = 26
    TEL = 27
    STREET = 30
    ZIP = 29
    CITY = 31
