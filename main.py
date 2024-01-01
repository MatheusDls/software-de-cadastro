import tkinter as tk
from tkinter import *

# Cria a janela principal
root = tk.Tk()

# Classe que define a aplicação
class Application():
    def __init__(self, root):
        self.root = root
        self.tela()  # Configurações da janela
        self.frames_de_tela()  # Criação dos frames na janela
        self.widgets_frame1()  # Criação dos widgets da 1º tela
        root.mainloop()

    def tela(self):
        # Configurações da janela principal
        self.root.title("Software de cadastro")
        self.root.configure(background='#1e3743')
        self.root.geometry("1600x1080")
        self.root.resizable(True, True)
        self.root.maxsize(width=1920, height=1080)
        self.root.minsize(width=800, height=600)

    def frames_de_tela(self):
        # Criação de dois frames na janela
        self.frame_1 = Frame(self.root, bd=4,
                             highlightbackground='#0000FF', highlightthickness=3)
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)

        self.frame_2 = Frame(self.root, bd=4,
                             highlightbackground='#0000FF', highlightthickness=3)
        self.frame_2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.49)
    
    def widgets_frame1(self):
        ## Criação do botão Incluir 
        self.bt_Incluir_Cadastro = Button(self.frame_1, text="INCLUIR CADASTRO", command=self.mostrar_label)
        self.bt_Incluir_Cadastro.place(relx=0.0, rely=0.0, relwidth=0.1, relheight=0.10)

        ## Criação do botão Buscar 
        self.bt_Buscar_Cadastro = Button(self.frame_1, text="BUSCAR CADASTRO")
        self.bt_Buscar_Cadastro.place(relx=0.1, rely=0.0, relwidth=0.1, relheight=0.10)

        ## Criação do botão Relatorio 
        self.bt_relatorio = Button(self.frame_1, text="RELATORIO")
        self.bt_relatorio.place(relx=0.2, rely=0.0, relwidth=0.1, relheight=0.10)

        ## Criação do botão Ajuda 
        self.bt_ajuda = Button(self.frame_1, text="AJUDA")
        self.bt_ajuda.place(relx=0.3, rely=0.0, relwidth=0.1, relheight=0.10)
        
        ## definindo função de click ao botão (Incluir Cadastro)
    def mostrar_label(self):
        novo_label = Label(self.frame_1, text = "Código")
        novo_label.place(relx = 0.0, rely = 0.13)

# Instanciação da aplicação
Application(root)
