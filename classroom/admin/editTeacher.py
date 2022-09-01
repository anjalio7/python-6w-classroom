from tkinter import*
from tkinter import messagebox
from PIL import Image , ImageTk
import dataBase
import viewTeacher
class ImageWidget:

    def __init__(self):
        self.root = Toplevel()
        self.root.title('Edit Teacher Page')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        

    def mainFrame(self,data):
        self.data = data

        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.place(x = 0, y = 0,width=1000,height=667)

        # placing images
        self.image = ImageTk.PhotoImage(Image.open('images/teacher.jpg').resize((1000,667)))
        self.imageLabel = Label(self.main_frame, image=self.image,bg='black')
        self.imageLabel.place(x = 0, y= 0)


        # frame 1
        self.frame1 = Frame(self.main_frame,bg='black')
        self.frame1.place(x = 550, y= 70,width=400,height=450)

        self.text = 'Edit Teachers'
        self.heading = Label(self.frame1,text=self.text,font=('Baskerville',20,'bold'),fg='white',bg='black')
        self.heading.place(x=80,y=20,width=250,height=50)
        

        self.NameLabel=Label(self.frame1,text='Teacher Name : ',font=('Rockwell',12),bg='black',fg='white')
        self.NameLabel.place(x=20,y=100)
        self.NameEntry=StringVar()
        self.entryWidget1=Entry(self.frame1,textvariable=self.NameEntry,bg='white',font=('Times New Roman',12))
        self.entryWidget1.place(x=210,y=100)


        self.AgeLabel=Label(self.frame1,text='Teacher Age : ',font=('Rockwell',12),bg='black',fg='white')
        self.AgeLabel.place(x=20,y=150)
        self.AgeEntry=StringVar()
        self.entryWidget2=Entry(self.frame1,textvariable=self.AgeEntry,bg='white',font=('Times New Roman',12))
        self.entryWidget2.place(x=210,y=150)


        self.QualLabel=Label(self.frame1,text='Teacher Qualification : ',font=('Rockwell',12),bg='black',fg='white')
        self.QualLabel.place(x=20,y=200)
        self.QualEntry=StringVar()
        self.entryWidget3=Entry(self.frame1,textvariable=self.QualEntry,bg='white',font=('Times New Roman',12))
        self.entryWidget3.place(x=210,y=200)


        self.MailLabel=Label(self.frame1,text='Teacher Username : ',font=('Rockwell',12),bg='black',fg='white')
        self.MailLabel.place(x=20,y=250)
        self.MailEntry=StringVar()
        self.entryWidget4=Entry(self.frame1,textvariable=self.MailEntry,bg='white',font=('Times New Roman',12))
        self.entryWidget4.place(x=210,y=250)


        self.ExpLabel=Label(self.frame1,text='Teacher Password : ',font=('Rockwell',12),bg='black',fg='white')
        self.ExpLabel.place(x=20,y=300)
        self.passEntry=StringVar()
        self.entryWidget5=Entry(self.frame1,textvariable=self.passEntry,bg='white',font=('Times New Roman',12))
        self.entryWidget5.place(x=210,y=300)
        

        self.EditButton=Button(self.frame1,text='Edit Now',command=self.login,fg='red',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.EditButton.place(x=160,y=370)

        
        for i in dataBase.editTeacher(data):
            print(i)
            self.entryWidget1.insert(0,i[1])
            self.entryWidget2.insert(0,i[2])
            self.entryWidget3.insert(0,i[3])
            self.entryWidget4.insert(0,i[4])
            self.entryWidget5.insert(0,i[5])

        self.root.mainloop()

    def login(self):
        data = (
            self.entryWidget1.get(),
            self.entryWidget2.get(),
            self.entryWidget3.get(),
            self.entryWidget4.get(),
            self.entryWidget5.get(),
            self.data[0]
        )
        if(self.entryWidget1.get() == ''):
            messagebox.showerror('Alert ','Enter your Name first')
        elif(self.entryWidget2.get() == ''):
            messagebox.showerror('Alert ','Enter your Age first')
        elif(self.entryWidget3.get() == ''):
            messagebox.showerror('Alert ','Enter your Qualification first')
        elif(self.entryWidget4.get() == ''):
            messagebox.showerror('Alert ','Enter your E-Mail ID first')
        elif(self.entryWidget5.get() == ''):
            messagebox.showerror('Alert ','Enter your Password first')
        else:
            res  = dataBase.updateTeacher_items(data)
            if res:
                print(data)
                messagebox.showinfo('Success', 'Teacher Edited successfully.')
                self.root.destroy()
                obj =viewTeacher.viewTeacher()
                obj.Teacher()
            else:
                messagebox.showinfo("Alert","Something went wrong")
    
if __name__ == "__main__":
    obj = ImageWidget()
    obj.mainFrame('data')
   