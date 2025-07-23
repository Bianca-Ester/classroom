#configurar funções

from tkinter import Frame, Label, Entry, Button, CENTER

class JanelaAcessarTurma:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_matricula = Label(janela, text="Matrícula:")
        label_matricula.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        self.entrada_matricula = Entry(janela)
        self.entrada_matricula.grid(row=0, column=1, sticky="W", padx=5, pady=5)
        self.entrada_matricula.focus()

        self.botao = Button(janela, text="Buscar", command=self.buscar_turma)
        self.botao.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.label_matricula_resultado = Label(janela)
        self.label_matricula_resultado.grid(row=2, column=0, padx=5, pady=5, columnspan=2)

        self.botao_acessar = Button(janela, text="Acessar", command=self.acessar_turma, state="disabled")
        self.botao_acessar.grid(row=6, column=0, sticky="E", padx=5, pady=5)

        self.botao_remover = Button(self.frame, text="Remover", command=self.remover_turma, state='disabled')
        self.botao_remover.grid(row=6, column=1, sticky='W', padx=5, pady=5)

    def limpar_campos(self):
        self.entrada_matricula.delete(0 ,'end')        
        self.entrada_matricula.focus()

    def buscar_turma(self):
        self.limpar_campos()
        #terminar

    def acessar_turma(self):
        self.limpar_campos()
        #terminar

    def remover_turma(self):
        self.limpar_campos()
        #terminar
