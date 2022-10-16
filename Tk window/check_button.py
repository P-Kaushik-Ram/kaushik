import tkinter as tk
from tkinter import *
##import tkMessageBox


top = tk.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = "Present", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5,  width = 20)
C2 = Checkbutton(top, text = "Absent", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5,  width = 20)
C1.pack()
C2.pack()
top.mainloop()
