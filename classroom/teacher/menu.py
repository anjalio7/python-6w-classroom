from tkinter import *
from PIL import Image, ImageTk
import addMaterial, viewMaterial
import addAssignment, viewAssignment


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

    def firstFrame(self, data):

        self.data = data

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

        Task = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Material', menu = Task)
        Task.add_command(label =' Add Material', command = self.openAddMaterial)
        Task.add_command(label =' Manage Material', command = self.openManageMaterial)
        
        # Adding food types Menu and commands

        Subject = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label ='Assignment', menu = Subject)
        Subject.add_command(label =' Add Assignment', command = self.openAddAssign)
        Subject.add_command(label =' Manage Assignment', command = self.openManageAssign)

        menubar.add_command(label="Logout",command=self.root.destroy)

        # display Menu
        self.root.config(menu = menubar)
        self.root.mainloop()
        
    def openAddMaterial(self):
        self.root.destroy()
        obj = addMaterial.ImageWidget()
        obj.mainFrame(self.data)


    def openManageMaterial(self): 
        self.root.destroy()
        obj = viewMaterial.view_assign()
        obj.assign(self.data)

    def openAddAssign(self):
        self.root.destroy()
        obj = addAssignment.ImageWidget()
        obj.mainFrame(self.data)

    def openManageAssign(self):
        self.root.destroy()
        obj = viewAssignment.view_assign()
        obj.assign(self.data)


if __name__ == '__main__':
    obj = menubar()
    obj.firstFrame()