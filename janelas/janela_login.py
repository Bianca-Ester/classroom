#CONFIGURAR, tendo por base 'janela_cadastro.py'

from tkinter import Frame, Label, Entry, Button, ttk, CENTER

class JanelaLogin:
    def __init__(self, janela):
        self.frame = Frame(janela, width=420, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label_nome = Label(self.frame, text="Nome: ")
        label_nome.grid(row=0, column=0, sticky="E", padx=5, pady=5)

        self.entrada_nome = Entry(self.frame)
        self.entrada_nome.grid(row=0, column=1, sticky="W", padx=5, pady=5)
        self.entrada_nome.focus()

        label_matricula = Label(self.frame, text="Matrícula:")
        label_matricula.grid(row=1, column=0, sticky="E", padx=5, pady=5)

        self.entrada_matricula = Entry(self.frame)
        self.entrada_matricula.grid(row=1, column=1, sticky="W", padx=5, pady=5)

        label_senha = Label(self.frame, text="Senha:")
        label_senha.grid(row=2, column=0, sticky="E", padx=5, pady=5)

        self.entrada_senha = Entry(self.frame)
        self.entrada_senha.grid(row=2, column=1, sticky="W", padx=5, pady=5)

        opcoes = ["Aluno", "Professor"]
        combobox = ttk.Combobox(janela, values=opcoes)
        combobox.grid(row=3, column=0, padx=5, pady=5, columnspan=2)
        combobox.set("Selecione uma opção")

        recuperacao_combobox = combobox.get()
        
        if recuperacao_combobox == "Professor":
            botao = Button(self.frame, text="Login", command=self.abrir_janela_principal_professor)
            botao.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

        elif recuperacao_combobox == "Aluno":
            botao = Button(self.frame, text="Login", command=self.abrir_janela_principal_aluno)
            botao.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

        else:
            erro = messagebox.showerror('Erro','Preencha todos os campos')
        
    def limpar_campos(self):
        self.entrada_nome.delete(0 ,'end')
        self.entrada_matricula.delete(0 ,'end')
        self.entrada_senha.delete(0, 'end')
        
        self.entrada_nome.focus()

    def abrir_janela_principal_professor(self):
        self.limpar_campos()
        #Adicionar verificação antes de abrir
        #messagebox

    def abrir_janela_principal_aluno(self):
        self.limpar_campos()
        #Adicionar verificação antes de abrir
        #messagebox
