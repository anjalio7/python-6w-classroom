from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image , ImageTk
import dataBase,viewSubject
class ImageWidget:

    def __init__(self):
        self.root = Toplevel()
        self.root.title('Add Subject Page')
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

   
        self.image = ImageTk.PhotoImage(Image.open('images/sub.jpg').resize((1000,667)))
        self.imageLabel= Label(self.main_frame, image=self.image,bg='white')
        self.imageLabel.place(x = 0, y= 0)

     # frame 1
        self.frame1 = Frame(self.main_frame,bg='white')
        self.frame1.place(x = 270, y= 100,width=500,height=300)

        self.text = 'Add Subject'
        self.heading = Label(self.frame1,text=self.text,font=('Baskerville',20,'bold'),fg='#FF3AAE',bg='white')
        self.heading.place(x=140,y=30,width=200,height=50)

        self.DeptLabel=Label(self.frame1,text='Select Course',font=('Rockwell',15),bg='white',fg='#3A85FF')
        self.DeptLabel.place(x=30,y=100)
        self.comboValue1 = StringVar()
        self.options = dataBase.ViewCourses()
        self.courseName = Combobox(self.frame1, textvariable=self.comboValue1, values=self.options,font=('Times New Roman',12),)
        self.courseName.place(x=210,y=100)

        self.CourseLabel=Label(self.frame1,text='Subject Name',font=('Rockwell',15),bg='white',fg='#3A85FF')
        self.CourseLabel.place(x=30,y=150)

        self.subNameEntry = StringVar()
        self.dropDown = Entry(self.frame1, textvariable=self.subNameEntry,font=('Times New Roman',12),)
        self.dropDown.place(x=210,y=150)
        
        self.SubLabel=Label(self.frame1,text='Subject Code',font=('Rockwell',15),bg='white',fg='#3A85FF')
        self.SubLabel.place(x=30,y=200)
        self.SubEntry=StringVar()
        self.entryWidget1=Entry(self.frame1,textvariable=self.SubEntry,bg='white',font=('Times New Roman',12))
        self.entryWidget1.place(x=210,y=200)

        self.AddButton=Button(self.frame1,text='Add Now',command=self.login,fg='#FF3A4F',bg='white',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.AddButton.place(x=190,y=240)

        self.root.mainloop()

    def login(self):
        self.courseName = self.courseName.get().split()
        print(self.courseName)
        data = (
            self.courseName[0],
            self.dropDown.get(),
            self.entryWidget1.get(),
        )
        if(self.courseName == ''):
            messagebox.showerror('Alert ','Enter the Course first')
        elif(self.dropDown.get() == ''):
            messagebox.showerror('Alert ','Enter the Subject name first')
        elif(self.SubEntry.get() == ''):
            messagebox.showerror('Alert ','Enter Subject code first')
        else:
            res  = dataBase.addSubject(data)
            if res:
                print(data)
                messagebox.showinfo('Success', 'Subject added successfully.')
                self.root.destroy()
                obj =viewSubject.viewSubject()
                obj.Subject()
            else:
                messagebox.showinfo("Alert","Something went wrong")


if __name__ == "__main__":
    obj = ImageWidget()
    obj.mainFrame()
   