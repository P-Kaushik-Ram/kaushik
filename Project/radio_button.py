import tkinter as tk
from tkinter import *

def sel():
   selection = "You Marked as  " + str(var.get())
   label.config(text = selection)

root = tk.Tk()
var = IntVar()
R1 = Radiobutton(root, text="Present", variable=var, value=1,command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Absent", variable=var, value=2,command=sel)
R2.pack( anchor = W )


label = Label(root)
label.pack()
root.mainloop()
