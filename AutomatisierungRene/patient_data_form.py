from dataclasses import dataclass
from enum import Enum
from windia_enums import PatientAutoID

@dataclass
class Patient:
    """Class for keeping track of Patient data"""
    name: str
    surname: str
    birthday: str
    anrede: str
    street: str
    zip: str
    city: str
    telephone: str
    gender: str 
    care_beginning_date: str
    care_end_date: str
    admission_date : str
    insurance_number : str
    k_insurance: str
    p_insurance: str
 
    
    def get_enum_from_field(self, name):
        upper = name.upper()
        match upper:
            case "NAME":
                return PatientAutoID.NAME
            case "SURNAME":
                return PatientAutoID.SURNAME
            case "BIRTHDAY":
                return PatientAutoID.BIRTHDAY
            case "ANREDE":
                return PatientAutoID.ANREDE
            case "STREET":
                return PatientAutoID.STREET
            case "STREET":
                return PatientAutoID.STREET
            case "ZIP":
                return PatientAutoID.ZIP
            case "CITY":
                return PatientAutoID.CITY
            case "TELEPHONE":
                return PatientAutoID.TELEPHONE
            case "BEGINNING_DATE":
                return PatientAutoID.BEGINNING_DATE
            case "END_DATE":
                return PatientAutoID.END_DATE
            case "ADMISSION_DATE":
                return PatientAutoID.ADMISSION_DATE
            case "ADMISSION_DATE":
                return PatientAutoID.ADMISSION_DATE

@dataclass
class Invoice:
    """Class for keeping track of Patine/School invoice data"""
    anrede :str
    name_1 : str
    name_2 : str #second line in invoice letter
    street : str
    zip : str
    city : str
    
    def get_enum_from_field(self, name : str):
        upper = "INVOICE_" + name.upper()
        match upper:
            case "INVOICE_ANREDE":
                return PatientAutoID.INVOICE_ANREDE
            case "INVOICE_NAME_1":
                return PatientAutoID.INVOICE_NAME_1
            case "INVOICE_NAME_2":
                return PatientAutoID.INVOICE_NAME_2
            case "INVOICE_STREET":
                return PatientAutoID.INVOICE_STREET
            case "INVOICE_ZIP":
                return PatientAutoID.INVOICE_ZIP
            case "INVOICE_CITY":
                return PatientAutoID.INVOICE_CITY
    


    