from tkinter import*
import dataBase
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image , ImageTk
import viewMaterial, menu
from tkinter import filedialog 

class ImageWidget:

    def __init__(self):
        self.root = Tk()
        self.root.title('Edit Material Page')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        
    # def create(self,e): 
    #     self.datavalue=self.dropDown2.get().split()
    #     # print(self.datavalue[0])
    #     val  =(self.datavalue[0],)
    #     print("val",val)
    #     a = dataBase.viewSubname(val)
    #     # print(a)
        
    #     self.comboValue3 = StringVar()
    #     # self.optiondata = ['']
    #     if len(a)>0:
    #         self.optiondata = dataBase.viewSubname(val)
    #     else:
    #         messagebox.showerror("warning",'Subject not Edited yet')
    #         self.optiondata = dataBase.viewSubname(val)
        

    def browseFiles(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

        print(self.filename)

    def mainFrame(self, matId, data):
        print(matId)
        self.matId = matId
        self.data = data

        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.place(x = 0, y = 0,width=1000,height=667)

   
        self.image = ImageTk.PhotoImage(Image.open('images/assign.jpg').resize((1000,667)))
        self.imageLabel= Label(self.main_frame, image=self.image,bg='white')
        self.imageLabel.place(x = 0, y= 0)

        # frame 1
        self.frame1 = Frame(self.main_frame,bg='#205950')
        self.frame1.place(x = 450, y= 100,width=500,height=400)

        self.text = 'Edit Material'
        self.heading = Label(self.frame1,text=self.text,font=('Baskerville',20,'bold'),fg='#FF3AAE',bg='#205950')
        self.heading.place(x=140,y=30,width=200,height=50)

        self.SubLabel=Label(self.frame1,text='Subject Name',font=('Rockwell',16),bg='#205950',fg='#F9F37F')
        self.SubLabel.place(x=30,y=150)

        self.dropDown3=Combobox(self.frame1, font=('Times New Roman',12))
        self.dropDown3.place(x=210,y=150)

        self.fileLabel = Label(self.frame1, text='Material', font=('Rockwell',16),bg='#205950',fg='#F9F37F').place(x=30, y=200)

        button_explore = Button(self.frame1, text = "Choose File", font=('Rockwell',16),bg='#205950',fg='#F9F37F', command = self.browseFiles).place(x = 210, y = 200)

        self.titleLabel = Label(self.frame1, text='Title', font=('Rockwell',16),bg='#205950',fg='#F9F37F').place(x=30, y=250)

        self.titleEntry = Entry(self.frame1)
        self.titleEntry.place(x = 210, y = 250)

        self.descLabel = Label(self.frame1, text='Description', font=('Rockwell',16),bg='#205950',fg='#F9F37F').place(x=30, y=300)

        self.descEntry = Entry(self.frame1)
        self.descEntry.place(x = 210, y = 300)




        self.AddButton=Button(self.frame1,text='Edit Now',command=self.login,fg='#FF3A4F',bg='white',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.AddButton.place(x=190,y=350)

        self.BackButton=Button(self.frame1,text='Back',command=self.back,fg='#FF3A4F',bg='white',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.BackButton.place(x=300,y=350)


        res = dataBase.getMaterial(self.matId)
        if res:
            self.dropDown3.insert(0, (res[0], res[1]))
            self.titleEntry.insert(0, res[3])
            self.descEntry.insert(0, res[4])

            self.dropDown3.configure(state='readonly')

        else:
            messagebox.showerror('Error', 'Something went wrong.')

        self.root.mainloop()

    def back(self):
        self.root.destroy()
        obj = menu.menubar()
        obj.firstFrame(self.data)

    def login(self):
        print("slef",self.dropDown3.get())
        if self.dropDown3.get() != "":
            self.courseName3 = self.dropDown3.get().split()
            data = (
                self.filename, 
                self.titleEntry.get(),
                self.descEntry.get(),
                self.matId[0]
            )
            print(data)
            if(self.dropDown3.get() == ''):
                messagebox.showerror('Alert ','Enter Subject name first')
            elif(self.titleEntry.get() == ''):
                messagebox.showerror('Alert ','Enter title first')
            elif(self.descEntry.get() == ''):
                messagebox.showerror('Alert ','Enter description first')
            else:
                pass
                res  = dataBase.editMaterial(data)
                if res:
                    print(data)
                    messagebox.showinfo('Success', 'Material updated successfully.')
                    self.root.destroy()
                    obj =viewMaterial.view_assign()
                    obj.assign(self.data)
                else:
                    messagebox.showinfo("Alert","Something went wrong")
        else:
            messagebox.showinfo("Alert","Subject not selected")

if __name__ == "__main__":
    obj = ImageWidget()
    obj.mainFrame()

   