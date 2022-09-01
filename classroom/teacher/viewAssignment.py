from tkinter import *
from tkinter.ttk import Treeview
from tkinter import messagebox
import menu
import editAssignment, detailAssignment
import dataBase
class view_assign():
    # constructor
    def __init__(self):
        self.root = Tk()
        self.root.title('view_Assigns')

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    def assign(self, data):
        self.data = data
        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="1000", height="667")

        self.backBtn = Button(self.fr, text='Back', command=self.back).place(x = 0, y = 620)

        self.tr = Treeview(self.fr, columns=('A', 'B', 'C','D','E', 'F'), selectmode="extended")

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


        self.tr.heading('#5', text="Edit")
        self.tr.column('#5', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#6', text="Delete")
        self.tr.column('#6', minwidth=0, width=80, stretch=NO)

        
        data = dataBase.viewassignments(self.data)
        print(data)
        if len(data)>0:
            for i in data:
                self.tr.insert('', 0, text = i[0], values=(i[1], i[3], i[4] ,i[2],"Edit","Delete"))

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
        if col == '#4':
            obj = detailAssignment.ImageWidget()
            obj.mainFrame(gup)
        if col == '#6':
            res = messagebox.askyesno("Delete", "Do You Realy Want to delete this item.")
            if res:
                a = dataBase.deleteassignments(gup)
                if a:
                    messagebox.showinfo("Success","Deleted Successfully")
                    self.root.destroy()
                    obj = view_assign()
                    obj.assign(self.data)
                else:
                    messagebox.showinfo("Alert","Something went wrong")

        if col == '#5':
            self.root.destroy()
            obj = editAssignment.ImageWidget()
            obj.mainFrame(gup, self.data)

    def back(self):
        self.root.destroy()
        obj = menu.menubar()
        obj.firstFrame(self.data)
   
if __name__ == '__main__':
    obj = view_assign()
    obj.assign()
