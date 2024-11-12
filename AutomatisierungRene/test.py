from pywinauto.application import Application


app = Application(backend="uia").connect(title="WinDIA® AMBULINO GmbH   2024       Systemdatum: 31.10.2024  Benutzer: supervisor", timeout=4)
dialog = app.window(title='WinDIA® AMBULINO GmbH   2024       Systemdatum: 31.10.2024  Benutzer: supervisor')
dialog.print_control_identifiers()

#stamm = dialog.child_window(title="Stamm", control_type="MenuItem").wrapper_object()
#print(dir(stamm))
#stamm.click_input()



#print(dir(closeButton))

def close_windows_on_startup():
    okButton = dialog.child_window(title="OK", auto_id="2", control_type="Button").wrapper_object()
    okButton.click_input()

    closeButton = dialog.child_window(title="Schließen", auto_id="16", control_type="Button").wait('enabled', timeout=5)
    closeButton.click_input()

def open_verordnungen():
    erfassungDropdown = dialog.child_window(title="Erfassung", control_type="MenuItem").wrapper_object()
    #print(dir(erfassungDropdown))
    erfassungDropdown.click_input()
    dialog.erfassungDropdown.wait('ready').menu_select('Verordnungen / Pflegeleistungen')

def input_new_verordnungen(patient):
    #click through list of patients to find the patient
    patientEditBox = dialog.child_window(auto_id="76", control_type="Edit").wrapper_object()
    firstPatientBtn =  dialog.child_window(title="<<", auto_id="30", control_type="Button").wrapper_object()
    nextPatientBtn = dialog.child_window(title=">", auto_id="28", control_type="Button").wrapper_object()
    
    firstPatientBtn.click_input()
    currPatient = patientEditBox.get_value()

    while(not patient in currPatient and not has_reached_end_of_patient_list()):
        #child_window(title="Öffnen", auto_id="DropDown", control_type="Button")
        nextPatientBtn.click_input()
        
        currPatient = patientEditBox.get_value()
        print(currPatient)
       
    if patient in currPatient:
        print("found!")
        print(patient)
    else:
        print("end")

def has_reached_end_of_patient_list():
    lastPatientPopUp = dialog.child_window(title="windia", control_type="Window")
    return lastPatientPopUp.exists()

#close_windows_on_startup()
#input_new_verordnungen("shasjahs")
