from ctypes import resize
from msilib.schema import ComboBox
from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
from turtle import bgcolor
from PIL import Image , ImageTk

class ImageWidget:

    def __init__(self):
        self.root = Toplevel()
        self.root.title('Add Courses Page')
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

        # frame 1
        self.frame1 = Frame(self.main_frame,bg='black')
        self.frame1.place(x = 0, y= 0,width=500,height=667)

        self.image = ImageTk.PhotoImage(Image.open('images/course.png').resize((500,335)))
        self.imageLabel= Label(self.frame1, image=self.image,bg='black')
        self.imageLabel.place(x = 0, y= 150)

        # frame 2

        self.frame2 = Frame(self.main_frame,bg='white')
        self.frame2.place(x = 500, y= 0,width=500,height=333.5)

        self.frame3 = Frame(self.main_frame,bg='red')
        self.frame3.place(x = 500, y= 333.5,width=500,height=333.5)
        self.image1 = ImageTk.PhotoImage(Image.open('images/batch.jpg').resize((500,333)))
        self.imageLabel1 = Label(self.frame3, image=self.image1,bg='white')
        self.imageLabel1.place(x = 0, y= 0)

        self.text = 'Add Courses'
        self.heading = Label(self.frame2,text=self.text,font=('Baskerville',20,'bold'),fg='black',bg='white')
        self.heading.place(x=0,y=0,width=200,height=50)

   
    def entryMethod(self):

        self.DeptLabel=Label(self.frame2,text='Select Department',font=('Rockwell',12),bg='white')
        self.DeptLabel.place(x=20,y=70)
        self.comboValue = StringVar()
        self.options = ['Civil', 'Computer Science', 'Mechanical']
        self.dropDown = Combobox(self.frame2, textvariable=self.comboValue, values=self.options,font=('Times New Roman',12),)
        self.dropDown.place(x=20,y=110)
        

        
        self.CourseLabel=Label(self.frame2,text='Course Name',font=('Rockwell',12),bg='white')
        self.CourseLabel.place(x=20,y=150)
        self.CourseEntry=StringVar()
        self.entryWidget1=Entry(self.frame2,textvariable=self.CourseEntry,bg='white',font=('Times New Roman',12))
        self.entryWidget1.place(x=20,y=180)


        self.CourseLabel=Label(self.frame2,text='Course Duration',font=('Rockwell',12),bg='white')
        self.CourseLabel.place(x=20,y=210)
        self.CourseEntry=StringVar()
        self.entryWidget1=Entry(self.frame2,textvariable=self.CourseEntry,bg='white',font=('Times New Roman',12))
        self.entryWidget1.place(x=20,y=240)

        self.AddButton=Button(self.frame2,text='Add Now',command=self.login,fg='red',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.AddButton.place(x=20,y=280)

        self.root.mainloop()

    def login(self):
        if(self.comboValue.get() == ''):
            messagebox.showerror('Alert ','Enter the Department first')
        elif(self.CourseEntry.get() == ''):
            messagebox.showerror('Alert ','Enter Course name first')
        else:
            messagebox.showinfo('Completion','Added Successfully')
    
if __name__ == "__main__":
    obj = ImageWidget()
    obj.mainFrame()
    obj.entryMethod()
   