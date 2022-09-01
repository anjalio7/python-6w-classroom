from tkinter import*
import dataBase
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image , ImageTk
import view_assign
class ImageWidget:

    def __init__(self):
        self.root = Toplevel()
        self.root.title('Assign Batches Page')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def create(self,e): 
        self.datavalue=self.dropDown2.get().split()
        # print(self.datavalue[0])
        val  =(self.datavalue[0],)
        print("val",val)
        a = dataBase.viewSubname(val)
        # print(a)
        self.SubLabel=Label(self.frame1,text='Subject Name',font=('Rockwell',16),bg='#205950',fg='#F9F37F')
        self.SubLabel.place(x=30,y=200)
        self.comboValue3 = StringVar()
        # self.optiondata = ['']
        if len(a)>0:
            self.optiondata = dataBase.viewSubname(val)
        else:
            messagebox.showerror("warning",'Subject not added yet')
            self.optiondata = dataBase.viewSubname(val)
        self.dropDown3=Combobox(self.frame1,state='readonly',textvariable=self.comboValue3,values=self.optiondata,font=('Times New Roman',12))
        self.dropDown3.configure(state='readonly')
        self.dropDown3.place(x=210,y=200)



    def mainFrame(self):
        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.place(x = 0, y = 0,width=1000,height=667)

   
        self.image = ImageTk.PhotoImage(Image.open('images/assign.jpg').resize((1000,667)))
        self.imageLabel= Label(self.main_frame, image=self.image,bg='white')
        self.imageLabel.place(x = 0, y= 0)

        # frame 1
        self.frame1 = Frame(self.main_frame,bg='#205950')
        self.frame1.place(x = 450, y= 100,width=500,height=300)

        self.text = 'Assign Batches'
        self.heading = Label(self.frame1,text=self.text,font=('Baskerville',20,'bold'),fg='#FF3AAE',bg='#205950')
        self.heading.place(x=140,y=30,width=200,height=50)

        self.TeacLabel=Label(self.frame1,text='Select Teacher',font=('Rockwell',16),bg='#205950',fg='#F9F37F')
        self.TeacLabel.place(x=30,y=100)
        self.comboValue1 = StringVar()
        self.options = dataBase.ViewnameTeacher()
        self.dropDown1 = Combobox(self.frame1,state='readonly', textvariable=self.comboValue1, values=self.options,font=('Times New Roman',12),)
        self.dropDown1.place(x=210,y=100)

        self.CourseLabel=Label(self.frame1,text='Select Course',font=('Rockwell',16),bg='#205950',fg='#F9F37F')
        self.CourseLabel.place(x=30,y=150)
        self.comboValue2 = StringVar()
        self.options = dataBase.ViewCourses()
        self.dropDown2 = Combobox(self.frame1,state='readonly', textvariable=self.comboValue2, values=self.options,font=('Times New Roman',12),)
        self.dropDown2.place(x=210,y=150)
        self.dropDown2.bind("<<ComboboxSelected>>",self.create)

        self.AddButton=Button(self.frame1,text='Add Now',command=self.login,fg='#FF3A4F',bg='white',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.AddButton.place(x=190,y=240)

        self.root.mainloop()

    def login(self):
        print("slef",self.dropDown3.get())
        self.courseName1 = self.dropDown1.get().split()
        self.courseName2 = self.dropDown2.get().split()
        if self.dropDown3.get()!="":
            self.courseName3 = self.dropDown3.get().split()
            data = (
                self.courseName1[0],
                self.courseName2[0],
                self.courseName3[0],
            )
            if(self.dropDown1.get() == ''):
                messagebox.showerror('Alert ','Enter the Department first')
            elif(self.dropDown2.get() == ''):
                messagebox.showerror('Alert ','Enter the Course first')
            elif(self.dropDown3.get() == ''):
                messagebox.showerror('Alert ','Enter Subject name first')
            else:
                res  = dataBase.addAssign(data)
                if res:
                    print(data)
                    messagebox.showinfo('Success', 'Assigned successfully.')
                    self.root.destroy()
                    obj =view_assign.view_assign()
                    obj.assign()
                else:
                    messagebox.showinfo("Alert","Something went wrong")
        else:
            messagebox.showinfo("Alert","Subject not selected")

if __name__ == "__main__":
    obj = ImageWidget()
    obj.mainFrame()

   