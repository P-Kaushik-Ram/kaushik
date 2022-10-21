from tkinter import *
from functools import partial
import tkinter as tk


def create_new_page(name_of_page):
    print("Present=%s" % (name_of_page))
def create_new_page1(name_of_page):
    print("Absent=%s" % (name_of_page))
 
root = Tk()
scroll_bar = Scrollbar(root)
scroll_bar.pack( side = RIGHT,fill = Y )
A={1: 'V.Bala Sandhya',  2: 'S.Harini', 3: 'V.M.Joshitha', 4: 'P.Madhuvanthi', 5: 'G.Mirudula', 6: 'J.Phoojithaa', 7: 'R.Rajalakshmi', 8: 'M.K.G.Raja Samvirtha', 9: 'C.R.Renuka', 10: 'V.Samanvitaa', 11: 'K.Samrithi', 12: 'S.Sanjula', 13: 'R.Shreenidhi', 14: 'S.Shreya', 15: 'S.Vijayasri', 16: 'R.Adithya', 17: 'K.Ashwin', 18: 'R.Balaji', 19: 'M.Chirag Sharma', 20: 'A.Deenathayalan', 21: 'Gokul', 22: 'A.Hem Akash Vishwa', 23: 'P.Kaushik Ram', 24: 'Lokesh Raj Kumar', 25: 'S.Manoj Srivatsava', 26: 'S.Meenatchi Sundaram', 27: 'M.Naren Rithik', 28: 'V.A.Padmesh', 29: 'M.Pranav Abishek', 30: 'V.R.Raghunanthan', 31: 'V.Rishikesh Raman', 32: 'M.Shashank', 33: 'R.Sivaramakrishnan', 34: 'Srijan Prasanna', 35: 'S.Srikar', 36: 'V.Srikumar', 37: 'Surjith Khannan Rajasekar'}
mylist = Listbox(root,yscrollcommand = scroll_bar.set )
 
for i in range(1,(len(A)+1)):
    mylist.insert(END,A[i])
    command = partial(create_new_page, i)
    command1 = partial(create_new_page1, i)
    label = tk.Label(root, text=A[i])
    button = tk.Button(root, text="Present", command=command)
    button1 = tk.Button(root, text="Absent", command=command1)
    label.pack()
    button.place(relx=0.7,rely=0.5,anchor="center")
    button1.place(relx=0.7,rely=0.5,anchor="center")
mylist.pack()
scroll_bar.config( command = mylist.yview )
 
root.mainloop()
