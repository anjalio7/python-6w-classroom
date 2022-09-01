from tkinter import *
from PIL import Image, ImageTk
import add_courses,view_Courses
import add_subject,viewSubject
import add_teacher,viewTeacher

import add_assign, view_assign
import viewMaterial, viewAssignment

class menubar:

    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('Menu Demonstration')

        # Creating Menubar
        menubar = Menu(self.root)
        
        # to get the width and height of your computer screen
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()

        # 1000 x 667 is the size of your screen

        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)
        # s = "200x200"

        # so screen cant be resized
        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def firstFrame(self):

         # create a frame
        self.mainFrame = Frame(self.root,bg="white")
        self.mainFrame.place(x = 0, y = 0, width="350", height="667")

        # set background image
        self.img=Image.open('images/coaching.jpg')
        self.resize_image = self.img.resize((1000, 667))
        self.image = ImageTk.PhotoImage(self.resize_image)
        self.bgLabel = Label(self.root, image=self.image)
        self.bgLabel.config(bg="white")
        self.bgLabel.place(x = 0, y = 0)
       
       
        menubar=Menu(self.mainFrame)

        # Adding course Menu and commands

        course = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Courses', menu = course)
        course.add_command(label =' Add Course', command = self.openAddcourse)
        course.add_command(label =' Manage Course', command = self.openManagecourse)
        
        # Adding food types Menu and commands

        Subject = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Subject', menu = Subject)
        Subject.add_command(label =' Add Subject', command = self.opensub)
        Subject.add_command(label =' Manage Subject', command = self.openManagesub)

        
        Teacher = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Teacher', menu = Teacher)
        Teacher.add_command(label ='Add Teacher', command = self.openAddTeacher)
        Teacher.add_command(label ='manage Teacher', command = self.openManageTeacher)
       
        # Adding food Menu and commands
        Assign = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Assign', menu = Assign)
        Assign.add_command(label ='Add Assign', command = self.openAddAssign)
        Assign.add_command(label ='manage Assign', command = self.openManageAssign)

        Material = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Material', menu = Material)
        Material.add_command(label ='View', command = self.openMat)

        Assignment = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Assignment', menu = Assignment)
        Assignment.add_command(label ='View', command = self.openMat)

        menubar.add_command(label="Logout",command=self.root.quit)

        # display Menu
        self.root.config(menu = menubar)
        self.root.mainloop()
        
    def openAddcourse(self):
        obj =add_courses.ImageWidget()
        obj.mainFrame()
   
    def openManagecourse(self): 
        obj = view_Courses.view_Courses()
        obj.Courses()

    def opensub(self):
        obj = add_subject.ImageWidget()
        obj.mainFrame() 

    def openManagesub(self):
        obj = viewSubject.viewSubject()
        obj.Subject()

    def openAddTeacher(self):
        obj =add_teacher.ImageWidget()
        obj.mainFrame()

    def openManageTeacher(self):
        obj = viewTeacher.viewTeacher()
        obj.Teacher()

    def openAddAssign(self):
        obj =add_assign.ImageWidget()
        obj.mainFrame()
        
    def openManageAssign(self):
        obj = view_assign.view_assign()
        obj.assign()

    def openMat(self):
        obj = viewMaterial.view_assign()
        obj.assign()
    
    def openAssign(self):
        obj = viewAssignment.view_assign()
        obj.assign()

if __name__ == '__main__':
    obj = menubar()
    obj.firstFrame()