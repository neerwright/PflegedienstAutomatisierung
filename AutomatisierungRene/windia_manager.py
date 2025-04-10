from automation_manager import *
from patient_data_form import Patient
from windia_ids import WindiaWindows
from dataclasses import dataclass, fields
from windia_ids import *
import re
from catalog_data import Catalog
from leistungsnachweis_navigation import *

INSURANCE_K_DROPDOWN_TITLE = "Behandlungspflege   ja / nein"
INSURANCE_P_DROPDOWN_TITLE = "Pflegeversicherung   ja / nein"
PFLICHT_CHECKBOX_TITLE = "nur Pflichtbesuch"
PRAXISEINSATZ_TEXT = "Praxiseinsatz *: allg. ambulante Akut- und Langzeitpflege"

class WindiaManager:
    
    patient_data = None
    catalog_data = None
    
    patient_invoice = None
    autoManager = None
    
    def __init__(self):
        self.autoManager = AutomationManager()
        

    
    def add_new_patient(self):
        
        #click NEW
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 3/9 , 9/10)

        
        #input patient info
        if not self.patient_data:
            raise Exception("set_patient_data() need to be called before a new patient is added")
        
        for field in fields(self.patient_data):
            if field.name == "k_insurance" or field.name == "p_insurance" or  field.name == "insurance_number" or field.name == "anrede":
                continue
            if field.name == "gender":
                self.autoManager.select_gender(getattr(self.patient_data, field.name))
                continue
            
            self.autoManager.input_text(field.name, getattr(self.patient_data, field.name))
            
            
        #----------------Krankenkasse-------------------------#
        self.autoManager.click_inside_window(WindiaWindows.PATIENT,4/9 , 3/13)
        
        
        self.autoManager.select_from_dropdown(PatientAutoID.INSURANCE_DROPDOWN , self.patient_data.k_insurance, INSURANCE_K_DROPDOWN_TITLE)
        self.autoManager.input_text(PatientAutoID.INSURANVE_NUMBER, self.patient_data.insurance_number)
        
        #----------------Pflegekasse-------------------------#
        self.autoManager.click_inside_window(WindiaWindows.PATIENT,4/12 , 3/13)
        self.autoManager.select_from_dropdown(PatientAutoID.INSURANCE_P_DROPDOWN , self.patient_data.p_insurance, INSURANCE_P_DROPDOWN_TITLE)
        self.autoManager.check_pane_tickbox(PFLICHT_CHECKBOX_TITLE)
        
        #----------------Rechnung-------------------------#
        if self.patient_invoice is not None:
            self.autoManager.click_inside_window(WindiaWindows.PATIENT,6/10 , 3/13)
            self._rechnung(self)

        #SAVE
        #self._save_new_patient()
            
            
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
        
    def _save_new_patient(self):
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 4/11 , 9/10)
        self.autoManager.cur_selected_patient = str(getattr(self.patient_data, "name")) + " " + str(getattr(self.patient_data, "surname"))
        print ("cur patient: ") + str(self.autoManager.cur_selected_patient)

    def _edit_patient(self):
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 4/10 , 9/10)

    def select_insurance(self, insurance : str):
        self.autoManager.select_from_dropdown(PatientAutoID.INSURANCE_DROPDOWN , insurance)
    
    def select_docotor(self, doc : str, number : int):
        if int(number) <= 1:
            self.autoManager.select_from_dropdown(PatientAutoID.DOC_DROPDOWN_1 , doc)
        else:
            self.autoManager.select_from_dropdown(PatientAutoID.DOC_DROPDOWN_2 , doc)    
    
    def add_new_degree_of_care(self, deg : int, date : str):
        if not ( 1 <= deg <= 5 ):
            print ("Pflegegrad muss zwischen 1 und 5 sein")
            return
        
        self.autoManager.click_button(PatientAutoID.PG_BUTTON)
        #self.autoManager.set_pg(date, deg)
    
    def test(self):
        pass

        

W = WindiaManager()
#W.autoManager.open_window(WindiaWindows.PATIENT)

W.patient_data = Patient("name", "surname", "15.04.1995", "Frau", "Froschstr", "71126", "Gäufelden", "017522314", "W", "07.04.2025", "", "09.04.2025", "XX", "Universitätsklinikum Tübingen", "AOK BW Sindelfingen P")
#W.add_new_patient()
#W.catalog_data = Catalog("10,75", ["29.04.2024 - 06.09.2024", "21.10.2024 - 29.11.2024"] , ["220,05", "218,7"])
#W.change_gebuerenkatalog()
W.add_new_degree_of_care(2, "12.01.2022")

