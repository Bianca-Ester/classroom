#CHECAR UTILIDADE

import json
import os
from models.professor import Professor
import utils as ut


CAMINHO_ARQUIVO = "data/professor.json"


def carregar_professores():
    lista_professores = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_professores
        f = open(CAMINHO_ARQUIVO, "r")
        professores = json.load(f)
        for p in professores:
            obj_professor = Professor(**p)
            lista_professores.append(obj_professor)
        return lista_professores
    except Exception as e:
        print(e)
        
        
def salvar_professores(lista):
    try:
        dados = [professor.to_dict() for professor in lista]
        
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
            
        return True
    except Exception as e:
        print(e)
        return False


def adicionar_professor(professor):
    try:
        # le arquivo em formato de adicao (append)
        professores = carregar_professores()
        
        # gera novo id
        proximo_matricula = ut.calcular_proximo_matricula(professor)
        
        # atribui novo id a editora que quer inserir
        professor.matricula = proximo_matricula
            
        # adiciona a nova editora na lista
        professores.append(professor)
                
        # salva a nova lista no arquivo
        return salvar_professores(professores), professor
    except Exception as e:
        print(e)
        return None
    
def buscar_professor_por_matricula(matricula):  
    try:  
        professores = carregar_professores()
        for p in professores:
            if p.matricula == matricula:
                return p
    except Exception as e:
        print(e)
        return None
    
    
def buscar_professor_por_nome(nome):
    try:
        professores = carregar_professores()
        for professor in professores:
            if professor.nome == nome:        
                # se achou um livro com o titulo, retorna o a linha completa do livro
                return professor
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return None


def atualizar_professor(professor):
    try:
        professores = carregar_professores()
        for idx, p in enumerate(professores):
            if p.matricula == professor.matricula:
                professores[idx] = professor
                salvar_professores(professores)
                return True
    except Exception as e:
        print(e)
        return False
    
    
def remover_professor(matricula):
    try:
        professores = carregar_professores()
        novos_professores = []
        for p in professores:
            if p.id != matricula:
                novos_professores.append(p)
        return salvar_professores(novos_professores)
    except Exception as e:
        print(e)
        return False
