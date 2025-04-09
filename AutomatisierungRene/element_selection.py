
from enum import Enum
from windia_enums import WindiaWindows
from pywinauto.application import Application




    
def get_wrapper(element : Enum, windia, title = None):
    id = element.value 
    c_type = get_control_type(id)

    if c_type == "Pane":
        return windia.child_window(title=title, control_type=c_type)
    if c_type == "ComboBox":
        comboBox = windia.child_window(auto_id=str(id), control_type=c_type).wrapper_object()
        return comboBox.children(control_type='Edit')
    return windia.child_window(auto_id=str(id), control_type=c_type).wrapper_object()
                    
            
def get_control_type(element_id):
    if element_id == -1:
        return "Pane"
    if element_id == 92 or element_id == 150:
        return "ComboBox"
    return "Edit"

        
def get_rec_midpoint_of_wrapper(element_wrapper):
    return element_wrapper.rectangle().mid_point()