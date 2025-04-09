from automation_manager import AutomationManager
from windia_enums import WindiaWindows
from pywinauto import keyboard

def input_hours_for_bill(automationManager : AutomationManager):
    offset = 0.024
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, 6/9 , 1/8)

    #Click inside Table
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, 3/10 , 18/50 + offset)
    keyboard.send_keys("200")
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, 3/10 , 19/50 + offset)

    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS,3/10 , 20/50 + offset)

    keyboard.send_keys("200")
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS,3/10 , 21/50 + offset)


    #click Rechnug = Done
    #automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS,3/11 , 9/10)

a = AutomationManager()
a.cur_selected_patient = "Plattner"
input_hours_for_bill(a)