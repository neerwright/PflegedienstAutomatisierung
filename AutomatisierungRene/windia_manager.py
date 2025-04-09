from automation_manager import *
from patient_data_form import Patient
from windia_enums import WindiaWindows
from dataclasses import dataclass, fields
from windia_enums import *
import re
from catalog_data import Catalog
from leistungsnachweis_navigation import *

INSURANCE_DROPDOWN_TITLE = "Behandlungspflege   ja / nein"
PRAXISEINSATZ_TEXT = "Praxiseinsatz *: allg. ambulante Akut- und Langzeitpflege"

class WindiaManager:
    
    patient_data = None
    catalog_data = None
    
    patient_invoice = None
    autoManager = None
    
    def __init__(self):
        self.autoManager = AutomationManager()
        #self.patient_data = Patient()
        #self.catalog_data = Catalog()
        
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
        
    def set_catalog_data(self, catalog_wage, dates, hours):
        self.catalog_data.catalog_wage = catalog_wage
        self.catalog_data.dates = dates
        self.catalog_data.hours = hours
        
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

        return
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
        self.autoManager.select_from_dropdown(PatientAutoID.INSURANCE_DROPDOWN , self.patient_data.k_insurance, INSURANCE_DROPDOWN_TITLE)
        self.autoManager.input_text(self.patient_data.insurance_number.name, self.patient_data.insurance_number)
        
    
        #----------------Rechnung-------------------------#
        if self.patient_invoice is not None:
            self.autoManager.click_inside_window(WindiaWindows.PATIENT,6/10 , 3/13)
            self._rechnung(self)
            
            
    def _rechnung(self):
        
        for field in fields(self.patient_invoice):
            self.autoManager.input_text(field.name, getattr(self.patient_invoice, field.name))
            
            
    def  change_gebuerenkatalog(self):
        #select catalog
        self.autoManager.select_from_dropdown( CatalogAutoID.MAIN_DROPDOWN , "Selbstzahler")
        #select Praxiseinsatz 1 and then 2
        for i in range(1,5):
            praxiseinsatz_index = "1"
            if (i == 3):
                praxiseinsatz_index =  "2"
            if (i%2) == 1:    
                self.autoManager.select_from_dropdown( CatalogAutoID.PRAXIS_DROPDOWN , f"Praxiseinsatz {praxiseinsatz_index}")
            else:
                self.autoManager.select_from_dropdown( CatalogAutoID.PRAXIS_DROPDOWN , f"{i}-{i}")
            

            #Change Name, Price and Number
            self.autoManager.click_inside_window(WindiaWindows.CATALOG,5/9 , 9/10 ) #Ändern btn
            
            if(i%2 == 1):
                self.autoManager.input_text(CatalogAutoID.PRICE, self.catalog_data.catalog_wage)
                txt = re.sub('[*]', praxiseinsatz_index, PRAXISEINSATZ_TEXT) 
                self.autoManager.input_text(CatalogAutoID.NAME, txt)
            else:
                if not self.catalog_data:
                    raise Exception("set_catalog_data() need to be called before the catalog can be changed!")
                    
                txt = f"{self.catalog_data.dates[(i%3) % 2]}, {self.catalog_data.hours[(i%3) % 2]} h"
                self.autoManager.input_text(CatalogAutoID.NAME, txt)

            self.autoManager.input_text(CatalogAutoID.NUMBER, str(i))
            self.autoManager.input_text(CatalogAutoID.ROW, str(i))

            self.autoManager.click_inside_window(WindiaWindows.CATALOG, 5/9 , 9/10) #Save btn   
            self.autoManager._click_popup_window_away("7")

        
            
    def issue_an_invoice(self):
        #open_patient_window -> add new patient
        self.autoManager.open_window(WindiaWindows.PATIENT)
        self.add_new_patient()
        
        #close window -> open and change Geürenkathalog
        self.autoManager.close_window()    
        self.autoManager.open_window(WindiaWindows.CATALOG)
        self.change_gebuerenkatalog()
        
        self.autoManager.close_window()    
        self.autoManager.open_window(WindiaWindows.LEISTUNGS_NACHWEIS)
        input_hours_for_bill()
        
        

W = WindiaManager()
#W.autoManager.open_window(WindiaWindows.PATIENT)

W.patient_data = Patient("name", "surname", "15.04.1995", "Frau", "Froschstr", "71126", "Gäufelden", "017522314", "W", "07.04.2025", "", "09.04.2025", "XX", "Alianz", "Alianz P")
#W.set_patient_data("name", "surname", "15.04.1995", "Frau", "Froschstr", "71126", "Gäufelden", "017522314", "W", "07.04.2025", "", "09.04.2025")
W.add_new_patient()



