from dataclasses import dataclass
from enum import Enum
from windia_ids import PatientAutoID

@dataclass
class Patient:
    """Class for keeping track of Patient data"""
    name: str
    surname: str
    gender: str
    birthday: str
    anrede: str
    street: str
    zip: str
    city: str
    telephone: str
     
    care_beginning_date: str
    care_end_date: str
    admission_date : str
    
@dataclass
class PatientInsuranceInfo():
    insurance_number : str
    k_insurance: str
    p_insurance: str
    care_degree : int
    degree_since_date : str
    doc1 : str
    doc2 : str
    relative1 : list # [name, surname, tel]
    misc : str
    pflicht_leistung : bool
    
def get_enum_from_field(name):
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
            case "ZIP":
                return PatientAutoID.ZIP
            case "CITY":
                return PatientAutoID.CITY
            case "TELEPHONE":
                return PatientAutoID.TELEPHONE
            case "CARE_BEGINNING_DATE":
                return PatientAutoID.BEGINNING_DATE
            case "CARE_END_DATE":
                return PatientAutoID.END_DATE
            case "ADMISSION_DATE":
                return PatientAutoID.ADMISSION_DATE
            case "GENDER":
                return PatientAutoID.GENDER
            
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

    

@dataclass
class Invoice:
    """Class for keeping track of Patine/School invoice data"""
    invoice_anrede :str
    invoice_name_1 : str
    invoice_name_2 : str
    invoice_street : str
    invoice_zip : str
    invoice_city : str
    

            
    


    