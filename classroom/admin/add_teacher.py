from tkinter import*
from tkinter import messagebox
from PIL import Image , ImageTk
import dataBase
import viewTeacher
class ImageWidget:

    def __init__(self):
        self.root = Toplevel()
        self.root.title('Add Teacher Page')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        

    def mainFrame(self):
        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.place(x = 0, y = 0,width=1000,height=667)

        # placing images
        self.image = ImageTk.PhotoImage(Image.open('images/teacher.jpg').resize((1000,667)))
        self.imageLabel = Label(self.main_frame, image=self.image,bg='black')
        self.imageLabel.place(x = 0, y= 0)


        # frame 1
        self.frame1 = Frame(self.main_frame,bg='black')
        self.frame1.place(x = 550, y= 70,width=400,height=450)

        self.text = 'Add Teachers'
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
        

        self.AddButton=Button(self.frame1,text='Add Now',command=self.login,fg='red',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.AddButton.place(x=160,y=370)

        self.root.mainloop()

    def login(self):
        data = (
            self.NameEntry.get(),
            self.AgeEntry.get(),
            self.QualEntry.get(),
            self.MailEntry.get(),
            self.passEntry.get(),
        )
        if(self.NameEntry.get() == ''):
            messagebox.showerror('Alert ','Enter your Name first')
        elif(self.AgeEntry.get() == ''):
            messagebox.showerror('Alert ','Enter your Age first')
        elif(self.QualEntry.get() == ''):
            messagebox.showerror('Alert ','Enter your Qualification first')
        elif(self.MailEntry.get() == ''):
            messagebox.showerror('Alert ','Enter your E-Mail ID first')
        elif(self.passEntry.get() == ''):
            messagebox.showerror('Alert ','Enter your Password first')
        else:
            res  = dataBase.addTeacher(data)
            if res:
                print(data)
                messagebox.showinfo('Success', 'Teacher added successfully.')
                self.root.destroy()
                obj =viewTeacher.viewTeacher()
                obj.Teacher()
            else:
                messagebox.showinfo("Alert","Something went wrong")
    
if __name__ == "__main__":
    obj = ImageWidget()
    obj.mainFrame()
   