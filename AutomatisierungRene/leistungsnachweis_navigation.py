from automation_manager import AutomationManager
from windia_ids import WindiaWindows
from pywinauto import keyboard, mouse

def input_hours_for_bill(automationManager : AutomationManager, max_hours : int):
    offset = 20
    x =  600
    y =  380
    
    #click Selbstzahler tab
    #automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, 6/9 , 1/8)
    click_distance_from_top_left(x,y, automationManager)
    
    keyboard.send_keys(str(max_hours))
    y += offset 
    #Click inside Table
    click_distance_from_top_left(x,y,automationManager)
    y += offset 
    

    click_distance_from_top_left(x,y,automationManager)
    y += offset 
    keyboard.send_keys(str(max_hours))

    click_distance_from_top_left(x,y,automationManager)
    y += offset 

    
    #click_distance_from_top_left( 3/10, 37/100, W.autoManager)


    #click Rechnug = Done
    #automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS,3/11 , 9/10)

def click_distance_from_top_left(x : float , y : float , automationManager : AutomationManager): 
    
    rec = automationManager._get_rec(WindiaWindows.LEISTUNGS_NACHWEIS)
    print(rec)
    x_multiplier = 1
    y_multiplier = 1
    if (rec.left > 800):
        x_multiplier = 0.95
        y_multiplier = 0.81
    #automationManager.click_inside_window(WindiaWindows.LEISTUNGS_NACHWEIS, (x * x_multiplier), (y* y_multiplier))
    w = abs(rec.top - rec.bottom) * y
    mouse.click(coords= ( int((rec.left + x) * x_multiplier) , int((rec.top + y) * y_multiplier)))

