from pywinauto.application import Application
from pywinauto import findwindows
from pywinauto import Desktop
import csv
import pywinauto.mouse as mouse
from pywinauto import keyboard
windows = Desktop(backend="uia").windows()
import time
#print([w.window_text() for w in windows])
#print (findwindows.find_windows(title_re=".*DIA*"))

def setup_empleyee_window():
    app = Application(backend="uia").connect(title="WinDIA®  -  Stammdaten für Mitarbeiter", timeout=4)
    dialog = app.window(title='WinDIA®  -  Stammdaten für Mitarbeiter')
    return dialog

#------------------------
dialog = setup_empleyee_window()

#key = dialog.child_window(auto_id="100", control_type="Edit").wrapper_object()
#
#
#
#
#fax = dialog.child_window(auto_id="85", control_type="Edit").wrapper_object()

#
#Dienst = dialog.child_window(auto_id="91", control_type="Edit").wrapper_object()

#ort = dialog.child_window(auto_id="92", control_type="Edit").wrapper_object()

#

#

#
#IBAN = dialog.child_window(auto_id="22", control_type="Edit").wrapper_object()
#Inhaber = dialog.child_window(auto_id="21", control_type="Edit").wrapper_object()
#gehalt = dialog.child_window(auto_id="13", control_type="Edit").wrapper_object()
#ueberstunden = dialog.child_window(auto_id="8", control_type="Edit").wrapper_object()


#-----------------------

def read_csv_to_list(file_name, row_start, row_end):
    with open(file_name, newline='') as csvfile:
        csv_table = csv.reader(csvfile, delimiter=';', quotechar='|')
        new_list = []
        for row in csv_table:
            
            if not ("" in list(row)):
                new_list.append(list(row))
                       #print(list(row))
        #new_list = new_list[row_start:row_end]
    #print(MitarbeiterListe)
    return new_list[1:]



def add_employee(employee):
    #Qualification

    #mouse.click(coords=(540, 320))
    #eing_als =
    #if (eing_als == "") :
    #    mouse.move(coords=(540, 340))
    
    #quali = dialog.child_window(title="Öffnen", auto_id="DropDown", control_type="Button").wrapper_object()
    #print(dialog.ÖffnenButton9.menu())


    #open Mitarbeiter window
    #Log into Mitarbeiter Window
#select pflegend
    #print_info(dialog)
    #active = dialog.child_window(title="pflegend tätig", auto_id="33", control_type="CheckBox")
    #active.click_input()
    #ArbeitsZeit reiter

    mouse.click(coords=(450, 260))
    
    
    #print_info(dialog)
    #print_info(dialog)
    #get exel table data 
    #check if employee already exists

    #DATA
    p_nr = employee[0]
    nachname = employee[1]
    vorname = employee[2]
    lb_nr = employee[3]
    hdz = employee[4]
    eing_als = employee[5]
    eintrittsdatum = employee[6]
    geb_datum = employee[7]
    tele = employee[8]
    handy = employee[9]
    email = employee[10]
    strase = employee[11]
    plz = employee[12]
    ort = employee[13]
    #print(p_nr, nachname, eintrittsdatum, email, plz, ort)
     
    #select New
    
    #print(dir(quali))
    #coords = quali.rectangle().mid_point()

    mouse.click(coords=(142, 180))
    
    time.sleep(1)
    #gültig
    mouse.double_click(coords=(470, 340))
    keyboard.send_keys(eintrittsdatum )
    keyboard.send_keys( "{ENTER}")
    time.sleep(0.3)
    #Anrede
    mouse.click(coords=(230, 370)) 
    time.sleep(0.1)
    mouse.click(coords=(230, 470))

    #iput Names and Adress and HZ
    time.sleep(0.5)

    name_field = dialog.child_window(auto_id="104", control_type="Edit").wrapper_object()
    name_field.set_text(nachname)
    vorname_field = dialog.child_window(auto_id="107", control_type="Edit").wrapper_object()
    vorname_field.set_text(vorname)
    
    hz = dialog.child_window(auto_id="99", control_type="Edit").wrapper_object()
    hz.set_text(hdz)
    short_name = dialog.child_window(auto_id="106", control_type="Edit").wrapper_object()
    short_name.set_text(hdz)

    birthday = dialog.child_window(auto_id="97", control_type="Edit").wrapper_object()
    birthday.set_text(geb_datum)

    per_nr = dialog.child_window(auto_id="101", control_type="Edit").wrapper_object()
    per_nr.set_text(p_nr)


    # ADRESSE
    street = dialog.child_window(auto_id="86", control_type="Edit").wrapper_object()
    street.set_text(strase)

    privat = dialog.child_window(auto_id="90", control_type="Edit").wrapper_object()
    privat.set_text(tele)
    mobil = dialog.child_window(auto_id="89", control_type="Edit").wrapper_object()
    mobil.set_text(handy)
    mail = dialog.child_window(auto_id="88", control_type="Edit").wrapper_object()
    mail.set_text(email)

    #Qualification


    #LBNR
    mouse.click(coords=(620, 260))

    #mouse.click(coords=(500, 260))
    LBNR = dialog.child_window(auto_id="26", control_type="Edit").wrapper_object()
    LBNR.set_text((lb_nr))

#   select pflegend
    pflegend_tätig = dialog.child_window(title="pflegend tätig", auto_id="33", control_type="CheckBox").wrapper_object()
    pflegend_tätig.click_input()
    
    #SAVE
    mouse.click(coords=(320, 190))
    time.sleep(1)

    

def check_if_emp_exists():
    pass


def setup_winDia():
    app = Application(backend="uia").connect(title="WinDIA® AMBULINO GmbH   2024       Systemdatum: 07.11.2024  Benutzer: supervisor", timeout=4)
    dialog = app.window(title='WinDIA® AMBULINO GmbH   2024       Systemdatum: 07.11.2024  Benutzer: supervisor')
    return dialog



def print_info(dialog):
    dialog.print_control_identifiers()

#d = setup_winDia()
employees = read_csv_to_list('MitarbeiterEnde2.csv', 1, 15)
print(employees)
for emp in employees:
    add_employee(emp)

#menue = d.child_window(title="Systemmenü", auto_id="MenuBar", control_type="MenuBar").wrapper_object()
#print(dir(menue))
#menue.click_input()
#print_info(d)
# child_window(title="Systemmenü", control_type="MenuItem")
# child_window(title="Systemmenü", auto_id="MenuBar", control_type="MenuBar")

 