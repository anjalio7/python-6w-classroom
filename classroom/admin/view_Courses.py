from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import menu
import editCourses
import dataBase
import view_Courses
class view_Courses():
    # constructor
    def __init__(self):
        self.root = Toplevel()
        self.root.title('view_Courses')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def Courses(self):
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="1000", height="667")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C'), selectmode="extended")

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Courses Name")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="Edit")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Delete")
        self.tr.column('#3', minwidth=0, width=80, stretch=NO)

        data = dataBase.ViewCourses()
        for i in data:
            self.tr.insert('', 0, text = i[0], values=(i[1],"Edit","Delete"))

        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,height=667,width= 1000)
        self.root.mainloop() 

    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'col {col}')
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#3':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                a = dataBase.deleteCourses(gup)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    obj = view_Courses()
                    obj.Courses()
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col == '#2':
            self.root.destroy()
            obj = editCourses.edit_Courses()
            obj.firstFrame(gup)
   
if __name__ == '__main__':
    obj = view_Courses()
    obj.Courses()
