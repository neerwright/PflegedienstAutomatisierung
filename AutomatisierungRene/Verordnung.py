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

            newApp = Application(backend="win32").connect(handle=window.handle)
            windia32 = newApp.window(handle=window.handle)
            print(windia32.print_control_identifiers())
            s = windia32.MehrfachauswahlSPR32A80_SpreadSheet
            #print((s.print_control_identifiers()))
            s.click_input()
            return windia



def print_info(dialog):
    dialog.print_control_identifiers()



def select_patient(windia, verordnung_window, patient):
    #click_magnifying_glas(verordnung_window.rectangle())
    #print_info(windia)
    #app=Desktop(backend="win32").windows()
    #print(app)
    pass
    #mehr = windia.child_window(title="Mehrfachauswahl", auto_id="42", control_type="CheckBox").wrapper_object()
    #mehr.click_input()



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
verordnung_window = get_verordnungen_window(windia)
select_patient(windia,verordnung_window, "Celep, Efe")

