from automation_manager import *
from patient_data_form import Patient
from windia_enums import WindiaWindows
from dataclasses import dataclass, fields


INSURANCE_DROPDOWN_TITLE = "Behandlungspflege   ja / nein"
INSURANCE_DROPDOWN_ID = "138"

class WindiaManager:
    
    patient_data = None
    patient_invoice = None
    autoManager = None
    
    def __init__(self):
        self.autoManager = AutomationManager()
        patient_data = Patient()
        
    def set_patient_data(self, name, surname, birthday, anrede, street, zip, city, telephone, gender, care_beginning_date, care_end_date, admission_date ):
        self.patient_data.name = name
        self.patient_data.surname = surname
        self.patient_dat.birthday = birthday
        self.patient_data.anrede = anrede
        self.patient_data.street = street
        self.patient_data.zip = zip
        self.patient_data.city = city
        self.patient_data.telephone = telephone
        self.patient_data.gender = gender
        self.patient_data.care_beginning_date = care_beginning_date
        self.patient_data.care_end_date = care_end_date
        self.patient_data.admission_date = admission_date
        
    def set_invoice_data(self, anrede, name_line1, name_line2, street, zip, city):
        self.patient_invoice.anrede = anrede
        self.patient_invoice.name_2 = name_line1
        self.patient_invoice.name_1 = name_line2
        self.patient_invoice.street = street
        self.patient_invoice.zip = zip
        self.patient_invoice.city = city

    
    def add_new_patient(self):
        #click NEW
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 3/9 , 9/10)
        
        #input patient info
        if not self.patient_data:
            raise Exception("set_patient_data() need to be called before a new patient is added")
        
        for field in fields(self.patient_data):
            if field.name == "k_insurance" or field.name == "p_insurance" or  field.name == "insurance_number":
                continue
            if field.name == "gender":
                self.autoManager.click_middle_of_field(field.name)
                continue
            
            self.autoManager.input_text(field.name, getattr(self.patient_data, field.name))
            
            
        #----------------Krankenkasse-------------------------#
        self.autoManager.click_inside_window(WindiaWindows.PATIENT,4/9 , 3/13)
        self.autoManager.select_from_dropdown( INSURANCE_DROPDOWN_TITLE , INSURANCE_DROPDOWN_ID , self.patient_data.k_insurance)
        self.autoManager.input_text(self.patient_data.insurance_number.name, self.patient_data.insurance_number)
        
    
        #----------------Rechnung-------------------------#
        if self.patient_invoice is not None:
            self.autoManager.click_inside_window(WindiaWindows.PATIENT,6/10 , 3/13)
            self._rechnung(self)
            
            
    def _rechnung(self):
        
        for field in fields(self.patient_invoice):
            self.autoManager.input_text(field.name, getattr(self.patient_invoice, field.name))
                
            
            
            
        