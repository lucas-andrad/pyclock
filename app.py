import tkinter
from tkinter.ttk import *
from time import strftime


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