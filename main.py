import tkinter as tk
from tkinter import *

root = tk.Tk()
class Application():
    def __init__(self,root):
        self.root = root
        self.tela()
        self.frames_de_tela()
        root.mainloop()
    def tela(self):
        self.root.title("Cadastro de Manutenção SistemPonto")
        self.root.configure(background='#1e3743')
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=1000, height=800)
        self.root.minsize(width=400, height=300)

    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd=4,
                             highlightbackground = '#0000FF', highlightthickness = 3)
        self.frame_1.place(relx= 0.01, rely=0.01, relwidth= 0.98, relheight= 0.48)

        self.frame_2 = Frame(self.root, bd=4,
                             highlightbackground='#0000FF', highlightthickness=3)
        self.frame_2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.49)





Application(root)












