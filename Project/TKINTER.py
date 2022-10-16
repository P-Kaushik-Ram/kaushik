import tkinter as tk
from tkinter import *
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt








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
##            df = pd.read_csv(filename)
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
##            e.delete(0,'end')
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
##
##    
##
##
##
##view()

def b1():
    bi=tk.Toplevel()
    bi.geometry("612x612")
    bi.title("Taking Attendance")
    bi.configure(bg='black')
    img = tk.PhotoImage(file="as.png") 
    label = tk.Label(bi, image = img)
    label.place(relx=0.5,rely=0.5,anchor='center')

    label=tk.Label(bi,text='Enter the Attendence...',font=('Comic Sans MS','30','bold'),bg="white",fg='black')
    label.place(relx=0.5,rely=0.05,anchor='center')
    def des():
        bi.destroy()
    i=tk.PhotoImage(file="power.png")
    b=tk.Button(bi,image=i,bg='white',borderwidth=0,command= des)
    b.place(relx=0.99,rely=0.99,anchor="se")
    bi.mainloop()

def b2():
    bi = tk.Toplevel()
    bi.geometry("612x612")
    bi.title("Viewing Attendance")
    bi.configure(bg='black')
    img = tk.PhotoImage(file="as.png") 
    label = tk.Label(bi, image = img)
    label.place(relx=0.5,rely=0.5,anchor='center')
    label=tk.Label(bi,text='Here you Go...',font=('Comic Sans MS','30','bold'),bg="white",fg='black')
    label.place(relx=0.5,rely=0.05,anchor='center')
    def des():
        bi.destroy()
    i=tk.PhotoImage(file="power.png")
    b=tk.Button(bi,image=i,bg='white',borderwidth=0,command= des)
    b.place(relx=0.99,rely=0.99,anchor="se")
    bi.mainloop()

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

label=tk.Label(root,text='Attendance System',font=('Comic Sans MS','30','bold'),bg="black",fg='white')
label.place(relx=0.5,rely=0.05,anchor='center')

bta=tk.Button(root,text="Taking Attendance",font=('Comic Sans MS','16','bold'),command=b1)
bta.place(relwidth=0.5,relx=0.5,rely=0.4,anchor="center")

bva=tk.Button(root,text="Viewing Attendance",font=('Comic Sans MS','16','bold'),command=b2)
bva.place(relwidth=0.5,relx=0.5,rely=0.55,anchor="center")

boa=tk.Button(root,text="Overall Attendance",font=('Comic Sans MS','16','bold'),command=over_all)
boa.place(relwidth=0.5,relx=0.5,rely=0.7,anchor="center")


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




