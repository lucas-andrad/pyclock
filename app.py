import tkinter
from tkinter.ttk import *
from time import strftime

root = tkinter.Tk()
root.title("PyClock")

def clock():
    hour = strftime("%H:%M:%S")
    label.config(text=hour)
    label.after(1000, hour)