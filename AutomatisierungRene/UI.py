from tkinter import *
from tkinter import filedialog

def invoice_ui(root):
    studentFrame = LabelFrame(root, text="Student")
    uniFrame = LabelFrame(root, text = "Uni/Schule")
    studentFrame.grid(row=0, column=0, padx=20, pady=20)
    uniFrame.grid(row=1, column=0, padx=20, pady=20)

    s_name = Label(studentFrame, text= "Name: ")
    s_name_box = Entry(studentFrame, bd = 5)
    s_surname = Label(studentFrame, text = "Vorname: ")
    s_surname_box = Entry(studentFrame, bd = 5)
    bday = Label(studentFrame, text="Geburtstag")
    gender = StringVar()
    w_radio = Radiobutton(studentFrame, text="W", variable=gender, value="W", command=lambda: clicked(root, gender.get()))
    m_radio = Radiobutton(studentFrame, text="M", variable=gender , value="M",  command=lambda: clicked(root, gender.get()))
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

    school = Label(uniFrame, text="Uni/Schule: ")
    school_var = StringVar()
    unis = ["Uni Tübingen", "Freiburg"]
    school_combobox = OptionMenu(uniFrame, school_var,unis[0], *unis)
    school_combobox.grid(row=3, column=3)

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
    

def clicked(root, val):
    print(val)
    #myLabel = Label(root, text=str(val))
    #myLabel.pack()

def open_file_dialog(root):
    root.filename = filedialog.askopenfilename(initialdir="", title="")

ui_start()