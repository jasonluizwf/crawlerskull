import tkinter as tk
import requests
from tkinter import ttk, messagebox, scrolledtext
from bs4 import BeautifulSoup


class Tabs:
    def __init__(self, root):
        self.root = root # Armazena a referência ao root
        # Criando o Notebook (abas)
        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=0, column=0, sticky="nsew") # Usando grid para o Notebook

        # Configurando as linhas e colunas da janela principal para expandir com o Notebook
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Criando as abas
        self.create_tabs()
        
    def create_tabs(self):
        # Criando quantidade de abas
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)

        # Adicionando as abas ao Notebook
        self.notebook.add(self.tab1, text="GET HTML")
        self.notebook.add(self.tab2, text="Aba 2")
        self.notebook.add(self.tab3, text="aba 3")

        # Adicionando conteúdo às abas
        self.create_tab1_content()
        self.create_tab2_content()
        self.create_tab3_content()

###########################################################################################
#########################         CONTEÚDO DAS ABAS           #############################
###########################################################################################

    def create_tab1_content(self):
        # Adicionando conteúdo à Aba 1
        self.label = tk.Label(self.tab1, text="URL")
        self.label.place(x=135, y=10)

        # Campo url
        self.campo_texto_url = tk.Entry(self.tab1, width=30)
        self.campo_texto_url.place(x=30,y=30)

        # Botão para escanear
        self.button = tk.Button(self.tab1, text="Scanner", command=self.on_button_click_scanner, width=5, height=1)
        self.button.place(x=120, y=60)

        # Criar caixa de texto com rolagem
        self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)
        self.text_box.place(x=300, y=50, relwidth=0.6, relheight=0.2)

    def create_tab2_content(self):
        # Adicionando conteúdo à Aba 2
        self.label = tk.Label(self.tab2, text="Conteúdo da Aba 2")
        self.label.place(x=50, y=50, relwidth=0.2, relheight=0.2)

    def create_tab3_content(self):
        # Adicionando conteúdo à Aba 3
        self.label = tk.Label(self.tab3, text="Conteúdo da Aba 3")
        self.label.place(x=50, y=50, relwidth=0.2, relheight=0.2)

###########################################################################################
#####################           FUNÇÕES ABA SCANNER             ###########################
###########################################################################################

    def on_button_click_scanner(self):
        url = self.campo_texto_url.get()
        if url == "":
            self.aviso_url_em_branco()
        else:
            self.response = requests.get(url)
            if self.response.status_code == 200:
                html_recebido = self.response.text
                html_formatado = BeautifulSoup(html_recebido, 'html.parser').prettify()
                self.text_box.config(state=tk.NORMAL)
                self.text_box.insert(tk.END, html_formatado)
                self.text_box.config(state=tk.DISABLED)
                self.text_box.see(tk.END) # Rolagem automática até o final
            else:
                self.url_invalida()

    def aviso_url_em_branco(self):
        messagebox.showwarning("Aviso", "É necessário inserir uma URL")

    def url_invalida(self):
        messagebox.showerror("URL inválida", "É necessario verificar a URL ou a página web. Status code:", self.response.status_code)