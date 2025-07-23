from tkinter import Tk, Menu
from janelas.janela_cadastro import JanelaCadastro
from janelas.janela_login import JanelaLogin

class JanelaPrincipal:
    def __init__(self):
        self.janela = Tk()   
        self.janela.title("Virtual ClassRoom")

        self.menu_bar = Menu(self.janela)
        self.janela.config(menu=self.menu_bar)

        self.menu_bar.add_command(label="Cadastro", command=self.abrir_janela_cadastro)
        self.menu_bar.add_command(label="Login", command=self.abrir_janela_login)
        self.menu_bar.add_command(label="Sair", command=self.janela.quit)

        self.centralizar_janela()
        self.janela.mainloop()

    def centralizar_janela(self):
        largura = 350
        altura = 300
        largura_tela = self.janela.winfo_screenwidth()
        altura_tela = self.janela.winfo_screenheight()

        x = (largura_tela // 2) - (largura // 2)
        y = (altura_tela // 2) - (altura // 2)

        self.janela.geometry(f"{largura}x{altura}+{x}+{y}")

    def limpar_widgets(self):
        if len(self.janela.winfo_children()) > 1:
            self.janela.winfo_children()[1].destroy()

    def abrir_janela_cadastro(self):
        self.limpar_widgets()
        JanelaCadastro(self.janela)

    def abrir_janela_login(self):
        self.limpar_widgets()
        JanelaLogin(self.janela)
