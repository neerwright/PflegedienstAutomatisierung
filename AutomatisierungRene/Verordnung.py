from pywinauto.application import Application
from pywinauto import findwindows
from pywinauto import Desktop
import csv
import pywinauto.mouse as mouse
from pywinauto import keyboard




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


def get_verordnungen_window(dialog):
    sub_windows = dialog.children()
    
    for window in sub_windows:
        if "Arbeitsbereich" in window.window_text():
            for dlg in window.children():
                if "Verordnung" in dlg.window_text():
                    return dlg

def click_magnifying_glas(win_rectangle):
    width = win_rectangle.right - win_rectangle.left
    height = win_rectangle.bottom - win_rectangle.top
    x = win_rectangle.left + width * (1/6.4)
    y = win_rectangle.top + height * (1/7)
    mouse.click(coords=(int(x), int(y)))

windia = setup_winDia()
#verordnung_window = get_verordnungen_window(windia)
#select_patient(windia, "Hanna", "Schnaible")
new_verordnung(windia)
