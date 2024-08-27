import tkinter as tk
import subprocess
from tkinter import ttk, messagebox, scrolledtext

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
        self.notebook.add(self.tab1, text="Aba 1")
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
        label = tk.Label(self.tab1, text="Scan")
        label.grid(row=0, column=1, padx=5, pady=5)

        # Criar caixa de texto com rolagem
        self.text_box = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)
        self.text_box.grid(row=0, column=1, padx=5, pady=5)

        # Botão para escanear
        button = tk.Button(self.tab1, text="Scanner", command=self.on_button_click_scanner)
        button.grid(row=2, column=1, padx=5, pady=5)

    def create_tab2_content(self):
        # Adicionando conteúdo à Aba 2
        label = tk.Label(self.tab2, text="Conteúdo da Aba 2")
        label.grid(row=0, column=1, padx=5, pady=5)

    def create_tab3_content(self):
        # Adicionando conteúdo à Aba 3
        label = tk.Label(self.tab3, text="Conteúdo da Aba 3")
        label.grid(row=0, column=1, padx=5, pady=5)

###########################################################################################
#####################           FUNÇÕES ABA SCANNER             ###########################
###########################################################################################

    def on_button_click_scanner(self):
        # Função para adicionar informação à caixa de texto
        self.text_box.config(state=tk.NORMAL)
        info = subprocess.run(['pwd'], capture_output=True, text=True)
        output = info.stdout.strip()  # Remove espaços em branco e novas linhas no início e no fim
        self.text_box.insert(tk.END, output)
        self.text_box.config(state=tk.DISABLED)
        self.text_box.see(tk.END) # Rolagem automática até o final
