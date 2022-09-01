from tkinter import*
import dataBase
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image , ImageTk
import viewMaterial, menu
from tkinter import filedialog 

class ImageWidget:

    def __init__(self):
        self.root = Toplevel()
        self.root.title('Add Material Page')
        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()


        self.width = int((self.fullwidth-1000)/2)
        self.height=int((self.fullheight-400)/2)

        s = "1000x400+" +str(self.width)+ "+" +str(self.height)

        self.root.resizable(height=False,width=False)
        
        self.root.geometry(s)

    def mainFrame(self, matId):
        self.text = Text(self.root)
        self.text.place(x = 0, y = 0, width=1000, height=400)

        self.id = matId
        fileLoc  = dataBase.getFileAssign(matId)

        with open(fileLoc[0], 'r') as file:
            stuff = file.read()
            self.text.insert(END, stuff)

        
if __name__ == '__main__':
    obj  = ImageWidget()
    obj.mainFrame()