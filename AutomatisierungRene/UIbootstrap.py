from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from windia_manager import WindiaManager
from patient_data_form import Patient, PatientInsuranceInfo
from catalog_data import Catalog
import pathlib
from tkinter.filedialog import askdirectory, asksaveasfilename
from tkinter import filedialog
from leistungsnachweis_navigation import *
from local_db import * 

class UImanager():
    windiaManager = None
    root = None
    menuFrame = None
    formFrame = None
    invoice_button = None
    patient_button = None
    ln_button = None
    doctors = []
    insuranses = {}
    
    ln_path = ""
    
    def __init__(self, windiaManager : WindiaManager, doctors, insuranses, base_ln_path):
        self.windiaManager = windiaManager
        
        self.root = tb.Window(themename="superhero")

        self.root.iconbitmap('AutomatisierungRene/ambIcon.ico')
        self.root.title("Windia Automation")
        self.root.geometry("800x1000")
        
        self.doctors = doctors
        self.insuranses = insuranses
        
        self.ln_path = base_ln_path

    ######## Main Menue #####################
    def start(self):
        self.main_menu()
        self.render_invoice()
        print("button: " + str(self.patient_button))
        self.root.mainloop()
        
        

        
    def main_menu(self):
        #scrollbar
        scroll_bar = tb.Scrollbar(self.formFrame, orient="vertical", bootstyle="secondary")
        scroll_bar.grid(row=0, column=4, padx=20, pady=20, sticky="e")

        #canvas = tk.Canvas(self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set)
        
        self.menuFrame = tb.Frame(self.root)
        self.formFrame = tb.Frame(self.root)
        self.menuFrame.grid(row=0, column=0, padx=20, pady=20, sticky="w")
        self.formFrame.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        
        

        #bigger button style:
        big_default_btn_style = tb.Style()
        big_default_btn_style.configure("default.TButton", font=("Helvetica", 16))
        big_red_btn_style = tb.Style()
        big_red_btn_style.configure("danger.TButton", font=("Helvetica", 16))
        
        
        self.invoice_button = tb.Button(self.menuFrame, text= "Rechnung", bootstyle="danger", style="danger.TButton", command=lambda: self.render_invoice())
        self.invoice_button.grid(row=0, column=0 , padx=20)
        self.patient_button = tb.Button(self.menuFrame, text= "Neuer Patient", bootstyle="default", style="default.TButton", command=lambda: self.render_new_patient_form() )
        self.patient_button.grid(row=0, column=1 , padx=20)
        self.ln_button = tb.Button(self.menuFrame, text= "Leistungsnachweise", bootstyle="default", style="default.TButton", command=lambda: self.render_ln())
        self.ln_button.grid(row=0, column=2 , padx=20)
        
    ######## LeistungsNachweise #####################   
    def render_ln(self):
        self.clear_frame(self.formFrame)
        self.ln_button.configure(bootstyle="danger", style="danger.TButton")
        self.patient_button.configure(bootstyle="default", style="default.TButton")
        self.invoice_button.configure(bootstyle="default" , style="default.TButton")
        
        pathEntryFrame = tb.Frame(self.formFrame)
        pathShowFrame = tb.Frame(self.formFrame)
        month_frame = tb.Frame(self.formFrame)
        dataFrame = tb.Labelframe(self.formFrame, text = "Patient / LN")
        bar = tb.Scrollbar(dataFrame, orient='vertical')
        sendFrame = tb.Frame(self.formFrame)
        
        pathEntryFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        pathShowFrame.grid(row=1, column=0, padx=20, pady=20, sticky="nw")
        month_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nw")
        sendFrame.grid(row=3, column=0, padx=20, pady=20, sticky="w")
        dataFrame.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        
        
        month = tb.Label(month_frame, text= "Monat: ")
        month_box = tb.Entry(month_frame)
        month.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        month_box.grid(row=0, column=1, padx=20, pady=20, sticky="nw")
        
        tb.Label(pathEntryFrame, text='Leistungsnachweise Zettel auswählen: ').grid(row=0, column=0, padx=10, pady=2, sticky='ew')
        curr_path = tb.Label(pathShowFrame, text=f'Ausgewählte Datei: {self.ln_path}')
        curr_path.grid(row=0, column=0, padx=10, pady=2, sticky='ew')

        button = tb.Button(pathEntryFrame, text='Word Datei wählen', command=lambda: self.on_browse(curr_path, dataFrame), style='primary.TButton')
        button.grid(row=0, column=2, sticky='ew', pady=2, ipadx=10)
        
        
        #month_box.grid(row=1, column=1, padx=20, pady=20, sticky="w")
        send_button = tb.Button(sendFrame, text="Leistungsnachweise drucken starten", style='Outline.TButton' , command=lambda: self.start_printing_ln(month_box.get()))
        send_button.grid(row=0, column=0)

    
    def on_browse(self, curr_path, dataFrame):
        filepath = filedialog.askopenfilename()
        self.ln_path = filepath
        curr_path.configure(text= f'Ausgewählte Datei: {self.ln_path}')
        try:
            res = read_VE_fromdocx_file(filepath)
            self.create_table(dataFrame, res)
        except:
            curr_path.configure(text= f'ERROR datei konnte nicht gelesen werden!', bootstyle="danger")
      
    def create_table(self, frame, data):
        i = 0
        for patient, ln_type in data.items():
              tb.Label(frame, text=str(patient)).grid(row=i, column=0, padx=10, pady=2, sticky='ew')
              tb.Label(frame, text=str(ln_type)).grid(row=i, column=1, padx=10, pady=2, sticky='ew')
              i +=1
              
    def start_printing_ln(self, month):
        if self.ln_path:
            self.windiaManager.print_lns(self.ln_path, month)

        
        
        
    ######## Invoice #####################
    def render_invoice(self):
        self.clear_frame(self.formFrame)
        self.invoice_button.configure(bootstyle="danger", style="danger.TButton")
        self.patient_button.configure(bootstyle="default", style="default.TButton")
        self.ln_button.configure(bootstyle="default", style="default.TButton")

        studentFrame = tb.Labelframe(self.formFrame, text="Student")
        uniFrame = tb.Labelframe(self.formFrame, text = "Uni/Schule Abrechnung")
        studentFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")
        uniFrame.grid(row=1, column=0, padx=20, pady=20, sticky="w")
        
        p1Frame = tb.Labelframe(self.formFrame, text="Praxiseinsatz 1")
        p2Frame = tb.Labelframe(self.formFrame, text = "Praxiseinsatz 2")
        p1Frame.grid(row=2, column=0, padx=20, pady=20, sticky="w")
        p2Frame.grid(row=3, column=0, padx=20, pady=20, sticky="w")

        name, surname, bday, gender = self.student_invoice_ui(studentFrame)
        
        school, wage, max_hours = self.school_ui(uniFrame)
        start_date1, end_date1, hours1 = self.praxiseinsatz_ui(p1Frame)
        start_date2, end_date2, hours2 = self.praxiseinsatz_ui(p2Frame)
        
        sendFrame = tb.Frame(self.formFrame)
        sendFrame.grid(row=4, column=0, padx=20, pady=20, sticky="w")
        send_button = tb.Button(sendFrame, text="Rechung erstellen starten", style='Outline.TButton' , command=lambda: self.start_invoice([name.get(), surname.get(), bday.entry.get().replace("/", "."), gender.get(), school.get(), wage.get(), max_hours.get(), start_date1.entry.get().replace("/", "."), end_date1.entry.get().replace("/", "."), hours1.get(),start_date2.entry.get().replace("/", "."), end_date2.entry.get().replace("/", "."), hours2.get() ], max_hours.get()))
        send_button.grid(row=0, column=0)
            
    
    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
    def student_invoice_ui(self, labelframe):
        s_name = tb.Label(labelframe, text= "Name: ")
        s_name_box = tb.Entry(labelframe)
        s_surname = tb.Label(labelframe, text = "Vorname: ")
        s_surname_box = tb.Entry(labelframe)
        bday = tb.Label(labelframe, text="Geburtstag")
        bday_box = tb.DateEntry(labelframe, bootstyle="default")
        
        
        s_name.grid(row=0, column=0, pady=10)
        s_name_box.grid(row=0, column=1, pady=10)

        s_surname.grid(row=1, column=0, pady=10)
        s_surname_box.grid(row=1, column=1, pady=10)

        bday.grid(row=2, column=0, pady=10)
        bday_box.grid(row=2, column=1, pady=10)
        
        gender = tb.StringVar()
        w_radio = tb.Radiobutton(labelframe, text="W", variable=gender, value="W", command=lambda: print( gender.get()))
        m_radio = tb.Radiobutton(labelframe, text="M", variable=gender , value="M",  command=lambda: print( gender.get()))
        w_radio.grid(row=3, column=0, pady=10)
        m_radio.grid(row=3, column=1, pady=10)

        
        return s_name_box, s_surname_box, bday_box, gender

    def school_ui(self, labelframe):
        school = tb.Label(labelframe, text="Uni/Schule: ")
        school_var = tb.StringVar()
        
        unis = ["Universitätsklinikum Tübingen", "Winterhaldenschule"]
        #school_var.set(unis[0])
        school_combobox = tb.OptionMenu(labelframe, school_var,unis[0], *unis)
        school_combobox.grid(row=0, column=1)
        school.grid(row=0, column=0)
        
        wage = tb.Label(labelframe, text="Stundenlohn: ")
        wage_box = tb.Entry(labelframe)
        wage.grid(row=1, column=0)
        wage_box.grid(row=1, column=1)
        
        max_hours = tb.Label(labelframe, text="Max. abrechenbare Stunden: ")
        max_hours_box = tb.Entry(labelframe)
        max_hours_box.insert(END, "200")
        max_hours.grid(row=2, column=0)
        max_hours_box.grid(row=2, column=1)
        
        return school_var, wage_box, max_hours_box
    
    def praxiseinsatz_ui(self, labelframe):
        
        start_date = tb.Label(labelframe, text="Von: ")
        start_date_box = tb.DateEntry(labelframe, bootstyle="default")
        start_date.grid(row=0, column=0 , padx=10, pady=10)
        start_date_box.grid(row=0, column=1, padx=10, pady=10)
        
        end_date = tb.Label(labelframe, text="bis: ")
        end_date_box =  tb.DateEntry(labelframe, bootstyle="default")
        end_date.grid(row=0, column=2, padx=10, pady=10)
        end_date_box.grid(row=0, column=3, padx=10,  pady=10)
    
        hours = tb.Label(labelframe, text="Geleistete Stunden: ")
        hours_box = tb.Entry(labelframe)
        hours.grid(row=1, column=0, padx=10, pady=10)
        hours_box.grid(row=1, column=1, padx=10, pady=10)
        
        return start_date_box, end_date_box, hours_box
    
    def start_invoice(self, values, max_hours):
        print (values)
        
        print("making an invoice....")
        self.windiaManager.patient_data = Patient(values[0], values[1], values[3], values[2], "", "", "", "","", "15.01.2025","","")
        self.windiaManager.catalog_data = Catalog(values[5], [str(values[7]) + " - " + str(values[8]) , str(values[10]) + " - " + str(values[11])], [str(values[9]), str(values[12])] )
        self.windiaManager.patient_insurance_data = PatientInsuranceInfo("XX", values[4], "", "", "", "", "", "", "", False)
        self.windiaManager.insert_invoice_data(values[4])
        self.windiaManager.issue_an_invoice(max_hours)
        
    
    ######## New Patient #####################
    def render_new_patient_form(self):
        self.clear_frame(self.formFrame)

        self.invoice_button.configure(bootstyle="default", style="default.TButton")
        self.ln_button.configure(bootstyle="default", style="default.TButton")
        self.patient_button.configure(bootstyle="danger", style="danger.TButton")
        
        

        stammFrame = tb.Labelframe(self.formFrame, text="Stamm")
        careFrame = tb.Labelframe(self.formFrame, text = "Pflege")
        stammFrame.grid(row=0, column=0, padx=20, pady=10, sticky="nw")
        careFrame.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        relativeFrame = tb.Labelframe(self.formFrame, text = "Angehörige")
        relativeFrame.grid(row=0, column=1, padx=10, pady=10,  sticky="nw")
        
        city, zip, street, name, surname, bday, gender, tel_box = self.stamm_ui(stammFrame)
        relative_name, relative_surname, relative_tel = self.relative_ui(relativeFrame)
        doctor1, doctor2, insurance, insurance_number, care_deg, care_deg_date, geldleistung, start_date, new_doc_name, new_doc_address = self.care_ui(careFrame)
        print("d1: " + str(doctor1))
        print("d2:" + str(doctor2))
        print("i" + str(insurance))
        sendFrame = tb.Frame(self.formFrame)
        sendFrame.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        send_button = tb.Button(sendFrame, text="Neuer Patient anlegen starten",  style='Outline.TButton' ,  command=lambda: self.start_new_patient([city.get(), zip.get(), street.get() , name.get(), surname.get(), bday.entry.get().replace("/", "."), gender.get(),tel_box.get(), relative_name.get(), relative_surname.get(), relative_tel.get(), doctor1.get(), insurance.get(), insurance_number.get(), care_deg.get(), care_deg_date.get(), geldleistung.get(), start_date.get(), doctor2.get()], [new_doc_name.get(), new_doc_address.get()]))
        send_button.grid(row=0, column=0)
        
    def stamm_ui(self, labelframe):
        s_name, s_surname, bday, gender = self.student_invoice_ui(labelframe)
        city = tb.Label(labelframe, text="Ort: ")
        zip = tb.Label(labelframe, text="PLZ: ")
        street = tb.Label(labelframe, text="Straße: ")
        city_box = tb.Entry(labelframe)
        zip_box = tb.Entry(labelframe)
        street_box = tb.Entry(labelframe)
        
        tel = tb.Label(labelframe, text="Telephon: ")
        tel_box = tb.Entry(labelframe)
            
        city.grid(row=4, column=0, pady=10)
        city_box.grid(row=4, column=1, pady=10)
        zip.grid(row=5, column=0, pady=10)
        zip_box.grid(row=5, column=1, pady=10)
        street.grid(row=6, column=0, pady=10)
        street_box.grid(row=6, column=1, pady=10)
        tel.grid(row=7, column=0, pady=10)
        tel_box.grid(row=7, column=1, pady=10)
        
        return city_box, zip_box, street_box, s_name, s_surname, bday, gender, tel_box

    def relative_ui(self, labelFrame):
        relative_name = tb.Label(labelFrame, text="Name: ")
        relative_surname =  tb.Label(labelFrame, text="Vorname: ")
        relative_tel =  tb.Label(labelFrame, text="Telephon: ")
        
        relative_name_box = tb.Entry(labelFrame)
        relative_surname_box =  tb.Entry(labelFrame)
        relative_tel_box =  tb.Entry(labelFrame)
        
        
        relative_name.grid(row=0, column=0)
        relative_surname.grid(row=1, column=0)
        relative_tel.grid(row=2, column=0)
        
        relative_name_box.grid(row=0, column=1)
        relative_surname_box.grid(row=1, column=1)
        relative_tel_box.grid(row=2, column=1)
        
        return relative_name_box, relative_surname_box, relative_tel_box
    
    
    def care_ui(self,labelframe):
        
        doctor1_var = tb.StringVar()
        doctor2_var = tb.StringVar()
        insurance_var = tb.StringVar()
        
        doc1_combobox = tb.OptionMenu(labelframe, doctor1_var,self.doctors[0], *self.doctors, bootstyle="secondary")
        doc2_combobox = tb.OptionMenu(labelframe, doctor2_var,self.doctors[0], *self.doctors, bootstyle="secondary")
        insurance_combobox = tb.OptionMenu(labelframe, insurance_var,list(self.insuranses.keys())[0], *list(self.insuranses.keys()) , bootstyle="secondary")

        new_doc_name = tb.Label(labelframe, text="neuer Arzt-Name: " , bootstyle = "secondary")
        new_doc_address = tb.Label(labelframe, text="neuer Arzt-Ort: " , bootstyle = "secondary")
        new_doc_name_box = tb.Entry(labelframe)
        new_doc_address_box = tb.Entry(labelframe)


        doctor1 = tb.Label(labelframe, text="Hausarzt: ")
        doctor2 = tb.Label(labelframe, text="Arzt2: ")
        insurance = tb.Label(labelframe, text="Krankenkasse: ")
        insurance_number = tb.Label(labelframe, text="Vers.Nr.: ")
        care_deg = tb.Label(labelframe, text="Pflegegrad: ")
        care_deg_date = tb.Label(labelframe, text="Seit: ")
  
  
        insurance_number_box = tb.Entry(labelframe)
        care_deg_box = tb.Entry(labelframe)
        care_deg_date_box = tb.Entry(labelframe)
        
        doctor1.grid(row=0, column=0 , pady=10)
        doctor2.grid(row=0, column=2, pady=10)
        doc1_combobox.grid(row=0, column=1, pady=10)
        doc2_combobox.grid(row=0, column=3, pady=10)

        new_doc_name.grid(row=1, column=0, pady=10)
        new_doc_name_box.grid(row=1, column=1, pady=10)
        new_doc_address.grid(row=1, column=2, pady=10)
        new_doc_address_box.grid(row=1, column=3, pady=10)

        insurance.grid(row=2, column=0, pady=10)
        insurance_combobox.grid(row=2, column=1, pady=10)
        insurance_number.grid(row=2, column=2, pady=10)
        insurance_number_box.grid(row=2, column=3, pady=10)
        care_deg.grid(row=3, column=0, pady=10)
        care_deg_date.grid(row=3, column=2, pady=10)
        care_deg_box.grid(row=3, column=1, pady=10)
        care_deg_date_box.grid(row=3, column=3, pady=10)
        
        geldleistung = IntVar()
        g_radio = tb.Radiobutton(labelframe, text="Geldleistung", variable=geldleistung, value=1, command=lambda: print(geldleistung))
        k_radio = tb.Radiobutton(labelframe, text="Kombileistung", variable=geldleistung , value=0, command=lambda: print(geldleistung))
  
        
        date = tb.Label(labelframe, text="Betreuungsbeginn: ")
        date_box = tb.Entry(labelframe)
        date.grid(row=4, column=0, pady=10)
        date_box.grid(row=4, column=1, pady=10)
        
        
        
        g_radio.grid(row=5, column=0, pady=10)
        k_radio.grid(row=5, column=1, pady=10)
        
        return doctor1_var,doctor2_var, insurance_var, insurance_number_box, care_deg_box, care_deg_date_box, geldleistung, date_box, new_doc_name_box, new_doc_address_box
    
    def start_new_patient(self, values, new_doc):
        print("adding patient...." + str(new_doc))
        self.windiaManager.patient_data = Patient(values[3], values[4], values[6], values[5], "", values[2], values[1], values[0], values[7], str(values[17]), "", str(values[17]))
        
        
        self.windiaManager.patient_insurance_data = None
        self.windiaManager.patient_insurance_data = PatientInsuranceInfo(values[13], values[12], values[12], values[14], values[15],values[11],values[18], [values[8],values[9],values[10]], "", values[16] )
        
        if new_doc[0]:
            print("new")
            self.windiaManager.add_new_patient(new_doc=[new_doc[0], new_doc[1]])
        else: self.windiaManager.add_new_patient()
    
    
#doctors_list_path = "PflegedienstAutomatisierung/AutomatisierungRene/doctors.txt"
#insurance_list_path = "PflegedienstAutomatisierung/AutomatisierungRene/both_insurances.txt"
#base_ln_path = "Hello"
#dm = localDataManager(doctors_list_path,insurance_list_path)
#W = WindiaManager()
#ui = UImanager(W, "","" , base_ln_path)
#ui.start()