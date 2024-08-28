import tkinter as tk
import importlib
from tabs import Tabs

class Application:
    def __init__(self, root):
        # Titulo do software
        root.title("Aplicativo com abas")
        # Definir a geometria da janela para preencher a tela menos a barra de tarefas
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}")
        # Definir o tamanho da janela principal
        root.minsize(1280,720)
        self.tabs= Tabs(root)        
if __name__ == "__main__":
    # Criando a janela principal
    root = tk.Tk()
    app = Application(root)
    # Iniciando o loop principal
    root.mainloop()