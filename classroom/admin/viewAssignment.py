from tkinter import *
from tkinter.ttk import Combobox, Treeview
from tkinter import messagebox
import menu
import detailAssignment
import dataBase
class view_assign():
    # constructor
    def __init__(self):
        self.root = Toplevel()
        self.root.title('view_Assigns')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def assign(self):

        a = dataBase.allTeachers().append('All')
        self.options = dataBase.allTeachers()
        self.teachDrop = Combobox(self.root, values=self.options)
        self.teachDrop.pack()
        self.teachDrop.bind("<<ComboboxSelected>>", lambda type = 'filter': self.allTable(type))
        
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=50, width="1000", height="667")

        self.allTable('all')

        self.root.mainloop() 

    def allTable(self, type):
        self.tr = Treeview(self.fr, columns=('A', 'B', 'C','D','E'), selectmode="extended")
        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=0, width=50, stretch=NO)

        self.tr.heading('#1', text="Subject")
        self.tr.column('#1', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#2', text="Title")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Description")
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#4', text="Assignment")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)


        if type == 'all':
       
            data = dataBase.viewassignments()
            print(data)
            if len(data)>0:
                for i in data:
                    self.tr.insert('', 0, text = i[0], values=(i[1], i[3], i[4] ,i[2]))
        else:
            a = self.teachDrop.get().split()
            data = dataBase.getFilterAssign(a[0])
            if len(data)>0:
                for i in data:
                    self.tr.insert('', 0, text = i[0], values=(i[1], i[3], i[4] ,i[2]))
        

        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0, y=0,height=667,width= 1000)


    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'col {col}')
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#4':
            obj = detailAssignment.ImageWidget()
            obj.mainFrame(gup)

    def back(self):
        self.root.destroy()
        obj = menu.menubar()
        obj.firstFrame(self.data)
   
if __name__ == '__main__':
    obj = view_assign()
    obj.assign()
