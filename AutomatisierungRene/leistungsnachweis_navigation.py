from automation_manager import AutomationManager
from windia_enums import WindiaWindows
from pywinauto import keyboard

def input_hours_for_bill(automationManager : AutomationManager):

    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, 6/9 , 1/8)

    #Click inside Table
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, 3/10 , 18/50)
    keyboard.send_keys("200")
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, 3/10 , 19/50)

    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS,3/10 , 20/50)

    keyboard.send_keys("200")
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS,3/10 , 21/50)


    #click Rechnug = Done
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS,3/11 , 9/10)
