"""
Buscar turma: matricula
Botão: entrar (só aparecer depois da busca)
"""
from tkinter import Frame, Label, Entry, Button, Menu, ttk, CENTER

class JanelaAcessarTurma:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)


        
    def limpar_campos(self):
        self.entrada_nome.delete(0 ,'end')
        self.entrada_matricula.delete(0 ,'end')
        self.entrada_senha.delete(0, 'end')
        
        self.entrada_nome.focus()

    def cadastrar_professor(self):
        self.limpar_campos()
        #terminar

    def cadastrar_aluno(self):
        self.limpar_campos()
        #terminar
