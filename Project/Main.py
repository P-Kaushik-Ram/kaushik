import tkinter as tk
from tkinter import *
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox as mb
import csv
import os
import sys






def over_all():
    df=pd.read_csv(r'absentees.csv')
    date = df["date"]
    absent = df["number_of_absentees"]
    present = df["number of present"]
    x = np.arange(len(date))  
    fig=plt.figure("Overall Attendance")
    ax=fig.subplots()
    width=0.35
    rects1 = ax.bar(x - width/2, absent, width, label='Absent')
    rects2 = ax.bar(x + width/2, present, width, label='Present')
    ax.set_ylabel('Number of students')
    ax.set_xlabel('Date')
    ax.set_title('XII-C ')
    ax.set_xticks(x, date)
    ax.legend()
    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)
    plt.show()
def b1():
    def filewriting(date,absents):      
   
        presence=os.path.isfile(r'absentees.csv')
        if presence == True :
            with open(r'absentees.csv','a',newline='\n') as fn :
                writer_2 = csv.writer(fn)
                bar_data=[date,len(absents),37-len(absents)]
                writer_2.writerow(bar_data)
               
        else :
            with open(r'absentees.csv','w',newline='\n') as fn :
                writer_2 = csv.writer(fn)
                bar_data=[date,len(absents),37-len(absents)]
                writer_2.writerow(bar_data)
    def absenteewriting(date,absents):      
   
        presence=os.path.isfile(r'Data.csv')
        if presence == True :
            with open(r'Data.csv','a',newline='\n') as fn :
                writer_2 = csv.writer(fn)
                bar_data=[date,absents]
                writer_2.writerow(bar_data)
               
        else :
            with open(r'Data.csv','w',newline='\n') as fn :
                writer_2 = csv.writer(fn)
                bar_data=[date,absents]
                writer_2.writerow(bar_data)

    d={1: 'V.Bala Sandhya',  2: 'S.Harini', 3: 'V.M.Joshitha', 4: 'P.Madhuvanthi', 5: 'G.Mirudula', 6: 'J.Phoojithaa', 7: 'R.Rajalakshmi', 8: 'M.K.G.Raja Samvirtha'}#, 9: 'C.R.Renuka', 10: 'V.Samanvitaa', 11: 'K.Samrithi', 12: 'S.Sanjula', 13: 'R.Shreenidhi', 14: 'S.Shreya', 15: 'S.Vijayasri', 16: 'R.Adithya', 17: 'K.Ashwin', 18: 'R.Balaji', 19: 'M.Chirag Sharma', 20: 'A.Deenathayalan', 21: 'Gokul', 22: 'A.Hem Akash Vishwa', 23: 'P.Kaushik Ram', 24: 'Lokesh Raj Kumar', 25: 'S.Manoj Srivatsava', 26: 'S.Meenatchi Sundaram', 27: 'M.Naren Rithik', 28: 'V.A.Padmesh', 29: 'M.Pranav Abishek', 30: 'V.R.Raghunanthan', 31: 'V.Rishikesh Raman', 32: 'M.Shashank', 33: 'R.Sivaramakrishnan', 34: 'Srijan Prasanna', 35: 'S.Srikar', 36: 'V.Srikumar', 37: 'Surjith Khannan Rajasekar'}

    class AttendFrame(Frame):
            def __init__(self,master,rno):
                    super().__init__(master,bg='black')
                    self.rno=rno
                    Label(self,text=f'{self.rno} - {d[self.rno]}',bg='black',fg='white',font=('Comic Sans MS','30','bold'),bd=10).grid(row=0,column=0,columnspan=2)
                    Button(self,text='PRESENT',bg='black',fg='white',font=('Comic Sans MS','20','bold'),bd=0,command=self.present).grid(row=1,column=0)
                    Button(self,text='ABSENT',bg='black',fg='white',font=('Comic Sans MS','20','bold'),bd=0,command=self.absent).grid(row=1,column=1)
                    self.update()
            def present(self):
                    self.val='present'
                    self.pack_forget()
                    self.quit()
            def absent(self):
                    self.val='absent'
                    self.pack_forget()
                    self.quit()
    def get_absentee():
            if list_of_today==[]:
                    print('attendence not taken')
                    return
            else:
               
                global absents
                absents=[]
                for i in d:
                        if list_of_today[i-1]=='absent':
                                absents.append(d[i])
                absenteewriting(date,absents)
                filewriting(date,absents)              
                st=''
                for a in absents:
                    st+=a+'\n'
                return st
               

    bi=Tk()
    list_of_today=[]
    bi.geometry('500x500')
    bi.configure(bg='black')
    Label(bi,text='Attendence',bg='black',fg='blue',font=('Comic Sans MS','40','bold')).pack()


    def date_entry():
       global date
       date= entry.get()
    entry= Entry(bi, font=('Comic Sans MS','10','bold'),width= 40,bd=0)
    entry.focus_set()
    entry.pack()
    tk.Button(bi, text= "Okay",font=('Comic Sans MS','10','bold'),bg='black',fg='white',bd=10,width= 10, command= date_entry).pack(pady=20)

    for i in d:
            x=AttendFrame(bi,i)
            x.pack()
            x.update()
            x.mainloop()
            value=x.val
            list_of_today.append(value)
    c=list_of_today.count('absent')
    Label(bi,text=str(get_absentee()),bg='black',fg='white',font=('Comic Sans MS','20','bold')).place(relx=0.5,rely=0.5,anchor='center')
    mb.showinfo('attendance',f'{c} students absent today')
    bi.destroy()


def b2():
    def date_entry():
        global date
        date = entry.get()
        fh=open("Data.csv")
        reader=csv.reader(fh)
        for rec in reader:
            if rec[0]== date:
                if len(rec[1]) == 2:
                    b='No Absentees !'
                    a.config(text=b)
                else:
                    b=rec[1]
                    b= b.replace("'",'')
                    sb = b.strip('][').split(', ')
                    b=''
                    for i in sb:
                        b += i + '\n'
                    a.config(text=b)

    ai=tk.Toplevel()
    ai.geometry("612x612")
    ai.title("Viewing Attendance")
    ai.configure(bg='black')
    entry= Entry(ai, font=('Comic Sans MS','10','bold'),width= 40,bd=10)
    entry.focus_set()
    entry.place(relx=0.5,rely=0.1,anchor='center')
    tk.Button(ai, text= "Okay",font=('Comic Sans MS','10','bold'),bg='black',fg='white',bd=10,width= 10, command= date_entry).place(relx=0.5,rely=0.2,anchor='center')
    a=tk.Label(ai,text="",font=('Comic Sans MS','30','bold'),bg="black",fg='white')
    a.place(relx=0.5,rely=0.5,anchor='center')
    ai.mainloop()

def b3():
    bi = tk.Toplevel()
    bi.geometry("612x612")
    bi.title("Overall Attendance")
    bi.configure(bg='black')
    img = tk.PhotoImage(file="as.png")
    label = tk.Label(bi, image = img)
    label.place(relx=0.5,rely=0.5,anchor='center')
    label=tk.Label(bi,text='Overall Attendance',font=('Comic Sans MS','30','bold'),bg="white",fg='black')
    label.place(relx=0.5,rely=0.05,anchor='center')
    def des():
        bi.destroy()
    i=tk.PhotoImage(file="power.png")
    b=tk.Button(bi,image=i,bg='white',borderwidth=0,command= des)
    b.place(relx=0.99,rely=0.99,anchor="se")
    bi.mainloop()




root = tk.Tk()
root.geometry("1000x800")
root.title("Attendance")
root.configure(bg='black')

file="a.gif"

info = Image.open(file)

frames = info.n_frames

im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

gif_label = tk.Label(root, text='test',image="")
gif_label.pack()
animation(count)

label=tk.Label(root,text='Attendance Software',font=('Comic Sans MS','30','bold'),bg="black",fg='white')
label.place(relx=0.5,rely=0.05,anchor='center')

bta=tk.Button(root,text="Taking Attendance",font=('Comic Sans MS','16','bold'),command=b1)
bta.place(relwidth=0.5,relx=0.5,rely=0.4,anchor="center")

bva=tk.Button(root,text="Viewing Attendance",font=('Comic Sans MS','16','bold'),command=b2)
bva.place(relwidth=0.5,relx=0.5,rely=0.55,anchor="center")

boa=tk.Button(root,text="Overall Attendance",font=('Comic Sans MS','16','bold'),command=over_all)
boa.place(relwidth=0.5,relx=0.5,rely=0.7,anchor="center")





i=tk.PhotoImage(file="power1.png")
b=tk.Button(root,image=i,bg='black',borderwidth=0,command= root.destroy)
b.place(relx=0.99,rely=0.99,anchor="se")

def frame1():
    root.geometry("800x700")
    root.title("Taking Attendance")
    root.configure(bg='black')
    b1=Button(root,text="back",font=('Comic Sans MS','20','bold'),bg='black',fg='white',borderwidth=0,padx=30,pady=15)
    b1.place(relx=0.99,rely=0.99,anchor="se")
   


def frame2():
    root.geometry("800x700")
    root.title("Taking Attendance")
    root.configure(bg='black')
    b2=Button(root,text="back",font=('Comic Sans MS','20','bold'),bg='black',fg='white',borderwidth=0,padx=30,pady=15)
    b2.place(relx=0.99,rely=0.99,anchor="se")





root.mainloop()
