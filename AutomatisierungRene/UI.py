from tkinter import *
from tkinter import filedialog, ttk
from ttkthemes import ThemedTk

def invoice_ui(root):
  
    studentFrame = LabelFrame(root, text="Student")
    uniFrame = LabelFrame(root, text = "Uni/Schule")
    studentFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    uniFrame.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    
    p1Frame = LabelFrame(root, text="Praxiseinsatz 1")
    p2Frame = LabelFrame(root, text = "Praxiseinsatz 1")
    p1Frame.grid(row=2, column=0, padx=20, pady=20, sticky="w")
    p2Frame.grid(row=3, column=0, padx=20, pady=20, sticky="w")

    student_invoice_ui(studentFrame)
    school_ui(uniFrame)
    praxiseinsatz_ui(p1Frame)
    praxiseinsatz_ui(p2Frame)
    
    sendFrame = Frame(root)
    sendFrame.grid(row=4, column=0, padx=20, pady=20, sticky="w")
    send_button = Button(sendFrame, text="Rechung erstellen starten", background="#5f70b8", foreground="white")
    send_button.grid(row=0, column=0)
    
    
def add_patient_ui(root):
    stammFrame = LabelFrame(root, text="Stamm")
    careFrame = LabelFrame(root, text = "Pflege")
    stammFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
    careFrame.grid(row=1, column=0, padx=20, pady=20, sticky="w")
    relativeFrame = LabelFrame(root, text = "Angehörige")
    relativeFrame.grid(row=2, column=0, padx=20, pady=20,  sticky="w")
    stamm_ui(stammFrame)
    relative_ui(relativeFrame)
    care_ui(careFrame)
    
    sendFrame = Frame(root)
    sendFrame.grid(row=4, column=0, padx=20, pady=20, sticky="w")
    send_button = Button(sendFrame, text="Neuer Patient anlegen starten", background="#5f70b8", foreground="white")
    send_button.grid(row=0, column=0)
    
def care_ui(labelframe):
    doctor = ttk.Label(labelframe, text="Hausarzt: ")
    insurance = ttk.Label(labelframe, text="Krankenkasse: ")
    insurance_number = ttk.Label(labelframe, text="Vers.Nr.: ")
    care_deg = ttk.Label(labelframe, text="Pflegegrad: ")
    care_deg_date = ttk.Label(labelframe, text="Seit: ")
    doctor_box = ttk.Entry(labelframe)
    insurance_box = ttk.Entry(labelframe)
    insurance_number_box = ttk.Entry(labelframe)
    care_deg_box = ttk.Entry(labelframe)
    care_deg_date_box = ttk.Entry(labelframe)
    
    doctor.grid(row=0, column=0)
    doctor_box.grid(row=0, column=1)
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
    
    
    
    g_radio.grid(row=3, column=0)
    k_radio.grid(row=3, column=1)
    
    
def stamm_ui(labelframe):
    student_invoice_ui(labelframe)
    city = ttk.Label(labelframe, text="Ort: ")
    zip = ttk.Label(labelframe, text="PLZ: ")
    street = ttk.Label(labelframe, text="Straße: ")
    city_box = ttk.Entry(labelframe)
    zip_box = ttk.Entry(labelframe)
    street_box = ttk.Entry(labelframe)
    
    city.grid(row=4, column=0)
    city_box.grid(row=4, column=1)
    zip.grid(row=5, column=0)
    zip_box.grid(row=5, column=1)
    street.grid(row=6, column=0)
    street_box.grid(row=6, column=1)
    
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
    w_radio = Radiobutton(labelframe, text="W", variable=gender, value="W", command=lambda: clicked( gender.get()))
    m_radio = Radiobutton(labelframe, text="M", variable=gender , value="M",  command=lambda: clicked( gender.get()))
    w_radio.grid(row=3, column=0)
    m_radio.grid(row=3, column=1)
    w_radio.deselect()
    m_radio.deselect()
    w_radio.select()
    

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
    
def setup():
    root = ThemedTk()
    style(root)
    root.iconbitmap('PflegedienstAutomatisierung/AutomatisierungRene/ambIcon.ico')
    #PflegedienstAutomatisierung\AutomatisierungRene\ambIcon.ico
    root.title("Windia Automation")
    root.geometry("500x700")
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
    
def ui_start():
    root = setup()
    #radio_button(root)
    #invoice_ui(root)
    menuFrame, formFrame = main_menu(root)
    #add_patient_ui(root)
    root.mainloop()


def radio_button(root):
    r = IntVar()
    Radiobutton(root, text="W", variable=r, value=1, command=lambda: clicked(root, r.get())).pack()
    Radiobutton(root, text="M", variable=r, value=2,  command=lambda: clicked(root, r.get())).pack()
    

def clicked(val):
    print(val)
    #myLabel = ttk.Label(root, text=str(val))
    #myLabel.pack()

def open_file_dialog(root):
    root.filename = filedialog.askopenfilename(initialdir="", title="")

def style(root):
    style = ttk.Style(root)
    style.theme_use("ubuntu")
    #style.configure("ttk.Label", foreground="black", background="blue")
    #style.configure("BW.TLabel", foreground="black", background="white")
    #print(root.get_themes())
    #yaru, breeze
    
    
ui_start()