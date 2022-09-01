from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD

import dataBase
import menu
from PIL import Image, ImageTk
import view_Courses


class edit_Courses:

    # constructor
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
        
    def firstFrame(self,data):
        print(data)
        self.data = data
        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.place(x = 0, y = 0,width=1000,height=667)

        self.image = ImageTk.PhotoImage(Image.open('images/sub.jpg').resize((1000,667)))
        self.imageLabel= Label(self.main_frame, image=self.image,bg='white')
        self.imageLabel.place(x = 0, y= 0)
        # frame 1
        self.frame1 = Frame(self.main_frame,bg='white')
        self.frame1.place(x = 270, y= 100,width=500,height=300)

        self.text = 'Add Courses'
        self.heading = Label(self.frame1,text=self.text,font=('Baskerville',20,'bold'),fg='#FF3AAE',bg='white')
        self.heading.place(x=120,y=30,width=300,height=50)
        
        self.SubLabel=Label(self.frame1,text='Courses Name',font=('Rockwell',15),bg='white',fg='#3A85FF')
        self.SubLabel.place(x=30,y=100)

        self.SubEntry=StringVar()
        self.entryWidget1=Entry(self.frame1,textvariable=self.SubEntry,bg='white',font=('Times New Roman',12),width='30')
        self.entryWidget1.place(x=210,y=100)

        self.AddButton=Button(self.frame1,text='Update',command=self.create,fg='red',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.AddButton.place(x=180,y=170)

       

    
        for i in dataBase.editCourses(data):
            print(i)
            self.entryWidget1.insert(0,i[1])

        self.root.mainloop()

    def create(self):
       
        data = (
            self.entryWidget1.get(),
            self.data[0]
            
        )
        if(self.entryWidget1.get() == ''):
            messagebox.showerror('Alert ','Enter Course name first')
        else:
            res  = dataBase.updateCourses_items(data)
            if res:
                print(data)
                messagebox.showinfo('Success', 'UPDATE successfully.')
                self.root.destroy()
                obj = view_Courses.view_Courses()
                obj.Courses()
            else:
                messagebox.showinfo('Alert', 'Please try again.')


if __name__ == '__main__':
    obj =edit_Courses()
    obj.firstFrame("data")
