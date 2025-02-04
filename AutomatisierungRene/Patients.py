from pywinauto.application import Application
from pywinauto import findwindows
from pywinauto import Desktop
import pywinauto.mouse as mouse
from pywinauto import keyboard
from dataclasses import dataclass
import time
from pywinauto.timings import wait_until

def setup_winDia():
    open_windows = Desktop(backend="uia").windows()

    for window in open_windows:
        
        window_title = window.window_text()
        if "WinDIA® AMBULINO GmbH" in window_title:
            app = Application(backend="uia").connect(handle=window.handle, timeout=4)
            windia = app.window(handle=window.handle)

            return windia
        

def print_info(dialog):
    dialog.print_control_identifiers()



def open_patient_window(windia):
    windia.set_focus()
    keyboard.send_keys("%{s}{p}")

def open_catalog_window(windia):
    windia.set_focus()
    keyboard.send_keys("^G")

def open_ln_window(windia):
    windia.set_focus()
    keyboard.send_keys("^L")  

def get_patient_window(dialog):
    sub_windows = dialog.children()
    
    for window in sub_windows:
        if "Arbeitsbereich" in window.window_text():
            for dlg in window.children():
                if "Patient" in dlg.window_text():
                    return dlg

def get_catalog_window(dialog):
    sub_windows = dialog.children()
    
    for window in sub_windows:
        if "Arbeitsbereich" in window.window_text():
            for dlg in window.children():
                if "Erfassung Gebührenkatalog" in dlg.window_text():
                    return dlg
                
def get_ln_window(dialog):  #TODO: change testname 
    open_windows = Desktop(backend="uia").windows()

    for window in open_windows:
        
        window_title = window.window_text()
        print(window_title)
        if "testname" in window_title:
            app = Application(backend="uia").connect(handle=window.handle, timeout=4)
            ln = app.window(handle=window.handle)

            return ln
                
def check_popup_window(dialog):
    sub_windows = dialog.children()
    
    for window in sub_windows:
        if "windia" == window.window_text():
            no_btn = dialog.child_window(auto_id="7", control_type="Button").wrapper_object()
            no_btn.invoke()

def click_inside_window(win_rectangle, left_percent, top_percent, double_click = False):
    width = win_rectangle.right - win_rectangle.left
    height = win_rectangle.bottom - win_rectangle.top
    x = win_rectangle.left + width * (left_percent)
    y = win_rectangle.top + height * (top_percent)
    if(double_click):
        mouse.double_click(coords=(int(x), int(y)))
        return 
    mouse.click(coords=(int(x), int(y)))


def add_new_patient(windia, name, surname, birthday, anrede, gender, street, zip_code, city, telephone, care_beginning_date, care_end_date ,admission_date, doctor, diagnoses, insurance, insurence_number, level_of_care, invoice_anrede = None, invoice_name = None, invoice_name_second_line = None ):
    
    
    #click NEW
    patient_dlg = get_patient_window(windia)
    wait_until(5, 0.1, patient_dlg.is_enabled)
    #click_inside_window(patient_dlg.rectangle(), 3/9 , 9/10)
    

    #----------------Pflegekasse-------------------------#
    krankenkasse_checkbox = windia.child_window(title="Pflegeversicherung   ja / nein", control_type="Pane")
    krankenkasse_checkbox.click_input()

    return
 
     #----------------Stamm-------------------------#

    p_name = windia.child_window(auto_id="193", control_type="Edit").wrapper_object()
    p_name.set_text(name)

    p_surname = windia.child_window(auto_id="192", control_type="Edit").wrapper_object()
    p_surname.set_text(surname)

    p_birthday = windia.child_window(auto_id="168", control_type="Edit").wrapper_object()
    p_birthday.set_text(birthday)

    anrede_comboBox = windia.child_window(auto_id="150", control_type="ComboBox").wrapper_object()
    p_anrede = anrede_comboBox.children(control_type='Edit')
    p_anrede[0].set_text(anrede)

    p_street = windia.child_window(auto_id="157", control_type="Edit").wrapper_object()
    p_street.set_text(street)

    p_zip = windia.child_window(auto_id="158", control_type="Edit").wrapper_object()
    p_zip.set_text(zip_code)

    p_city = windia.child_window(auto_id="156", control_type="Edit").wrapper_object()
    p_city.set_text(city)

    female = windia.child_window(title="W", control_type="Pane")
    coordinates = female.rectangle().mid_point()
    mouse.click(coords=(coordinates.x, coordinates.y))

    p_telephone = windia.child_window(auto_id="151", control_type="Edit").wrapper_object()
    p_telephone.set_text(telephone)

    p_care_beginning_date = windia.child_window(auto_id="166", control_type="Edit").wrapper_object()
    p_care_beginning_date.set_text(care_beginning_date)

    p_care_end_date = windia.child_window(auto_id="167", control_type="Edit").wrapper_object()
    p_care_end_date.set_text(care_end_date)

    p_admission_date = windia.child_window(auto_id="165", control_type="Edit").wrapper_object()
    p_admission_date.set_text(admission_date)

    #----------------Pflege-------------------------#

    #----------------Pflegekasse-------------------------#

    #----------------Krankenkasse-------------------------#
    click_inside_window(patient_dlg.rectangle(),4/9 , 3/13)

    krankenkasse_checkbox = windia.child_window(title="Behandlungspflege   ja / nein", control_type="Pane")
    krankenkasse_checkbox.click_input()

    insurance_dropdown = windia.child_window(auto_id="138", control_type="ComboBox").wrapper_object()   
    insurance_button = insurance_dropdown.children(control_type='Button')[0]
    insurance_button.invoke()

    insurences_list = insurance_dropdown.children(control_type='List')[0]
    insurences = insurences_list.children(control_type='ListItem')

    for insurance in insurences:
        #print((insurance.window_text()))

        if "Universitätsklinikum Tübingen" in insurance.window_text():
            print(insurance)
            insurance.invoke()
    
    p_insurance_number = windia.child_window(auto_id="137", control_type="Edit").wrapper_object()
    p_insurance_number.set_text(insurence_number)

    #----------------Rechnung-------------------------#
    click_inside_window(patient_dlg.rectangle(),6/10 , 3/13)
    #aNREDE
    anrede_comboBox = windia.child_window(auto_id="92", control_type="ComboBox").wrapper_object()
    i_anrede = anrede_comboBox.children(control_type='Edit')
    i_anrede[0].set_text(invoice_anrede)

    i_name = windia.child_window(auto_id="89", control_type="Edit").wrapper_object()
    i_name.set_text(invoice_name)

    i_name = windia.child_window(auto_id="91", control_type="Edit").wrapper_object()
    i_name.set_text(invoice_name_second_line)
    
    i_street = windia.child_window(auto_id="88", control_type="Edit").wrapper_object()
    i_street.set_text(street)

    i_zip = windia.child_window(auto_id="87", control_type="Edit").wrapper_object()
    i_zip.set_text(zip_code)

    i_city = windia.child_window(auto_id="86", control_type="Edit").wrapper_object()
    i_city.set_text(city)


    #SAFE
    click_inside_window(patient_dlg.rectangle(), 4/9 , 9/10)

def  change_gebuerenkatalog(windia, hourly_wage, dates, hours):
    #select catalog
    catalog_dropdown = windia.child_window(auto_id="52", control_type="ComboBox").wrapper_object()  
    catalog_button = catalog_dropdown.children(control_type='Button')[0]
    catalog_button.invoke()

    catalog_list = catalog_dropdown.children(control_type='List')[0]
    catalogs = catalog_list.children(control_type='ListItem')
    for catalog in catalogs:
        if "Selbstzahler" in catalog.window_text():
            catalog.invoke()

    time.sleep(0.5)


    #select Praxiseinsatz 1 and then 2
    for i in range(1,5):
        praxiseinsatz_index = ("1" if i == 1 else "2")
        
        praxiseinsatz_dropdown = windia.child_window(auto_id="83", control_type="ComboBox").wrapper_object()   
        praxiseinsatz_button = praxiseinsatz_dropdown.children(control_type='Button')[0]
        praxiseinsatz_button.invoke()

        praxiseinsatz_list = praxiseinsatz_dropdown.children(control_type='List')[0]
        praxiseinsaetze = praxiseinsatz_list.children(control_type='ListItem')
        
        for praxiseinsatz in praxiseinsaetze:
            if (i%2) == 1 and f"Praxiseinsatz {praxiseinsatz_index}" in praxiseinsatz.window_text():
                praxiseinsatz.invoke()
            elif (i%2) == 0 and f"{i}-{i}" in praxiseinsatz.window_text():
                praxiseinsatz.invoke()

        #Change Name, Price and Number
        catalog_dlg = get_catalog_window(windia)
        click_inside_window(catalog_dlg.rectangle(),5/9 , 9/10)    #Ändern btn    
        price = windia.child_window(auto_id="80", control_type="Edit").wrapper_object()
        name = windia.child_window(auto_id="82", control_type="Edit").wrapper_object()

        if(i%2 == 1):
            price.set_text(hourly_wage)
            name.set_text(f"Praxiseinsatz {praxiseinsatz_index}: allg. ambulante Akut- und Langzeitpflege")
        else:
            #price.set_text("0,01")
            name.set_text(f"{dates[(i%3) % 2]}, {hours[(i%3) % 2]} h")

        number = windia.child_window(auto_id="85", control_type="Edit").wrapper_object()
        number.set_text(str(i))

        row = windia.child_window(auto_id="67", control_type="Edit").wrapper_object()
        row.set_text(str(i))

        click_inside_window(catalog_dlg.rectangle(),5/9 , 9/10)    #Save btn   
        check_popup_window(windia)
    #select line with the date for Praxiseinsatz 1 and then 2


def change_leistungsnachweis(windia):
    #select Selbstzahler tab
    time.sleep(10)
    ln_dlg = get_ln_window(windia)

    click_inside_window(ln_dlg.rectangle(),6/9 , 1/8)

    #Click inside Table
    click_inside_window(ln_dlg.rectangle(),3/10 , 15/40)
    keyboard.send_keys("200")
    click_inside_window(ln_dlg.rectangle(),3/10 , 16/40)

    click_inside_window(ln_dlg.rectangle(),3/10 , 17/41)
    keyboard.send_keys("200")
    click_inside_window(ln_dlg.rectangle(),3/10 , 18/41)

    #click Rechnug = Done
    #click_inside_window(ln_dlg.rectangle(),3/11 , 9/10)



windia = setup_winDia()
#open_patient_window(windia)
add_new_patient(windia,"testname2","testSurname2","01.01.2004","Frau","W","Froschberg 32","71126","Gäufelden","01561823412", "14.01.2025", "15.02.2025","13.01.2025","doc","diagnosis","Uni Tübingen","XX",1, "An das", "Universitätsklinikum Tübingen", "Stabstelle KV4 Pflegedirektion, Fr.Zahn" )

#open_catalog_window(windia)
dates = ["29.07.2024 - 06.09.2024", "21.10.2024 - 29.11.2024"] 
hours = ["220,05", "218,7"] 
#change_gebuerenkatalog(windia, "10,74",dates, hours)
#open_ln_window(windia)
#change_leistungsnachweis(windia)

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

    #test commit on new PC