#CORRIRGIR DIAGRAMA, APLICAR E VER UTILIDADE

from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, senha, matricula, turma):
        super().__init__(nome, senha, matricula)
        self.turma = turma
