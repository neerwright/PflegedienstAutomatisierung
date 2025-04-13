from tkinter import *

def invoice_ui():
    pass

def setup():
    root = Tk()
    root.title("WindiaAutomation")
    #root.iconbitmap("")
    return root
    
def create_frame(root, ):
    frame = LabelFrame(root)
    
def ui_start():
    root = setup()
    radio_button(root)
    root.mainloop()

def radio_button(root):
    r = IntVar()
    Radiobutton(root, text="W", variable=r, value=1, command=lambda: clicked(root, r.get())).pack()
    Radiobutton(root, text="M", variable=r, value=2,  command=lambda: clicked(root, r.get())).pack()
    

def clicked(root, val):
    print(val)
    myLabel = Label(root, text=str(val))
    myLabel.pack()


ui_start()