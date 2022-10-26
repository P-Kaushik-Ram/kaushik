##import tkinter as tk
##from tkinter import *
##from PIL import Image
##import pandas as pd
##import numpy as np
##import matplotlib.pyplot as plt
##from tkinter import messagebox as mb
##import csv
##import os
##import sys
##import csv
##import os
##
##
##def filewriting(date,absents):      
##    
##    presence=os.path.isfile(r'absentees.csv')
##    if presence == True :
##        with open(r'absentees.csv','a',newline='\n') as fn :
##            writer_2 = csv.writer(fn)
##            bar_data=[date,len(absents),37-len(absents)]
##            writer_2.writerow(bar_data)
##            
##    else :
##        with open(r'absentees.csv','w',newline='\n') as fn :
##            writer_2 = csv.writer(fn)
##            bar_data=[date,len(absents),37-len(absents)]
##            writer_2.writerow(bar_data)
##
##
##d={1: 'V.Bala Sandhya',  2: 'S.Harini', 3: 'V.M.Joshitha', 4: 'P.Madhuvanthi', 5: 'G.Mirudula', 6: 'J.Phoojithaa', 7: 'R.Rajalakshmi', 8: 'M.K.G.Raja Samvirtha'}#, 9: 'C.R.Renuka', 10: 'V.Samanvitaa', 11: 'K.Samrithi', 12: 'S.Sanjula', 13: 'R.Shreenidhi', 14: 'S.Shreya', 15: 'S.Vijayasri', 16: 'R.Adithya', 17: 'K.Ashwin', 18: 'R.Balaji', 19: 'M.Chirag Sharma', 20: 'A.Deenathayalan', 21: 'Gokul', 22: 'A.Hem Akash Vishwa', 23: 'P.Kaushik Ram', 24: 'Lokesh Raj Kumar', 25: 'S.Manoj Srivatsava', 26: 'S.Meenatchi Sundaram', 27: 'M.Naren Rithik', 28: 'V.A.Padmesh', 29: 'M.Pranav Abishek', 30: 'V.R.Raghunanthan', 31: 'V.Rishikesh Raman', 32: 'M.Shashank', 33: 'R.Sivaramakrishnan', 34: 'Srijan Prasanna', 35: 'S.Srikar', 36: 'V.Srikumar', 37: 'Surjith Khannan Rajasekar'}
##
##class AttendFrame(Frame):
##        def __init__(self,master,rno):
##                super().__init__(master,bg='black')
##                self.rno=rno
##                Label(self,text=f'{self.rno} - {d[self.rno]}',bg='black',fg='white',font=('Comic Sans MS','30','bold'),bd=10).grid(row=0,column=0,columnspan=2)
##                Button(self,text='PRESENT',bg='black',fg='white',font=('Comic Sans MS','20','bold'),bd=0,command=self.present).grid(row=1,column=0)
##                Button(self,text='ABSENT',bg='black',fg='white',font=('Comic Sans MS','20','bold'),bd=0,command=self.absent).grid(row=1,column=1)
##                self.update()
##        def present(self):
##                self.val='present'
##                self.pack_forget()
##                self.quit()
##        def absent(self):
##                self.val='absent'
##                self.pack_forget()
##                self.quit()
##def get_absentee():
##        if list_of_today==[]:
##                print('attendence not taken')
##                return
##        else:
##            
##            global absents
##            absents=[]
##            for i in d:
##                    if list_of_today[i-1]=='absent':
##                            absents.append(d[i])
##            filewriting(date,absents)               
##            st=''
##            for a in absents:
##                st+=a+'\n'
##            return st
##            
##
##bi=Tk()
##list_of_today=[]
##bi.geometry('500x500')
##bi.configure(bg='black')
##Label(bi,text='Attendence',bg='black',fg='blue',font=('Comic Sans MS','40','bold')).pack()
##
##
##def date_entry():
##   global date
##   date= entry.get()
##entry= Entry(bi, font=('Comic Sans MS','10','bold'),width= 40,bd=0)
##entry.focus_set()
##entry.pack()
##tk.Button(bi, text= "Okay",font=('Comic Sans MS','10','bold'),bg='black',fg='white',bd=10,width= 10, command= date_entry).pack(pady=20)
##
##for i in d:
##        x=AttendFrame(bi,i)
##        x.pack()
##        x.update()
##        x.mainloop()
##        value=x.val
##        list_of_today.append(value)
##c=list_of_today.count('absent')
##Label(bi,text=str(get_absentee()),bg='black',fg='white',font=('Comic Sans MS','20','bold')).place(relx=0.5,rely=0.5,anchor='center')
##mb.showinfo('attendance',f'{c} students absent today')
##bi.destroy()
##        
##
##
##
##



# This python program gets attendance and writes the output to an excel file [to prevent data getting lost on closure of program ]
# Our goal is to make use of the excel file to store attendance for a given day ,
# Plot graph of trends for a week and acces attendance of specific day if prompted by user
##                             importing needed modules                      ##

import os
import pandas as pd
import csv
from time import sleep
from attendance_list import A             #here attendance list is a .py file , A is a dictionary of students
import matplotlib.pyplot as plt
import numpy as np
while True :
    ##   creating needed empty lists , empty dictionary and empty csv files ##
    ## lists :
    AbRoll      = []                                  #AbRoll  is list of absentees Roll number
    AbName      = []                                  #AbName  is list of absentees Name
    Attendance  = []
    ##dictionaries
    AbDict      = {}
    AbNum       = {}
    c=0
    print("_________".center(50))
    print("XII-C ATTENDANCE REGISTER".center(50))
    print("_________".center(50))
    print("What do you want to do ?")
    print("[1]".ljust(27), "Take Attendance")
    print("[2]".ljust(27), "Access Daily Attendance")
    print("[3]".ljust(27), "View Overall Statistics")
    choice = input("enter your choice ".ljust(20))
    if choice == '1' :
        print("You have selected task : Take Attendance")
        ##                   ATTENDANCE MODULE START            ##

##                   ATTENDANCE MODULE START            ##

        date = int(input("Enter the date"))
        while date > 31 and date > 0:
            date = int(input("Enter the correct date"))
        month = int(input("Enter the month"))
        while month > 12 and month > 0:
            month = int(input("Enter the correct month"))
        while month==2 and date>=29:
            print("Please Change the Date or Month")
            o=input("for Date enter d,for Month enter m")
            while o.lower() in 'dm':
                if o.lower()=='d':
                    date = int(input("Enter the correct date"))
                elif o.lower()=='m':
                    month = int(input("Enter the correct month"))
        while (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and date>31:
            print("Please Change the Date or Month")
            o=input("for Date enter d,for Month enter m")
            while o.lower() in 'dm':
                if o.lower()=='d':
                    date = int(input("Enter the correct date"))
                elif o.lower()=='m':
                    month = int(input("Enter the correct month"))
        while (month==4 or month==6 or month==9 or month==11) and date>30:
            print("Please Change the Date or Month")
            o=input("for Date enter d,for Month enter m")
            while o.lower() in 'dm':
                if o.lower()=='d':
                    date = int(input("Enter the correct date"))
                elif o.lower()=='m':
                    month = int(input("Enter the correct month"))
        year = 2022
        mydate = str(date) + '-' + str(month) + '-' + str(year)
           
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
       
        if len(AbDict['roll'])==0:
            print("there are no absentees")
        else:
            print("DATE".ljust(20),mydate)
            print("number on roll".ljust(20))
            print ("Today's absentees : ")
            print ("Roll".ljust(6),"Name".ljust(30))

            for i in range (len(AbDict["roll"])):
                print( str( AbDict["roll"][i]).ljust(6) , AbDict["name"][i].ljust(30) , end="\n" )
                AbNum=len(AbDict["name"])



        ##        writing attendance to csv           ##
        # attendance
        filename = mydate + "_daily_attendance.csv"
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

        ## Making  the pie chart
        Tasks = [c,(n-c)]
        my_labels = 'Absentees','Present'
        plt.pie(Tasks,labels=my_labels,autopct='%1.1f%%')
        plt.title('Class Attendees')
        plt.axis('equal')
        plt.show()
        c=input("enter q to quit any other key to continue :  ")
        if c.lower()== 'q' :
            break
        else :
            continue

       
    elif choice == '2' :
        print("You have selected task : Access Daily Attendance")
        date = input("enter date to access attendance {date should be in the form dd-mm-yyyy for months October to December and dd-m-yyyy for other months}:")
        filename = date + "_daily_attendance.csv"
        print("opening " , filename)
        df = pd.read_csv(filename)
        print(df)
        c=input("enter q to quit any other key to continue :  ")
        if c.lower()== 'q' :
            break
        else :
            continue
       
    elif choice == '3' :
        df=pd.read_csv(r'absentees.csv')
        date = df["date"]
        absent = df["number_of_absentees"]
        present = df["number of present"]
        x = np.arange(len(date))  
        fig, ax = plt.subplots()
        width=0.35
        rects1 = ax.bar(x - width/2, absent, width, label='Absent')
        rects2 = ax.bar(x + width/2, present, width, label='Present')
        ax.set_ylabel('Number of students')
        ax.set_xlabel('Date')
        ax.set_title('XII C ')
        ax.set_xticks(x, date)
        ax.legend()
        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)
        fig.tight_layout()
        plt.show()
        c=input("enter q to quit any other key to continue :  ")
        if c.lower()== 'q' :
            break
        else :
            continue
