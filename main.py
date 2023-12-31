import tkinter as tk
from tkinter import *
from tkinter import ttk

# Cria a janela principal
root = tk.Tk()

# Classe que define a aplicação
class Application():
    def __init__(self, root):
        self.root = root
        self.tela()  # Configurações da janela
        self.frames_de_tela()  # Criação dos frames na janela
        self.widgets_frame1()  # Criação dos widgets da 1º tela
        self.lista_frame2() #Criação do treeviewer na 2º tela
        root.mainloop()

    def tela(self):
        # Configurações da janela principal
        self.root.title("Software de cadastro")
        self.root.configure(background='#1e3743')
        self.root.geometry("1200x1080")
        self.root.resizable(True, True)
        self.root.maxsize(width=1200, height=1080)
        self.root.minsize(width=800, height=600)

    def frames_de_tela(self):
        # Criação de dois frames na janela
        self.frame_1 = Frame(self.root, bd=4, bg='#eeeeee', highlightbackground='#0000FF', highlightthickness=3)
        self.frame_1.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.48)

        self.frame_2 = Frame(self.root, bd=4, bg='#eeeeee', highlightbackground='#0000FF', highlightthickness=3)
        self.frame_2.place(relx=0.01, rely=0.4, relwidth=0.98, relheight=0.49)
    

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
        #Configuração label Código
        novo_label_0 = Label(self.frame_1, text = "Código")
        novo_label_0.place(relx = 0.0, rely = 0.13)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.13, relwidth=0.05)
       
        # Configuração label Razão Social
        novo_label_1 = Label(self.frame_1, text = "Razão Social")
        novo_label_1.place(relx = 0.00, rely = 0.2)

        self.razao_entry = Entry(self.frame_1)
        self.razao_entry.place(relx=0.07, rely=0.20, relwidth=0.15)

        # Configuração label CNPJ
        novo_label_2 = Label(self.frame_1, text = "Cnpj")
        novo_label_2.place(relx = 0.0, rely = 0.27)

        self.cnpj_entry = Entry(self.frame_1)
        self.cnpj_entry.place(relx=0.04, rely=0.27, relwidth=0.15)

        # Configuração Dados DO Relogio
        novo_label_3 = Label(self.frame_1, text = "DADOS DO RELOGIO")
        novo_label_3.place(relx = 0.00, rely = 0.36)

        # Configuração Modelo
        novo_label_4 = Label(self.frame_1, text = "Modelo")
        novo_label_4.place(relx = 0.00, rely = 0.45)
        
        self.modelo_entry = Entry(self.frame_1)
        self.modelo_entry.place(relx=0.05, rely=0.45, relwidth=0.15)

        # Configuração Serial
        novo_label_5 = Label(self.frame_1, text = "Serial")
        novo_label_5.place(relx = 0.00, rely = 0.52)
        
        self.serial_entry = Entry(self.frame_1)
        self.serial_entry.place(relx=0.04, rely=0.52, relwidth=0.15)

        # Configuração (Inicio da manutenção)
        novo_label_6 = Label(self.frame_1, text = "Data de inicio")
        novo_label_6.place(relx = 0.00, rely = 0.60)
        
        self.data_inicio = Entry(self.frame_1)
        self.data_inicio.place(relx=0.07, rely=0.60, relwidth=0.10)





       ## Configuração de colunas na treeviewer
    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, column=("col1", "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Empresa")
        self.listaCli.heading("#3", text="telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width=0)
        self.listaCli.column("#1", width=50)
        self.listaCli.column("#2", width=100)
        self.listaCli.column("#3", width=125)
        self.listaCli.column("#4", width=125)

        relx_centered = (1 - 0.96) / 2  # (1 - relwidth) / 2
        rely_centered = (1 - 0.85) / 2  # (1 - relheight) / 2

        self.listaCli.place(relx=relx_centered, rely=rely_centered, relwidth=0.94, relheight=0.90)




# Instanciação da aplicação
Application(root)
