#CORRIRGIR DIAGRAMA, APLICAR E VER UTILIDADE

class Pessoa:
    def __init__(self, nome, senha, matricula):
        self.nome = nome
        self.__senha = senha
        self.matricula = matricula

    def to_dict(self):
        return{
            'id': self.id,
            'nome': self.nome,
            'senha': self.__senha,
            'matricula': self.matricula
        }
    
    def cadastrar_pessoa(self, nome, matricula, senha):
            pass

    def get_pessoa(self, matricula):
            pass
