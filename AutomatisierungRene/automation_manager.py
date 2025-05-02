from pywinauto.application import Application
from pywinauto import findwindows
from pywinauto import Desktop
import pywinauto.mouse as mouse
from pywinauto import keyboard
import time
from pywinauto.timings import wait_until
from windia_ids import *
from element_selection import *
from patient_data_form import get_enum_from_field


ARBEITSBEREICH = "Arbeitsbereich"
DEG_OF_CARE_WINDOW_TITLE = "Pflegestufenhistorie"
WINDIA_DLG_STRING = "WinDIA® AMBULINO GmbH"
PATIENT_DLG_STRING = "Patient"
CATALOG_DLG_STRING = "Erfassung Gebührenkatalog"
AUSDRUCK_LN__DLG_STRING = " Ausgabe Leistungsnachweis"
DIST_TO_SECOND_MONITOR = 750

class AutomationManager:
    windia = None
    cur_selected_patient = ""
    
    
    def __init__(self):
        self.windia = self.setup_automation(WINDIA_DLG_STRING)
        print(self.windia)

    def select_gender(self, gender : str):
        
        w = self.windia.child_window(title=str(gender), control_type="Pane")

        coordinates = get_rec_midpoint_of_wrapper(w)
        mouse.click(coords=(coordinates.x, coordinates.y))

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
        dlg = None
        match window:
            case  WindiaWindows.LEISTUNGS_NACHWEIS:
                keyboard.send_keys("^L") 
                self.get_and_wait_for_window(WindiaWindows.LEISTUNGS_NACHWEIS, 60)
                time.sleep(10)
            case  WindiaWindows.PATIENT:
                keyboard.send_keys("%{s}{p}")
                self.get_and_wait_for_window(WindiaWindows.PATIENT, 10)
            case WindiaWindows.CATALOG:
                keyboard.send_keys("^G")
                self.get_and_wait_for_window(WindiaWindows.CATALOG, 5)
            case WindiaWindows.AUSDRUCK_LN:
                self.get_and_wait_for_window(WindiaWindows.AUSDRUCK_LN, 10)
            case WindiaWindows.WINDIA:
                pass

    def open_rechnungslegung(self):
        #menuApp = self.setup_automation()
        open_windows = Desktop(backend="uia").windows()
        for window in open_windows:
            window_title = window.window_text()
            if window_title == "AMBULINO GmbH":
                pwa_app = Application(backend="uia").connect(handle=window.handle, timeout=4)
                dialog = pwa_app.window(handle=window.handle)
                print("Found " + str(pwa_app))
                dialog.set_focus()
                rec = dialog.child_window(auto_id="1", control_type="Pane").wrapper_object().rectangle()
                mouse.click(coords=(int(rec.right - 50), int(rec.bottom - 80)))
            
        #\\ambulinods\windia\windiastart.exe
 
        #app_path = "//ambulinods/windia/windiastart.exe"


        
        
        #print(rec)
        #
        
        
                    
    def _click_popup_window_away(self, id, title, w = None):
        sub_windows = self.windia.children()
        if w:
            btn= w.child_window(auto_id=str(id), control_type="Button", found_index=0).wrapper_object()
            btn.invoke()

        for window in sub_windows:
            if title == window.window_text():
                no_btn = self.windia.child_window(auto_id=str(id), control_type="Button", found_index=0).wrapper_object()
                no_btn.invoke()
        
    def click_inside_window(self, window : WindiaWindows, left_percent, top_percent, click = True):
        
        win_rectangle = self._get_rec(window)
        width = abs(win_rectangle.right - win_rectangle.left)
        height = abs(win_rectangle.bottom - win_rectangle.top)
        x = win_rectangle.left + width * (left_percent)
        y = win_rectangle.top + height * (top_percent)
        if click:
            mouse.click(coords=(int(x), int(y)))
        else:
            mouse.move(coords=(int(x), int(y)))
        
    def click_on_top_left_corner(self,element, offset_x : float, offset_y : float, double_click = False):
        rec = element.rectangle()
        if not double_click:
            mouse.click(coords=(int(rec.left + offset_x), int(rec.top + offset_y)))
        else:
            mouse.double_click(coords=(int(rec.left + offset_x), int(rec.top + offset_y)))
    

        
    def _get_rec(self, window : WindiaWindows):
        dlg = self.get_and_wait_for_window(window, 5)
        return dlg.rectangle() if dlg else None

    def select_patient(self, patient_name):
        if not self.get_and_wait_for_window(WindiaWindows.PATIENT, 3):
            self.open_window(WindiaWindows.PATIENT)
        patient_name = patient_name.replace(",", "")
        patient_name = patient_name.replace(" ", "")
        patient_name = patient_name.replace("-", "")
        print(patient_name)
        #open Patienten Window
        #self.open_window(WindiaWindows.PATIENT)
        #Find patient
        patient_scrollbar = self.windia.child_window(auto_id="1", control_type="List").wrapper_object()
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
                return True
        return False
                
    
    def get_child_object(self):
        pass
    
    def input_text(self, field_name_or_enum , text : str , windia = None):
        if windia is None:
            windia = self.windia
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
        get_wrapper(element_enum, windia).set_text(text) 
        
    
    def check_pane_tickbox(self, tickbox_title : str):
        checkbox = self.windia.child_window(title=tickbox_title, control_type="Pane")
        checkbox.click_input()
        
    def select_from_dropdown(self, combo_box_id : Enum, element_to_select : str, tickbox_title = None):
        if tickbox_title: # makes the dropdown appear on the Krankenkassen tab
            self.check_pane_tickbox(tickbox_title)


        dropdown = self.windia.child_window(auto_id=str(combo_box_id.value), control_type="ComboBox").wrapper_object()   
        button = dropdown.children(control_type='Button')[0]
        button.invoke()
        time.sleep(0.5)
        element_list = dropdown.children(control_type='List')[0]
        elements = element_list.children(control_type='ListItem')
        
        for element in elements:
            print(element.window_text())
            if element_to_select in element.window_text():
                #print(element)
                try:
                    element.invoke()
                except:
                    print("something went wrong when selecting from dropdown, but will proceed")
                    pass
                
    def close_window(self, window = None):
        if window:
            window.SchließenButton.invoke()
        self.windia.SchließenButton.invoke()

    def click_yes_no(self, butn : Enum,  window):
        window.child_window(auto_id=str(butn.value), control_type="Button").wrapper_object().click()

    def click_button(self, button : Enum, double_click = False):
        if button == PatientAutoID.PG_HISTORY_TOOLBAR_NEW or button == PatientAutoID.PG_HISTORY_TOOLBAR_SAFE or button == PatientAutoID.PG_HISTORY_TOOLBAR_CLOSE or button == PatientAutoID.PG_HISTORY_TOOLBAR_EDIT:
            pg_window = self.find_win32_window(DEG_OF_CARE_WINDOW_TITLE)
            rec = pg_window.rectangle()
            new_button = self.get_child_by_classname(pg_window,"AfxWnd40")
            x_offset = -button.value if rec.left <= DIST_TO_SECOND_MONITOR else -button.value * 0.77
            self.click_on_top_left_corner(new_button, x_offset ,20, double_click)
            return
  
        if not double_click:
            get_wrapper(button, self.windia).click()
        else:
            get_wrapper(button, self.windia).double_click()

    def find_win32_window(self, w_title : str, dont_wrap = False):
        dialog = Desktop(backend="win32").window(title=w_title)
        #print(dialog.print_control_identifiers())
        wait_until(5, 0.1, dialog.is_enabled)

        if dont_wrap:
            return dialog
        return dialog.wrapper_object()

    def get_child_by_classname(self, element, classname : str):
        for c in element.children():
            if (c.class_name() == classname):
                return c
            
    def set_pg(self, date : str, pg : str):
        dialog = Desktop(backend="win32").window(title=DEG_OF_CARE_WINDOW_TITLE)
        rec = dialog.wrapper_object().rectangle()



        for c in dialog.descendants():

            pg_y_dist = 324
            pg_x_dist = 330
            date_x_dist = 161
            date_y_dist = 320
            #very hacky, but names keep changing, had to work with image recogniion to find the edit fields instead
            if c.friendly_class_name() == "Edit" and c.is_visible() == True:                
                if self.check_if_element_in_correct_position(c.rectangle(), rec, pg_x_dist, pg_y_dist):
                    c.set_text(str(pg))
                if self.check_if_element_in_correct_position(c.rectangle(), rec, date_x_dist, date_y_dist):
                    c.set_text(str(date))
    

    def check_if_element_in_correct_position(self, element_rec, window_rec, x_distance, y_distance):
        delta = 80
        x_dist = abs(element_rec.left - window_rec.left)
        y_dist = abs(element_rec.top - window_rec.top)
        if abs(x_dist - x_distance) < delta  and abs(y_dist - y_distance) < delta:
            return True
        return False

    def get_and_wait_for_window(self, window : WindiaWindows, wait_time : float):
        match window:
            case  WindiaWindows.LEISTUNGS_NACHWEIS:
                dlg = self.get_separate_window(self.cur_selected_patient)
            case  WindiaWindows.PATIENT:
                dlg = self.get_sub_window(ARBEITSBEREICH, PATIENT_DLG_STRING)
            case WindiaWindows.CATALOG:
                dlg = self.get_sub_window(ARBEITSBEREICH, CATALOG_DLG_STRING)
            case WindiaWindows.CARE_DEGREE_HISTORY:
                dlg = self.find_win32_window(DEG_OF_CARE_WINDOW_TITLE)
            case WindiaWindows.AUSDRUCK_LN:
                dlg = self.get_separate_window(AUSDRUCK_LN__DLG_STRING)

            case WindiaWindows.WINDIA:
                pass
        if not dlg:
            return False
        try:
            wait_until(wait_time, 0.1, dlg.is_enabled)
        except:
            pass
        return dlg
