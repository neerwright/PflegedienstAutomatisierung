from tkinter import *
from tkinter import filedialog

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

def school_ui(labelframe):
    school = Label(labelframe, text="Uni/Schule: ")
    school_var = StringVar()
    
    unis = ["Uni Tübingen", "Freiburg"]
    school_var.set(unis[0])
    school_combobox = OptionMenu(labelframe, school_var, *unis)
    school_combobox.grid(row=0, column=1)
    school.grid(row=0, column=0)
    
    wage = Label(labelframe, text="Stundenlohn: ")
    wage_box = Entry(labelframe, bd = 5)
    wage.grid(row=1, column=0)
    wage_box.grid(row=1, column=1)
    
    max_hours = Label(labelframe, text="Max. abrechenbare Stunden: ")
    max_hours_box = Entry(labelframe, bd = 5)
    max_hours_box.insert(END, "200")
    max_hours.grid(row=2, column=0)
    max_hours_box.grid(row=2, column=1)
    
    
def student_invoice_ui(labelframe):
    s_name = Label(labelframe, text= "Name: ")
    s_name_box = Entry(labelframe, bd = 5)
    s_surname = Label(labelframe, text = "Vorname: ")
    s_surname_box = Entry(labelframe, bd = 5)
    bday = Label(labelframe, text="Geburtstag")
    gender = StringVar()
    w_radio = Radiobutton(labelframe, text="W", variable=gender, value="W", command=lambda: clicked( gender.get()))
    m_radio = Radiobutton(labelframe, text="M", variable=gender , value="M",  command=lambda: clicked( gender.get()))
    w_radio.deselect()
    m_radio.deselect()
    w_radio.select()
    
    s_name.grid(row=0, column=0)
    s_name_box.grid(row=0, column=1)

    s_surname.grid(row=1, column=0)
    s_surname_box.grid(row=1, column=1)

    bday.grid(row=2, column=0)
    w_radio.grid(row=2, column=1)
    m_radio.grid(row=2, column=2)
    

def praxiseinsatz_ui(labelframe):
    start_date = Label(labelframe, text="Von: ")
    start_date_box = Entry(labelframe, bd = 5)
    start_date.grid(row=0, column=0)
    start_date_box.grid(row=0, column=1)
    
    end_date = Label(labelframe, text="bis: ")
    end_date_box = Entry(labelframe, bd = 5)
    end_date.grid(row=0, column=2)
    end_date_box.grid(row=0, column=3)
    
    hours = Label(labelframe, text="Geleistete Stunden: ")
    hours_box = Entry(labelframe, bd = 5)
    hours.grid(row=1, column=0)
    hours_box.grid(row=1, column=1)
    
def setup():
    root = Tk()
    root.title("WindiaAutomation")
    #root.iconbitmap("")
    root.geometry("500x500")

    return root



def create_frame(root ):
    frame = LabelFrame(root)
    
def ui_start():
    root = setup()
    #radio_button(root)
    invoice_ui(root)
    root.mainloop()


def radio_button(root):
    r = IntVar()
    Radiobutton(root, text="W", variable=r, value=1, command=lambda: clicked(root, r.get())).pack()
    Radiobutton(root, text="M", variable=r, value=2,  command=lambda: clicked(root, r.get())).pack()
    

def clicked(val):
    print(val)
    #myLabel = Label(root, text=str(val))
    #myLabel.pack()

def open_file_dialog(root):
    root.filename = filedialog.askopenfilename(initialdir="", title="")

ui_start()