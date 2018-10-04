import tkinter as tk



class GenericWindow:
    def __init__(self,title,size):
        self.title = title
        self.size = size

    def WindowSetup(self):
        self.root = tk.Tk()
        self.root.title(self.title)
        self. root.geometry(self.size)
        self.root.mainloop()
        
    def AddButton(self):
        b = tk.Button(self.root, text="OK")
        b.pack()



mainWindow = GenericWindow("windows","320x200")
mainWindow.WindowSetup()
mainWindow.AddButton()



