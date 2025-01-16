from pywinauto.application import Application
from pywinauto import findwindows
from pywinauto import Desktop
import pywinauto.mouse as mouse
from pywinauto import keyboard
import time

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

def get_patient_window(dialog):
    sub_windows = dialog.children()
    
    for window in sub_windows:
        if "Arbeitsbereich" in window.window_text():
            for dlg in window.children():
                if "Patient" in dlg.window_text():
                    return dlg

def click_inside_window(win_rectangle, left_percent, top_percent, double_click = False):
    width = win_rectangle.right - win_rectangle.left
    height = win_rectangle.bottom - win_rectangle.top
    x = win_rectangle.left + width * (left_percent)
    y = win_rectangle.top + height * (top_percent)
    if(double_click):
        mouse.double_click(coords=(int(x), int(y)))
        return 
    mouse.click(coords=(int(x), int(y)))


def add_new_patient(windia, name, surname, birthday, anrede, gender, street, zip_code, city, telephone, care_beginning_date, care_end_date ,admission_date, doctor, diagnoses, insurance, insurence_number, level_of_care, Rechnung = None ):
    
    

    
    #click NEW
    patient_dlg = get_patient_window(windia)
    click_inside_window(patient_dlg.rectangle(),3/9 , 9/10)

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




    #save button
    #click_inside_window(patient_dlg.rectangle(),2/5 , 9/10)


    
    
windia = setup_winDia()
#open_patient_window(windia)
#print_info(windia)
add_new_patient(windia,"testname","testSurname","01.01.2004","Frau","W","Froschberg 32","71126","Gäufelden","01561823412", "14.01.2025", "15.02.2025","13.01.2025",1,1,1,1,1)
#patient_dlg = get_patient_window(windia)
#click_inside_window(patient_dlg.rectangle(), 2/5 , 9/10)