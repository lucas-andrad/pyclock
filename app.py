import tkinter
from time import strftime
from tkinter.ttk import *


root = tkinter.Tk()
root.title("PyClock")

def clock():
    hour = strftime("%H:%M:%S")
    label.config(text=hour)
    label.after(1000, clock)

label = Label(root, font=("Helvetica", 60), background="#000", foreground="#00FF04")
label.pack(anchor="center")

clock()

tkinter.mainloop()