#configurar função

from tkinter import Frame, Label, Entry, Button, CENTER

class JanelaCadastrarTurma:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_nome_turma = Label(janela, text="Turma:")
        label_nome_turma.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        self.entrada_turma = Entry(janela)
        self.entrada_turma.grid(row=0, column=1, sticky="W", padx=5, pady=5)
        self.entrada_turma.focus()

        label_codigo_turma = Label(janela, text="Código:")
        label_codigo_turma.grid(row=1, column=0, sticky="E", padx=5, pady=5)

        self.entrada_codigo = Entry(janela)
        self.entrada_codigo.grid(row=1, column=1, sticky="W", padx=5, pady=5)

        self.botao = Button(janela, text="Cadastrar", command=self.cadastrar_turma)
        self.botao.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

    def limpar_campos(self):
        self.entrada_turma.delete(0 ,'end')        
        self.entrada_codigo.delete(0 ,'end')

        self.entrada_turma.focus()

    def cadastrar_turma(self):
        self.limpar_campos()
        #terminar
