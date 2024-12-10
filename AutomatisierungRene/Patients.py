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

windia = setup_winDia()

#name = windia.child_window(auto_id="192", control_type="Edit").wrapper_object()
#surname = windia.child_window(auto_id="193", control_type="Edit").wrapper_object()
#birthday = windia.child_window(auto_id="168", control_type="Edit").wrapper_object()
anrede_comboBox = windia.child_window(auto_id="150", control_type="ComboBox").wrapper_object()
#name.set_text("Test")
#surname.set_text("Test")
#birthday.set_text("01.01.2004")

anrede = anrede_comboBox.children(control_type='Edit')
anrede[0].set_text("Frau")

