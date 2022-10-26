import tkinter as tk
from tkinter import *
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from time import sleep


AbRoll      = []                                  #AbRoll  is list of absentees Roll number
AbName      = []                                  #AbName  is list of absentees Name
Attendance  = []

AbDict      = {}
AbNum       = {}
c=0
mydate=111
A={1: 'V.Bala Sandhya'}#,  2: 'S.Harini', 3: 'V.M.Joshitha', 4: 'P.Madhuvanthi', 5: 'G.Mirudula', 6: 'J.Phoojithaa', 7: 'R.Rajalakshmi', 8: 'M.K.G.Raja Samvirtha', 9: 'C.R.Renuka', 10: 'V.Samanvitaa', 11: 'K.Samrithi', 12: 'S.Sanjula', 13: 'R.Shreenidhi', 14: 'S.Shreya', 15: 'S.Vijayasri', 16: 'R.Adithya', 17: 'K.Ashwin', 18: 'R.Balaji', 19: 'M.Chirag Sharma', 20: 'A.Deenathayalan', 21: 'Gokul', 22: 'A.Hem Akash Vishwa', 23: 'P.Kaushik Ram', 24: 'Lokesh Raj Kumar', 25: 'S.Manoj Srivatsava', 26: 'S.Meenatchi Sundaram', 27: 'M.Naren Rithik', 28: 'V.A.Padmesh', 29: 'M.Pranav Abishek', 30: 'V.R.Raghunanthan', 31: 'V.Rishikesh Raman', 32: 'M.Shashank', 33: 'R.Sivaramakrishnan', 34: 'Srijan Prasanna', 35: 'S.Srikar', 36: 'V.Srikumar', 37: 'Surjith Khannan Rajasekar'}

##                   ATTENDANCE MODULE START            ##


print ( "roll".ljust(6),"Name".ljust(30),"Attendance" )
for i in A.keys() :
    print ( str(i).ljust(6),A[i].ljust(30),end="" )
    response = input(" ".ljust(1))
    while response.lower() != "n" and response.lower() != "y" :
        response = input("Enter n or y")
    if response.lower() == "n" :
        AbRoll.append(i)
        AbName.append(A[i])
        c=c+1
    Attendance.append({'roll':str(i),'name':str(A[i]),'attendance':str(response)})
AbDict={"date":mydate,"roll":AbRoll,"name":AbName}
n=len(A.keys())
bar_data={"date":mydate,"number_of_absentees":c,"number of present":n-c}

##                   ATTENDANCE MODULE END            ##

b = tuple()
if len(AbDict['roll'])==0:
    print("there are no absentees")
else:
    date="DATE".ljust(20),mydate
    l="Today's absentees : "


    for i in range (len(AbDict["roll"])):
        a=( str( AbDict["roll"][i]).ljust(6) , AbDict["name"][i].ljust(30) )
        AbNum=len(AbDict["name"])
        b=b+(a,)


eg=tk.Tk()
eg.geometry("800x800")
eg.configure(bg="black")
label=tk.Label(eg,bg='black',font=('Comic Sans MS','20','bold'),fg='white',bd=0,text=str(date))
label1=tk.Label(eg,bg='black',font=('Comic Sans MS','20','bold'),fg='white',text=str(l))
label2=tk.Label(eg,bg='black',font=('Comic Sans MS','20','bold'),fg='white',text=str(b))

label.place(relx=0.5,rely=0.1,anchor='center')
label1.place(relx=0.5,rely=0.3,anchor='center')
label2.place(relx=0.5,rely=0.5,anchor='center')
eg.mainloop()







##        writing attendance to csv           ##
# attendance
filename = str(mydate) + "_daily_attendance.csv"
date1=[mydate,]
with open(filename , 'w' )  as f :
    writer = csv.writer(f)
    writer.writerow(date1)  
    attendance_pen = csv.DictWriter(f, fieldnames=['roll','name','attendance'])            
    attendance_pen.writeheader()
    for i in Attendance :
        attendance_pen.writerow(i)
print("attendance has been written to ", filename)

#storing absentees data  
presence=os.path.isfile(r'absentees.csv')
if presence == True :                                   
    with open(r'absentees.csv','a',newline='\n') as fn :
        writer_2 = csv.DictWriter(fn,fieldnames= ['date' , 'number_of_absentees',"number of present"])
        writer_2.writerow(bar_data)
else :
    with open(r'absentees.csv','w',newline='\n') as fn :
        writer_2 = csv.DictWriter(fn , fieldnames = ['date' , 'number_of_absentees',"number of present"])
        writer_2.writeheader()
        writer_2.writerow(bar_data)

####################################################################################################
####################################################################################################
####################################################################################################


##def view():
##    t=tk.Toplevel()
##    t.title("Attendance")
##    t.geometry("500x500")
##    t.configure(bg="black")
##
##    def getattend():
##        try:
##            value=e.get()
##            
##            date = value #input("enter date to access attendance {date should be in the form dd-mm-yyyy for months October to December and dd-m-yyyy for other months}:")
##            filename = date  + "_daily_attendance.csv"
##        ##        print("opening " , filename)
####            df = pd.read_csv(filename)
##            for i in range (len(AbDict["roll"])):
##                print( str( AbDict["roll"][i]).ljust(6) , AbDict["name"][i].ljust(30) , end="\n" )
##                AbNum=len(AbDict["name"])
##            print(i)
##            t1=tk.Toplevel()
##
##            t1.title("Attendance")
##            t1.geometry("500x500")
##            t1.configure(bg="black")
##            label=Label(t1)
##            label.config(text=df)
##            label.place()
##            t1.mainloop()
##            
##        ##        print(value)
####            e.delete(0,'end')
##        except FileNotFoundError:
##            bi=tk.Toplevel()
##            bi.title("Attendance")
##            bi.geometry("500x500")
##            bi.configure(bg="black")
##            a=Label(bi,text='Enter date correctly...!',font=('Comic Sans MS','30','bold'),bg='black',fg='white',bd=0)
##            a.place(relx=0.5,rely=0.1,anchor='center')
##            def des():
##                bi.destroy()
##            b=tk.Button(bi,text='OK',bg='black',fg='White',font=('Comic Sans MS','20','bold'),activebackground='black',width=10,command= des)
##            b.place(relx=0.5,rely=0.5,anchor="center")
##            bi.mainloop()
##            
##            
##
##            
##    l=Label(t,font=('Comic Sans MS','30','bold'),bg='black',fg='white',bd=0,text='Enter date')
##    e=Entry(t,font=('Comic Sans MS','30','bold'),width=20)
##    b=Button(t,text='Get attendance',bg='black',bd=0,fg='white',font=('Comic Sans MS','30','bold'),command=getattend)
##
##    l.place(relx=0.5,rely=0.1,anchor='center')
##    e.place(relx=0.5,rely=0.3,anchor='center')
##    b.place(relx=0.5,rely=0.5,anchor='center')
##
##    t.mainloop()

