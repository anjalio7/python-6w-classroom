from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import menu
import editTeacher
import dataBase
import viewTeacher
class viewTeacher():
    # constructor
    def __init__(self):
        self.root = Toplevel()
        self.root.title('view_Teacher')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def Teacher(self):
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="1000", height="667")

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C','D','E','F','G'), selectmode="extended")

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Teacher Name")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="Teacher Age")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Teacher Qualification")
        self.tr.column('#3', minwidth=0, width=150, stretch=NO)

        self.tr.heading('#4', text="Username")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#5', text="Password")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)

        self.tr.heading('#6', text="Edit")
        self.tr.column('#6', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#7', text="Delete")
        self.tr.column('#7', minwidth=0, width=80, stretch=NO)

        data = dataBase.ViewTeacher()
        for i in data:
            # print(i)
            self.tr.insert('', 0, text = i[0], values=(i[1],i[2],i[3],i[4],i[5],"Edit","Delete"))

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
        if col == '#7':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                a = dataBase.deleteTeacher(gup)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    obj = viewTeacher()
                    obj.Teacher()
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col == '#6':
            self.root.destroy()
            obj = editTeacher.ImageWidget()
            obj.mainFrame(gup)
   
if __name__ == '__main__':
    obj = viewTeacher()
    obj.Teacher()
