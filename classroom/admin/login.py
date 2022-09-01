from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import dataBase
import menu
from turtle import bgcolor
from PIL import Image , ImageTk

class ImageWidget:

    def __init__(self):
        self.root = Tk()
        self.root.title('Login Page')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-667)/2)

        s = "1000x667+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)
        

    def mainFrame(self):
        self.main_frame = Frame(self.root, bg='#FADD4C')
        self.main_frame.place(x = 0, y = 0,width=1000,height=667)

        # placing images
        self.image = ImageTk.PhotoImage(Image.open('images/bg1.jpg').resize((1000,667)))
        self.imageLabel = Label(self.main_frame, image=self.image,bg='black')
        self.imageLabel.place(x = 0, y= 0)


        # self.image1 = ImageTk.PhotoImage(Image.open('images/login-.png').resize((100,100)))
        # self.imageLabel1 = Label(self.main_frame, image=self.image1,bg='black')
        # self.imageLabel1.place(x = 450, y= 150)
        


        # frame 1
        self.frame1 = Frame(self.main_frame,bg='white')
        self.frame1.place(x = 340, y= 90,width=400,height=500)

        
        self.image1 = ImageTk.PhotoImage(Image.open('images/138-user.png').resize((400,150)))
        self.imageLabel1 = Label(self.frame1, image=self.image1,bg='white')
        self.imageLabel1.place(x = 0, y= 0)

        self.text = 'Log In'
        self.heading = Label(self.frame1,text=self.text,font=('yu gothic ui',25,'bold'),fg='black',bg='white')
        self.heading.place(x=100,y=160,width=200,height=50)




    def entryMethod(self):

        
        self.UserLabel=Label(self.frame1,text='Username',font=('Rockwell',12),bg='white')
        self.UserLabel.place(x=70,y=280)

        self.entryValue=StringVar()
        self.entryWidget=Entry(self.frame1,textvariable=self.entryValue,bg='white')

        self.entryWidget.place(x=170,y=280)

        self.UserPass=Label(self.frame1,text='Password',font=('Rockwell',12),bg='white')
        self.UserPass.place(x=70,y=330)

        self.entryPass=StringVar()
        self.entryWidget1=Entry(self.frame1,textvariable=self.entryPass,show='*',bg='white')

        self.entryWidget1.place(x=170,y=330)

        self.loginButton=Button(self.frame1,text='Login',command=self.login,fg='#900C3F',activebackground='blue',activeforeground='white',font=('Comic Sans MS',13))
        self.loginButton.place(x=170,y=400)

        self.root.mainloop()

    def login(self):
        self.data=(
            self.entryWidget.get(),
            self.entryWidget1.get()
        )

        if(self.entryWidget.get()==''):
            messagebox.showinfo('Alert','Enter your username')
        elif(self.entryWidget1.get()==''):
            messagebox.showinfo('Alert','Enter your password')
        else:
            res = dataBase.login(self.data)
            if res:
                messagebox.showinfo("Success","Login successful")
                self.root.destroy()
                obj = menu.menubar()
                obj.firstFrame()

            else:
                # print(self.data)
                messagebox.showerror('Alert','Invalid Username/Password')
    
    
if __name__ == "__main__":
    obj = ImageWidget()
    obj.mainFrame()
    obj.entryMethod()
