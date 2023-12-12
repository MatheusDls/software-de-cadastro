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
        self.criando_botoes()  # Criação dos botões
        root.mainloop()

    def tela(self):
        # Configurações da janela principal
        self.root.title("Software de cadastro")
        self.root.configure(background='#1e3743')
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.root.maxsize(width=1000, height=800)
        self.root.minsize(width=400, height=300)

    def frames_de_tela(self):
        # Criação de dois frames na janela
        self.frame_1 = Frame(self.root, bd=4,
                             highlightbackground='#0000FF', highlightthickness=3)
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)

        self.frame_2 = Frame(self.root, bd=4,
                             highlightbackground='#0000FF', highlightthickness=3)
        self.frame_2.place(relx=0.01, rely=0.5, relwidth=0.98, relheight=0.49)

    def criando_botoes(self):
        ## Criação do botão Limpar 
        self.bt_limpar = Button(self.frame_1, text="Limpar")
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        
        ## Criação do botão Buscar 
        self.bt_buscar = Button(self.frame_1, text="Buscar")
        self.bt_buscar.place(relx=0.4, rely=0.2, relwidth=0.1, relheight=0.15)
       
        ## Criação do botão Novo 
        self.bt_botao_novo = Button(self.frame_1, text="Novo")
        self.bt_botao_novo.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.15)
       
        ## Criação do botão alterar 
        self.bt_alterar = Button(self.frame_1, text="Alterar")
        self.bt_alterar.place(relx=0.6, rely=0.2, relwidth=0.1, relheight=0.15)
        
        ## Criação do botão apagar 
        self.bt_apagar = Button(self.frame_1, text="Apagar")
        self.bt_apagar.place(relx=0.7, rely=0.2, relwidth=0.1, relheight=0.15)
    

# Instanciação da aplicação
Application(root)
