from automation_manager import AutomationManager
from windia_enums import WindiaWindows
from pywinauto import keyboard, mouse

def input_hours_for_bill(automationManager : AutomationManager):
    offset = 16
    x = 465
    y = 320
    #click Selbstzahler tab
    automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, 6/9 , 1/8)
    click_distance_from_top_left(465,320,a)
    #Click inside Table
    click_distance_from_top_left(x,y,a)
    y += offset
    keyboard.send_keys("200")

    click_distance_from_top_left(x,y,a)
    y += offset

    click_distance_from_top_left(x,y,a)
    y += offset

    keyboard.send_keys("200")
    click_distance_from_top_left(x,y,a)
    y += offset


    #click Rechnug = Done
    #automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS,3/11 , 9/10)

def click_distance_from_top_left(x : int , y : int , automationManager : AutomationManager): 
    rec = automationManager._get_rec(WindiaWindows.LEISTUNGS_NACHWEIS)

    multiplier = 1 
    if (rec.left < 40):
        multiplier = 1.25 #open on small laptop display
    #
    mouse.click(coords= (int((int(rec.left) + int(x)) * multiplier), int((int(rec.top) + int(y)) *multiplier)))

a = AutomationManager()
a.cur_selected_patient = "Plattner"

input_hours_for_bill(a)
