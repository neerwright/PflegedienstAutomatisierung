
from enum import Enum
from windia_ids import *
from pywinauto.application import Application




    
def get_wrapper(element : Enum, windia, title = None):
    print("getting wrapper for: " + str(element))
    id = element.value 
    c_type = get_control_type(id)

    if c_type == "Pane":
        return windia.child_window(title=title, control_type=c_type)
    if c_type == "ComboBox":
        comboBox = windia.child_window(auto_id=str(id), control_type=c_type).wrapper_object()
        return comboBox.children(control_type='Edit')
    
    return windia.child_window(auto_id=str(id), control_type=c_type, found_index=0).wrapper_object()
                    
            
def get_control_type(element_id):
    if isinstance(element_id, Windia_Buttons ):
        print("bingo")
        return "Button"
    #if element_id == 88:
        
    if element_id == PatientAutoID.GENDER.value:
        return "Pane"
    if element_id == PatientAutoID.INVOICE_ANREDE.value or element_id == PatientAutoID.ANREDE.value or element_id == PatientAutoID.LEISTUNG.value:
        return "ComboBox"
    #if element_id == PatientAutoID.OK_BUTTON.value or element_id == PatientAutoID.PG_BUTTON.value or element_id == RelativesAutoID.CLOSE_BTN.value or element_id == LN_ids.EINSTELLUNG_BTN.value or  element_id == LN_ids.LN_PRINT_once.value :
    #    return "Button"
    return "Edit"

      #Windia_Buttons  
def get_rec_midpoint_of_wrapper(element_wrapper):
    return element_wrapper.rectangle().mid_point()

get_control_type(PatientAutoID.INVOICE_ANREDE)