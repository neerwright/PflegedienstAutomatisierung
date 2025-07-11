from automation_manager import *
from patient_data_form import Patient, PatientInsuranceInfo, Invoice
from windia_ids import WindiaWindows
from dataclasses import dataclass, fields
from windia_ids import *
import re
from catalog_data import Catalog
from leistungsnachweis_navigation import *
from findDocSelenium import findDocSelenium
import pygame
from local_db import localDataManager

INSURANCE_K_DROPDOWN_TITLE = "Behandlungspflege   ja / nein"
INSURANCE_P_DROPDOWN_TITLE = "Pflegeversicherung   ja / nein"
PFLICHT_CHECKBOX_TITLE = "nur Pflichtbesuch"
PRAXISEINSATZ_TEXT = "Praxiseinsatz *: allg. ambulante Akut- und Langzeitpflege"


class WindiaManager:
    
    patient_data = None
    patient_insurance_data = None
    catalog_data = None
    switched = False
    patient_invoice = None
    autoManager = None
    docSelenium = None
    data_manager = None

    def __init__(self, dm : localDataManager):
        self.autoManager = AutomationManager()
        
        self.data_manager = dm

    def input_stamm(self):
        if not self.patient_data or not self.patient_insurance_data:
            raise Exception("patient_data needs to be filled before a new patient is added")
        
        for field in fields(self.patient_data):
            if field.name == "anrede" :
                continue
            if field.name == "gender":
                self.autoManager.select_gender(getattr(self.patient_data, field.name))
                continue
            
            self.autoManager.input_text(field.name, getattr(self.patient_data, field.name))
         
    def input_insurance(self, i_dropdown : PatientAutoID, insurance : str, dropdown_title : str, insurance_number = None):
        
        
        self.autoManager.select_from_dropdown(i_dropdown , insurance, dropdown_title)
        if insurance_number:
            self.autoManager.input_text(PatientAutoID.INSURANVE_NUMBER, insurance_number)

    def input_insurance_p(self):
        self.input_insurance( i_dropdown=PatientAutoID.INSURANCE_P_DROPDOWN  ,insurance=self.data_manager.get_insurances().get(self.patient_insurance_data.k_insurance) , dropdown_title= INSURANCE_P_DROPDOWN_TITLE )
        if self.patient_insurance_data.pflicht_leistung:
            self.autoManager.check_pane_tickbox(PFLICHT_CHECKBOX_TITLE)
        #-- save and edit to change degree of care
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 5/12 , 9/10)
        time.sleep(1)
        self.autoManager._click_popup_window_away("6", "WinDIA-Meldung") # soll ort übernommen werden - ja button
        time.sleep(0.1)
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 4/9 , 9/10)
        time.sleep(0.2)
        self.input_degree_of_care(self.patient_insurance_data.care_degree, self.patient_insurance_data.degree_since_date)

    def insert_invoice_data(self, insurance_str : str):
        if insurance_str == "Universitätsklinikum Tübingen":
            self.patient_invoice = Invoice("An das", "Universitätsklinikum Tübingen", "Stabstelle KV4 Pflegedirektion, Fr.Zahn",  "Hoppe-Seyer-Str.6", "72076", "Tübingen")
            self.patient_data.street = "Hoppe-Seyer-Str.6"
            self.patient_data.zip = "72076"
            self.patient_data.city = "Tübingen"

    def add_new_patient(self, new_doc = None):
        
        if new_doc:
            print("new doc!! " + str(new_doc))
            self.docSelenium = findDocSelenium()
            self.docSelenium.find_doc_on_search_results_page(new_doc[0], new_doc[1])
            doc_street, doc_zip_code, doc_city, doc_tel = self.docSelenium.get_doc_data()
            

        if not self.autoManager.get_and_wait_for_window(WindiaWindows.PATIENT, 3):
            self.autoManager.open_window(WindiaWindows.PATIENT)
        
        
        #click NEW
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 3/9 , 9/10)

        #input patient info
        if self.patient_invoice is not None:
            self.check_SZ()
        self.input_stamm()   
        
        #----------------Krankenkasse-------------------------#
        self.switch_patient_tab(PatientWindowTabs.KRANKENKASSE)
        time.sleep(0.5)
        self.input_insurance( PatientAutoID.INSURANCE_DROPDOWN , self.patient_insurance_data.k_insurance,  INSURANCE_K_DROPDOWN_TITLE , self.patient_insurance_data.insurance_number)
        
        #----------------Rechnung-------------------------##
        if self.patient_invoice is not None:
            self.switch_patient_tab(PatientWindowTabs.RECHNUNG)
            self.autoManager.click_inside_window(WindiaWindows.PATIENT,6/10 , 3/13)
            self._rechnung()
            #self.autoManager._click_popup_window_away("2")
            self._save_new_patient() #save patient/student
            return

        #----------------Pflegekasse-------------------------#
        self.switch_patient_tab(PatientWindowTabs.PFLEGEKASSE)
        self.input_insurance_p()
        

        #------Sonstige tab REMARKS---------------------
        self.switch_patient_tab(PatientWindowTabs.SONSTIGES)
        self.autoManager.input_text(PatientAutoID.REMARKS, self.patient_insurance_data.misc)
        
        #------Angehörige----------
        self.switch_patient_tab(PatientWindowTabs.ANGEHORIGE)
        # click New inside tab
        self.autoManager.click_inside_window(WindiaWindows.PATIENT,1/15 , 10/13)
        if len(self.patient_insurance_data.relative1) >= 1:
            self.autoManager.input_text(RelativesAutoID.NAME, self.patient_insurance_data.relative1[0])
        if len(self.patient_insurance_data.relative1) >= 2:
            self.autoManager.input_text(RelativesAutoID.SURNAME, self.patient_insurance_data.relative1[1])
        if len(self.patient_insurance_data.relative1) >= 3:
            self.autoManager.input_text(RelativesAutoID.TELEPHONE, self.patient_insurance_data.relative1[2])
        #close relative window
        self.autoManager.close_window()
        time.sleep(3)

        #-----PFLEGE--------
        self.switch_patient_tab(PatientWindowTabs.PFLEGE)
        if new_doc:
            self.add_new_doctor(self.docSelenium.surname, self.docSelenium.name, doc_street, doc_zip_code, doc_city, doc_tel)
            self.data_manager.add_doctor(self.docSelenium.surname , self.docSelenium.name)
            
        else:
            doc1 = self.patient_insurance_data.doc1
            doc2 = self.patient_insurance_data.doc2
            if doc1:
                self.select_docotor(doc1, 1)
            if doc2:
                self.select_docotor(doc2, 2)
        
        
        #------End on Diagnosis tab ---------
        self._play_success_sound()
        return 


            
            
    def _rechnung(self):
        
        for field in fields(self.patient_invoice):
            if field.name == "invoice_anrede":
                self.autoManager.select_from_dropdown(get_enum_from_field(field.name) ,  getattr(self.patient_invoice, field.name))
                continue
            print(field.name)
            self.autoManager.input_text(field.name, getattr(self.patient_invoice, field.name))
        self.autoManager.cur_selected_patient = (self.patient_data.name) + ", " + (self.patient_data.surname)
        if self.autoManager.cur_selected_patient:
            print ("cur patient: " + self.autoManager.cur_selected_patient)
            
            
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
            time.sleep(0.1)  
            self.autoManager._click_popup_window_away("7", "windia")

        
            
    def issue_an_invoice(self, max_hours):
        #open_patient_window -> add new patient
        self.autoManager.open_window(WindiaWindows.PATIENT)
        self.add_new_patient()
        
        #close window -> open and change Geürenkathalog
        self.autoManager.close_window()    
        self.autoManager.open_window(WindiaWindows.CATALOG)
        self.change_gebuerenkatalog()
        
        self.autoManager.close_window()    
        self.autoManager.open_window(WindiaWindows.LEISTUNGS_NACHWEIS)
        
        print(self.catalog_data.hours[1])
        interships = 2 if not self.catalog_data.hours[1] else 1
        input_hours_for_bill(self.autoManager, max_hours, interships)
        self._save_invoice_and_open_invoice_page()
        self._play_success_sound()
        
    def _save_new_patient(self):
        
        print("saving patient")
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 5/12 , 9/10)
        self.autoManager.cur_selected_patient = (self.patient_data.name) + ", " + (self.patient_data.surname)
        if self.autoManager.cur_selected_patient:
            print ("cur patient: " + self.autoManager.cur_selected_patient)

    def _edit_patient(self):
        self.autoManager.click_inside_window(WindiaWindows.PATIENT, 4/10 , 9/10)

    def select_insurance(self, insurance : str):
        self.autoManager.select_from_dropdown(PatientAutoID.INSURANCE_DROPDOWN , insurance)
    
    def select_docotor(self, doc : str, number : int):
        if int(number) <= 1:
            self.autoManager.select_from_dropdown(PatientAutoID.DOC_DROPDOWN_1 , doc)
        else:
            self.autoManager.select_from_dropdown(PatientAutoID.DOC_DROPDOWN_2 , doc)    
    
    def input_degree_of_care(self, deg : int, date : str, new = False):
        if not ( 1 <= int(deg) <= 5 ):
            print ("Pflegegrad muss zwischen 1 und 5 sein")
            return
        
        self.autoManager.click_button(Windia_Buttons.PG_BTN)
        print("click")
        self.autoManager.get_and_wait_for_window(WindiaWindows.CARE_DEGREE_HISTORY, 5)
        if new:
            self.autoManager.click_button(PatientAutoID.PG_HISTORY_TOOLBAR_NEW)
        else: 
            self.autoManager.click_button(PatientAutoID.PG_HISTORY_TOOLBAR_EDIT)
        time.sleep(1.5)
        self.autoManager.set_pg(date, deg)
        time.sleep(1.5)
        self.autoManager.click_button(PatientAutoID.PG_HISTORY_TOOLBAR_SAFE)
        time.sleep(1.5)
        self.autoManager.click_button(PatientAutoID.PG_HISTORY_TOOLBAR_CLOSE)

    

    def switch_patient_tab(self,tab : PatientWindowTabs):
        place = tab.value
        if self.switched:
            if place % 2 == 0:
                place += 1
            else:
                place -=1

        x,y = 0,0
        if place % 2 == 0:
            y = 3/13
            self.switched = False if not self.switched else True
        else:
            y = 3/15
            self.switched = True if not self.switched else False

        
        if place == 0 or place == 1:
            x = 1/10
        if place == 2 or place == 3:
            x = 3/10     
        if place == 4 or place == 5:
            x = 4/9
        if place == 6 or place == 7:
            x = 7/10
            
        self.autoManager.click_inside_window(WindiaWindows.PATIENT,x , y)
            
    def print_lns(self, path, month):

        set_month = False
        
        patient_ln_type = read_VE_fromdocx_file(path)

        cur_page = "E"
        for patient, ln_type in patient_ln_type.items():
            print(str(patient) + " : " + str(ln_type))
            
            self.autoManager.select_patient(patient)
            self.autoManager.close_window()

            if "-" in patient:
                patient = patient.replace(" - ", "-")
            #patient.replace(",  ", ",")
            patient = ' '.join(patient.split())
            print("curr Pat: " + str(patient))
            self.autoManager.cur_selected_patient = patient

            self.autoManager.open_window(WindiaWindows.LEISTUNGS_NACHWEIS)
            #input Month
            if not set_month:
                LN = self.autoManager.get_and_wait_for_window(WindiaWindows.LEISTUNGS_NACHWEIS, 5)
                self.autoManager.input_text(LN_ids.LN_MONTH, str(month),windia= LN)
                set_month = True

            if ln_type == "E+V" or ln_type == "E + V":
                print_leistungsnachweis(self.autoManager, "E", "E")
                time.sleep(5)
                self.autoManager.open_window(WindiaWindows.LEISTUNGS_NACHWEIS)
                print_leistungsnachweis(self.autoManager, "V", "E")
                cur_page = "E"
                continue

            
            print_leistungsnachweis(self.autoManager, ln_type, cur_page)
            cur_page = "E"
        
        print("Donnneeeee!")
        self._play_success_sound()
                
    def check_SZ(self):
        box_pane = self.autoManager.windia.child_window(auto_id=str(PatientAutoID.SZ_PANE.value), control_type="Pane")
        for child_pane in box_pane.children(control_type='Pane'):
            if child_pane.window_text() == "SZ":
                rec = child_pane.rectangle()
                mouse.click(coords=(int(rec.left), int(rec.top)))
        
    def _save_invoice_and_open_invoice_page(self):
        LN = self.autoManager.get_and_wait_for_window(WindiaWindows.LEISTUNGS_NACHWEIS, 5)
        self.autoManager.close_window(LN)
        time.sleep(3)
        self.autoManager.windia.set_focus()
        self.autoManager.click_yes_no(Windia_Buttons.RELATIVE_CLOSE_BTN, self.autoManager.windia)
        time.sleep(3)
        LN.set_focus()
        self.autoManager.click_yes_no(Windia_Buttons.SAVE_BUTTON_BTN, LN)
        time.sleep(5)
        self.autoManager.open_rechnungslegung()
        
    def _play_success_sound(self):
        pygame.mixer.init()
        pygame.mixer.music.load("AutomatisierungRene\successSound.mp3")
        pygame.mixer.music.play()  
        time.sleep(2)   

    def add_new_doctor(self, surname, name, street, zip_code, city, tel):
        cbox = self.autoManager.windia.child_window(auto_id=str(67), control_type="ComboBox")
        for child in cbox.children():
            if "Button" in child._control_types:
                rec = child.rectangle()
                mouse.click(coords=( int(rec.left +40)  ,  int(rec.top + 5)))

        self._doc_window_click_new_btn(120)

        self.autoManager.input_text(DocAutoIds.TITEL, "dr.med.")
        self.autoManager.input_text(DocAutoIds.SURNAME, surname)
        self.autoManager.input_text(DocAutoIds.NAME, name )
        self.autoManager.input_text(DocAutoIds.STREET, street )
        self.autoManager.input_text(DocAutoIds.ZIP, zip_code )
        self.autoManager.input_text(DocAutoIds.CITY, city )
        self.autoManager.input_text(DocAutoIds.TEL, tel )

        self._doc_window_click_new_btn(200)

        #click yes to safe new address
        try:
            self.autoManager._click_popup_window_away(Windia_Buttons.SAVE_BUTTON_BTN.value, "windia")
        except:
            pass
        self.autoManager.close_window()
        time.sleep(2)
        self.autoManager.select_from_dropdown(PatientAutoID.DOC_DROPDOWN_1,surname)


    def _doc_window_click_new_btn(self, offset : int):
        rarrow = self.autoManager.windia.child_window(auto_id=str(DocAutoIds.RIGHT_ARROW_NEXT_TO_NEW.value) , control_type="Button")
        rec = rarrow.rectangle()
        mouse.click(coords=( int(rec.left + offset )  ,  int(rec.top)))
        
    def test(self):
        self.autoManager.close_window()
        #self.autoManager.select_from_dropdown(PatientAutoID.DOC_DROPDOWN_1,surname)
        #self.autoManager._click_popup_window_away(Windia_Buttons.SAVE_BUTTON_BTN.value, "windia")
        #self.autoManager.click_yes_no(Windia_Buttons.SAVE_BUTTON_BTN, self.autoManager.windia)

#W = WindiaManager("")
#W.test()
#W._save_invoice_and_open_invoice_page()
#W.autoManager.open_window(WindiaWindows.PATIENT)

##W.patient_data = Patient("name7", "surname7", "W" ,"15.04.1995", "Frau", "Froschstr", "71126", "Gäufelden", "017522314", "07.04.2025", "", "09.04.2025")
#W.patient_insurance_data = PatientInsuranceInfo(  "XX", "Universitätsklinikum Tübingen", "AOK BW Sindelfingen P", 5, "01.01.2024", "Baiker", "Brosch", ["Eltern im Haus", "Hallo"], "braucht beatmung", True )
#W.catalog_data = Catalog("10,76", ["29.04.2024 - 06.09.2024", "21.14.2024 - 29.11.2024"] , ["210,15", "218,7"])
#W.patient_invoice = Invoice("An das", "Universitätsklinikum Tübingen", "Stabstelle KV4 Pflegedirektion, Fr.Zahn",  "Hoppe-Seyer-Str.6", "72076", "Tübingen")
#W.patient_invoice = Invoice("An das", "Universitätsklinikum Tübingen", "Stabstelle KV4 Pflegedirektion, Fr.Zahn",  "Hoppe-Seyer-Str.6", "72076", "Tübingen")


#W.autoManager.open_window(WindiaWindows.PATIENT)
#W.add_new_patient()
#W.autoManager.close_window()
#W.autoManager.open_window(WindiaWindows.CATALOG)
#W.change_gebuerenkatalog()
#W.autoManager.close_window()
#W.autoManager.open_window(WindiaWindows.LEISTUNGS_NACHWEIS)
#input_hours_for_bill(W.autoManager, 200)

#W.test()
