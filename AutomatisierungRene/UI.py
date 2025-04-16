from tkinter import *
from tkinter import filedialog, ttk
from ttkthemes import ThemedTk
from windia_manager import WindiaManager
from patient_data_form import Patient, PatientInsuranceInfo
from catalog_data import Catalog

def invoice_ui(root):
  
    studentFrame = LabelFrame(root, text="Student")
    uniFrame = LabelFrame(root, text = "Uni/Schule Abrechnung")
    studentFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    uniFrame.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    
    p1Frame = LabelFrame(root, text="Praxiseinsatz 1")
    p2Frame = LabelFrame(root, text = "Praxiseinsatz 1")
    p1Frame.grid(row=2, column=0, padx=20, pady=20, sticky="w")
    p2Frame.grid(row=3, column=0, padx=20, pady=20, sticky="w")

    name, surname, bday, gender = student_invoice_ui(studentFrame)
    school, wage, max_hours = school_ui(uniFrame)
    start_date1, end_date1, hours1 = praxiseinsatz_ui(p1Frame)
    start_date2, end_date2, hours2 = praxiseinsatz_ui(p2Frame)
    
    sendFrame = Frame(root)
    sendFrame.grid(row=4, column=0, padx=20, pady=20, sticky="w")
    send_button = Button(sendFrame, text="Rechung erstellen starten", background="#5f70b8", foreground="white", command=lambda: clicked([name.get(), surname.get(), bday.get(), gender.get(), school.get(), wage.get(), max_hours.get(), start_date1.get(), end_date1.get(), hours1.get(),start_date2.get(), end_date2.get(), hours2.get() ], 0))
    send_button.grid(row=0, column=0)
    
    
def add_patient_ui(root):
    stammFrame = LabelFrame(root, text="Stamm")
    careFrame = LabelFrame(root, text = "Pflege")
    stammFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    careFrame.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    relativeFrame = LabelFrame(root, text = "Angehörige")
    relativeFrame.grid(row=2, column=0, padx=20, pady=20,  sticky="w")
    
    city, zip, street, name, surname, bday, gender, tel_box = stamm_ui(stammFrame)
    relative_name, relative_surname, relative_tel = relative_ui(relativeFrame)
    doctor1, doctor2, insurance, insurance_number, care_deg, care_deg_date, geldleistung, start_date = care_ui(careFrame)
    
    sendFrame = Frame(root)
    sendFrame.grid(row=4, column=0, padx=20, pady=20, sticky="w")
    send_button = Button(sendFrame, text="Neuer Patient anlegen starten", background="#5f70b8", foreground="white",  command=lambda: clicked([city.get(), zip.get(), street.get() , name.get(), surname.get(), bday.get(), gender.get(),tel_box.get(), relative_name.get(), relative_surname.get(), relative_tel.get(), doctor1.get(), insurance.get(), insurance_number.get(), care_deg.get(), care_deg_date.get(), geldleistung.get(), start_date.get(), doctor2.get()], 1))
    send_button.grid(row=0, column=0)
    
    
    
def care_ui(labelframe):
    doctor1 = ttk.Label(labelframe, text="Hausarzt: ")
    doctor2 = ttk.Label(labelframe, text="Arzt2: ")
    insurance = ttk.Label(labelframe, text="Krankenkasse: ")
    insurance_number = ttk.Label(labelframe, text="Vers.Nr.: ")
    care_deg = ttk.Label(labelframe, text="Pflegegrad: ")
    care_deg_date = ttk.Label(labelframe, text="Seit: ")
    doctor_box1 = ttk.Entry(labelframe)
    doctor_box2= ttk.Entry(labelframe)
    insurance_box = ttk.Entry(labelframe)
    insurance_number_box = ttk.Entry(labelframe)
    care_deg_box = ttk.Entry(labelframe)
    care_deg_date_box = ttk.Entry(labelframe)
    
    doctor1.grid(row=0, column=0)
    doctor2.grid(row=0, column=2)
    doctor_box1.grid(row=0, column=1)
    doctor_box2.grid(row=0, column=3)
    insurance.grid(row=1, column=0)
    insurance_box.grid(row=1, column=1)
    insurance_number.grid(row=1, column=2)
    insurance_number_box.grid(row=1, column=3)
    care_deg.grid(row=2, column=0)
    care_deg_date.grid(row=2, column=2)
    care_deg_box.grid(row=2, column=1)
    care_deg_date_box.grid(row=2, column=3)
    
    geldleistung = IntVar()
    g_radio = Radiobutton(labelframe, text="Geldleistung", variable=geldleistung, value=1, command=lambda: print(geldleistung))
    k_radio = Radiobutton(labelframe, text="Kombileistung", variable=geldleistung , value=0, command=lambda: print(geldleistung))
    g_radio.deselect()
    k_radio.deselect()
    g_radio.select()
    
    date = ttk.Label(labelframe, text="Betreuungsbeginn: ")
    date_box = ttk.Entry(labelframe)
    date.grid(row=3, column=0)
    date_box.grid(row=3, column=1)
    
    
    
    g_radio.grid(row=4, column=0)
    k_radio.grid(row=4, column=1)
    
    return doctor_box1,doctor_box2, insurance_box, insurance_number_box, care_deg_box, care_deg_date_box, geldleistung, date_box
    
    
def stamm_ui(labelframe):
    s_name, s_surname, bday, gender = student_invoice_ui(labelframe)
    city = ttk.Label(labelframe, text="Ort: ")
    zip = ttk.Label(labelframe, text="PLZ: ")
    street = ttk.Label(labelframe, text="Straße: ")
    city_box = ttk.Entry(labelframe)
    zip_box = ttk.Entry(labelframe)
    street_box = ttk.Entry(labelframe)
    
    tel = ttk.Label(labelframe, text="Telephon: ")
    tel_box = ttk.Entry(labelframe)
        
    city.grid(row=4, column=0)
    city_box.grid(row=4, column=1)
    zip.grid(row=5, column=0)
    zip_box.grid(row=5, column=1)
    street.grid(row=6, column=0)
    street_box.grid(row=6, column=1)
    tel.grid(row=7, column=0)
    tel_box.grid(row=7, column=1)
    
    return city_box, zip_box, street_box, s_name, s_surname, bday, gender, tel_box
    
def relative_ui(labelFrame):
    relative_name = ttk.Label(labelFrame, text="Name: ")
    relative_surname =  ttk.Label(labelFrame, text="Vorname: ")
    relative_tel =  ttk.Label(labelFrame, text="Telephon: ")
    
    relative_name_box = ttk.Entry(labelFrame)
    relative_surname_box =  ttk.Entry(labelFrame)
    relative_tel_box =  ttk.Entry(labelFrame)
    
    
    relative_name.grid(row=0, column=0)
    relative_surname.grid(row=1, column=0)
    relative_tel.grid(row=2, column=0)
    
    relative_name_box.grid(row=0, column=1)
    relative_surname_box.grid(row=1, column=1)
    relative_tel_box.grid(row=2, column=1)
    
    return relative_name_box, relative_surname_box, relative_tel_box
    
       
def school_ui(labelframe):
    school = ttk.Label(labelframe, text="Uni/Schule: ")
    school_var = StringVar()
    
    unis = ["Uni Tübingen", "Freiburg"]
    school_var.set(unis[0])
    school_combobox = OptionMenu(labelframe, school_var, *unis)
    school_combobox.grid(row=0, column=1)
    school.grid(row=0, column=0)
    
    wage = ttk.Label(labelframe, text="Stundenlohn: ")
    wage_box = ttk.Entry(labelframe)
    wage.grid(row=1, column=0)
    wage_box.grid(row=1, column=1)
    
    max_hours = ttk.Label(labelframe, text="Max. abrechenbare Stunden: ")
    max_hours_box = ttk.Entry(labelframe)
    max_hours_box.insert(END, "200")
    max_hours.grid(row=2, column=0)
    max_hours_box.grid(row=2, column=1)
    
    return school_var, wage_box, max_hours_box
    
    
def student_invoice_ui(labelframe):
    s_name = ttk.Label(labelframe, text= "Name: ")
    s_name_box = ttk.Entry(labelframe)
    s_surname = ttk.Label(labelframe, text = "Vorname: ")
    s_surname_box = ttk.Entry(labelframe)
    bday = ttk.Label(labelframe, text="Geburtstag")
    bday_box = ttk.Entry(labelframe)
    
    
    s_name.grid(row=0, column=0)
    s_name_box.grid(row=0, column=1)

    s_surname.grid(row=1, column=0)
    s_surname_box.grid(row=1, column=1)

    bday.grid(row=2, column=0)
    bday_box.grid(row=2, column=1)
    
    gender = StringVar()
    w_radio = Radiobutton(labelframe, text="W", variable=gender, value="W", command=lambda: print( gender.get()))
    m_radio = Radiobutton(labelframe, text="M", variable=gender , value="M",  command=lambda: print( gender.get()))
    w_radio.grid(row=3, column=0)
    m_radio.grid(row=3, column=1)
    w_radio.deselect()
    m_radio.deselect()
    w_radio.select()
    
    return s_name_box, s_surname_box, bday_box, gender
    

def praxiseinsatz_ui(labelframe):
    start_date = ttk.Label(labelframe, text="Von: ")
    start_date_box = ttk.Entry(labelframe)
    start_date.grid(row=0, column=0)
    start_date_box.grid(row=0, column=1)
    
    end_date = ttk.Label(labelframe, text="bis: ")
    end_date_box = ttk.Entry(labelframe)
    end_date.grid(row=0, column=2)
    end_date_box.grid(row=0, column=3)
    
    hours = ttk.Label(labelframe, text="Geleistete Stunden: ")
    hours_box = ttk.Entry(labelframe)
    hours.grid(row=1, column=0)
    hours_box.grid(row=1, column=1)
    
    return start_date_box, end_date_box, hours_box
    
def setup():
    root = ThemedTk()
    style(root)
    root.iconbitmap('PflegedienstAutomatisierung/AutomatisierungRene/ambIcon.ico')
    root.title("Windia Automation")
    root.geometry("700x900")
    return root

def main_menu(root):
    menuFrame = Frame(root)
    formFrame = Frame(root)
    menuFrame.grid(row=0, column=0, padx=20, pady=20, sticky="w")
    formFrame.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    invoice_button = ttk.Button(menuFrame, text= "Rechnung", command=lambda: clicked_menu_item(formFrame,0))
    invoice_button.grid(row=0, column=0)
    patient_button = ttk.Button(menuFrame, text= "Neue Patient", command=lambda: clicked_menu_item(formFrame,1))
    patient_button.grid(row=0, column=1)
    
    return menuFrame, formFrame

def clicked_menu_item(frame, number):
    for widget in frame.winfo_children():
        widget.destroy()
    if number == 0:
        invoice_ui(frame)
    if number == 1:
        add_patient_ui(frame)
    
def ui_start(windiaManager : WindiaManager):
    global w_manager 
    w_manager = windiaManager
    root = setup()
    menuFrame, formFrame = main_menu(root)

    root.mainloop()


def radio_button(root):
    r = IntVar()
    Radiobutton(root, text="W", variable=r, value=1, command=lambda: clicked(root, r.get())).pack()
    Radiobutton(root, text="M", variable=r, value=2,  command=lambda: clicked(root, r.get())).pack()
    

def clicked(values, number):
    print ( values)
    if number == 0:
        w_manager.patient_data = Patient(values[0], values[1], values[3], values[2], "", "", "", "","", "","","")
        w_manager.catalog_data = Catalog(values[5], [str(values[7]) + " - " + str(values[8]) , str(values[10]) + " - " + str(values[11])], [str(values[9]), str(values[12])] )
        w_manager.patient_insurance_data = PatientInsuranceInfo("XX", values[4], "", "", "", "", "", "", "", False)
        w_manager.issue_an_invoice()
        
    if number == 1:
        w_manager.patient_data = Patient(values[3], values[4], values[6], values[5], "", values[2], values[1], values[0], values[7], str(values[17]), "", str(values[17]))
        
        
        w_manager.patient_insurance_data = PatientInsuranceInfo(values[13], values[12], values[12], values[14], values[15],values[11],values[18], [values[8],values[9],values[10]], "", values[16] )
        w_manager.add_new_patient()
        
        
        

def open_file_dialog(root):
    root.filename = filedialog.askopenfilename(initialdir="", title="")

def style(root):
    style = ttk.Style(root)
    style.theme_use("ubuntu")

    
    
