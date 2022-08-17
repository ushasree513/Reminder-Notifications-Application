from email import message
import time
from tkinter import *
from win10toast import *

root = Tk()
root.geometry("800x400")
l1 = Label(root,font=('Bold',30))
name_entry = Entry(root, width=30)
name_entry.pack()
name_entry.insert(0,"What you want me to remind you?")
Time_Enter = Entry(root,width=30)
Time_Enter.pack()
Time_Enter.insert(0,"Enter Time in Minutes")

def Display():
    Text_Input = name_entry.get()
    GetTime = int(Time_Enter.get())
    GetTime = GetTime * 60
    time.sleep(GetTime)
    l1.config(text=Text_Input)
    l1.pack()
    hr = ToastNotifier()
    hr.show_toast("remind",Text_Input)

Display_Label = Button(root,text="Click to Program it",font=('Normal',20),command=Display).pack()
root.mainloop()
