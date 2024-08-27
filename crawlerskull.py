import tkinter as tk
from tabs import Tabs

class Application:
    def __init__(self, root):
        # Titulo do software
        # Definir o tamanho da janela principal
        root.title("Aplicativo com abas")
        root.geometry("800x600")

        self.tabs= Tabs(root)        
if __name__ == "__main__":
    # Criando a janela principal
    root = tk.Tk()
    app = Application(root)
    # Iniciando o loop principal
    root.mainloop()