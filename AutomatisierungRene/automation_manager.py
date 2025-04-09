from pywinauto.application import Application
from pywinauto import findwindows
from pywinauto import Desktop
import pywinauto.mouse as mouse
from pywinauto import keyboard
import time
from pywinauto.timings import wait_until
from windia_enums import *
from element_selection import *
from patient_data_form import get_enum_from_field

ARBEITSBEREICH = "Arbeitsbereich"
WINDIA_DLG_STRING = "WinDIA® AMBULINO GmbH"
PATIENT_DLG_STRING = "Patient"
CATALOG_DLG_STRING = "Erfassung Gebührenkatalog"

class AutomationManager:
    windia = None
    cur_selected_patient = ""
    
    
    def __init__(self):
        self.windia = self.setup_automation(WINDIA_DLG_STRING)
        print(self.windia)

    def set_catalog_price(self, val):
        self.catalog_price = val
        
    def setup_automation(self, app_name):
        open_windows = Desktop(backend="uia").windows()

        for window in open_windows:
            
            window_title = window.window_text()
            if app_name in window_title:
                app = Application(backend="uia").connect(handle=window.handle, timeout=4)
                return app.window(handle=window.handle)
            
    def _print_info(self):
        self.windia.print_control_identifiers()
        
    def get_sub_window(self, subwindow_title : str , subDialog = None):
        sub_windows = self.windia.children()
        #print(sub_windows)
        for window in sub_windows:
            if subwindow_title in window.window_text():
                if subDialog == None:
                    return window
                #print(window)
                for dlg in window.children():
                    if subDialog in dlg.window_text():
                        return dlg
                    
    def get_separate_window(self, w_title : str):  
        open_windows = Desktop(backend="uia").windows()

        for window in open_windows:
            
            window_title = window.window_text()
            if w_title in window_title:
                app = Application(backend="uia").connect(handle=window.handle, timeout=4)
                dialog = app.window(handle=window.handle)

                return dialog
            
    def open_window(self, window : WindiaWindows):
        self.windia.set_focus()
        match window:
            case  WindiaWindows.LEISTUNGS_NACHWEIS:
                keyboard.send_keys("^L") 
            case  WindiaWindows.PATIENT:
                keyboard.send_keys("%{s}{p}")
            case WindiaWindows.CATALOG:
                keyboard.send_keys("^G")
            case WindiaWindows.WINDIA:
                pass
                    
    def _click_popup_window_away(self, id):
        sub_windows = self.windia.children()
        
        for window in sub_windows:
            if WINDIA_DLG_STRING == window.window_text():
                no_btn = self.windia.child_window(auto_id=str(id), control_type="Button").wrapper_object()
                no_btn.invoke()
        
    def click_inside_window(self, window : WindiaWindows, left_percent, top_percent, click = True):
        
        win_rectangle = self._get_rec(window)
        width = win_rectangle.right - win_rectangle.left
        height = win_rectangle.bottom - win_rectangle.top
        x = win_rectangle.left + width * (left_percent)
        y = win_rectangle.top + height * (top_percent)
        if click:
            #mouse.double_click(coords=(int(x), int(y)))
            #return 
            mouse.click(coords=(int(x), int(y)))
        else:
            mouse.move(coords=(int(x), int(y)))
    
    def click_middle_of_field(self, field_name):
        element_enum = get_enum_from_field(field_name)
        if not element_enum:
            return
        if element_enum.value == -1:
            w = get_wrapper(element_enum, self.windia)
            coordinates = get_rec_midpoint_of_wrapper(w)
            mouse.click(coords=(coordinates.x, coordinates.y))
        
    def _get_rec(self, window : WindiaWindows):
        dlg = None
        match window:
            case  WindiaWindows.LEISTUNGS_NACHWEIS:
                dlg = self.get_separate_window(self.cur_selected_patient)
            case  WindiaWindows.PATIENT:
                dlg = self.get_sub_window(ARBEITSBEREICH, PATIENT_DLG_STRING)
            case WindiaWindows.CATALOG:
                dlg = self.get_sub_window(ARBEITSBEREICH, CATALOG_DLG_STRING)
            case WindiaWindows.WINDIA:
                pass
        if not dlg:
            return
        wait_until(5, 0.1, dlg.is_enabled)
        return dlg.rectangle() if dlg else None

    def select_patient(self, windia, patient_firstname, patient_surname):
        patient_name = patient_surname + patient_firstname
        #open Patienten Window
        self.open_window(WindiaWindows.PATIENT)
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
                self.cur_selected_patient = patient_name
                
    
    def get_child_object(self):
        pass
    
    def input_text(self, field_name_or_enum , text : str ):
        element_enum = None
        if isinstance(field_name_or_enum, str):
            element_enum = get_enum_from_field(field_name_or_enum)
        else:
            element_enum = field_name_or_enum
        
        if not element_enum:
            return
        
        if element_enum.value == -1:
            return
        print(element_enum)
        get_wrapper(element_enum, self.windia).set_text(text) 
        
    
        
        
    def select_from_dropdown(self, combo_box_id : str, element_to_select : str, title = None):
        if title:
            checkbox = self.windia.child_window(title=title, control_type="Pane")
            checkbox.click_input()

        dropdown = self.windia.child_window(auto_id=str(combo_box_id), control_type="ComboBox").wrapper_object()   
        button = dropdown.children(control_type='Button')[0]
        button.invoke()
        time.sleep(0.5)
        element_list = dropdown.children(control_type='List')[0]
        elements = element_list.children(control_type='ListItem')
        
        for element in elements:
            if element_to_select in element.window_text():
                print(element)
                element.invoke()
                
    def close_window(self):
        self.windia.SchließenButton.invoke()