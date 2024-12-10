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



def select_patient(windia, patient_firstname, patient_surname):
    patient_name = patient_surname + patient_firstname
    #open Patienten Window
    windia.set_focus()
    keyboard.send_keys("%{s}{p}")
    #Find patient
    patient_scrollbar = windia.child_window(auto_id="1", control_type="List").wrapper_object()
    patients = patient_scrollbar.children(control_type='ListItem')
    for patient in patients:
        patient_string = ""
        for char in patient.window_text():
            if char.isalpha():
                patient_string += char
        if patient_string == patient_name:
            print("found patient!")
            patient.invoke()

def new_verordnung(windia):
    #open verordnung Window
    windia.set_focus()
    keyboard.send_keys("%{e}{v}")


    #click new
    verordnung_dlg = get_verordnungen_window(windia)
    click_inside_window(verordnung_dlg.rectangle(),3/8 , 9/10)

    #VO auswählen
    all_vo_checkbox = windia.child_window(title="alle VO anzeigen", auto_id="46", control_type="CheckBox").wrapper_object()
    all_vo_checkbox.invoke()
    ok_btn = windia.child_window(title="OK", auto_id="2", control_type="Button").wrapper_object()
    ok_btn.invoke()
    
    input_zeitintensive_pflege_kinde(windia, verordnung_dlg)
    

def get_verordnungen_window(dialog):
    sub_windows = dialog.children()
    
    for window in sub_windows:
        if "Arbeitsbereich" in window.window_text():
            for dlg in window.children():
                if "Verordnung" in dlg.window_text():
                    return dlg

def input_zeitintensive_pflege_kinde(windia, verordnung_dlg):
    vo_dropdown = windia.Edit.wrapper_object()
    click_inside_window(verordnung_dlg.rectangle(),1/10 , 1/2 , False)
    click_inside_window(verordnung_dlg.rectangle(),1/10 , 6/9)
    time.sleep(0.1)
    for item in vo_dropdown.legacy_properties().values():
        if "Zeitintensive Pflege" in str(item):
            print(item)
            return
    
    #the dropdown was sorted in the wrong way - need to try again
    vo_dropdown = windia.Edit.wrapper_object()
    click_inside_window(verordnung_dlg.rectangle(),1/10 , 1/2 , False)
    click_inside_window(verordnung_dlg.rectangle(),1/10 , 6/9)
    for item in vo_dropdown.legacy_properties().values():
        if "Zeitintensive Pflege" in str(item):
            print(item)
            print("2")
            return

def click_inside_window(win_rectangle, left_percent, top_percent, double_click = False):
    width = win_rectangle.right - win_rectangle.left
    height = win_rectangle.bottom - win_rectangle.top
    x = win_rectangle.left + width * (left_percent)
    y = win_rectangle.top + height * (top_percent)
    if(double_click):
        mouse.double_click(coords=(int(x), int(y)))
        return 
    mouse.click(coords=(int(x), int(y)))

windia = setup_winDia()
#select_patient(windia, "Hanna", "Schnaible")
#new_verordnung(windia)

#print_info(windia)
#comboBox = windia.child_window(auto_id="48", control_type="ComboBox").wrapper_object()
#Intervall = comboBox.children(control_type='Edit')
#print(Intervall[0].get_value())

time_begin = windia.child_window(auto_id="51", control_type="Edit").wrapper_object()
time_begin.set_text("02.10.2024")
print(time_begin.get_value())

time_end = windia.child_window(auto_id="53", control_type="Edit").wrapper_object()
time_end.set_text("03.10.2024")