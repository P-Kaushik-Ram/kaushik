from tkinter import *
from tkinter import messagebox as mb

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
        absents=[]
        for i in d:
                if list_of_today[i-1]=='absent':
                        absents.append(d[i])
        return absents

bi=Tk()
list_of_today=[]
bi.geometry('500x500')
bi.configure(bg='black')
Label.PhotoImage(Image.open("as.png"), master=app_root )
Label(bi,text='Attendence',bg='black',fg='blue',font=('Comic Sans MS','40','bold')).pack()
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

