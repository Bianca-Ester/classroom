#CHECAR UTILIDADE

import json
import os
from models.aluno import Aluno
import utils as ut


CAMINHO_ARQUIVO = "data/aluno.json"


def carregar_alunos():
    lista_alunos = []
    try:
        if not os.path.exists(CAMINHO_ARQUIVO):
            return lista_alunos
        f = open(CAMINHO_ARQUIVO, "r")
        alunos = json.load(f)
        for a in alunos:
            obj_aluno = Aluno(**a)
            lista_alunos.append(obj_aluno)
        return lista_alunos
    except Exception as e:
        print(e)
        
        
def salvar_alunos(lista):
    try:
        dados = [aluno.to_dict() for aluno in lista]
        
        f = open(CAMINHO_ARQUIVO, "w")
        json.dump(dados, f, indent=4)
            
        return True
    except Exception as e:
        print(e)
        return False


def adicionar_aluno(aluno):
    try:
        # le arquivo em formato de adicao (append)
        alunos = carregar_alunos()
        
        # gera novo id
        proximo_matricula = ut.calcular_proximo_matricula(alunos)
        
        # atribui novo id a editora que quer inserir
        aluno.matricula = proximo_matricula
            
        # adiciona a nova editora na lista
        alunos.append(aluno)
                
        # salva a nova lista no arquivo
        return salvar_alunos(alunos), aluno
    except Exception as e:
        print(e)
        return None
    
def buscar_aluno_por_matricula(matricula):  
    try:  
        alunos = carregar_alunos()
        for a in alunos:
            if a.matricula == matricula:
                return a
    except Exception as e:
        print(e)
        return None
    
    
def buscar_aluno_por_nome(nome):
    try:
        alunos = carregar_alunos()
        for aluno in alunos:
            if aluno.nome == nome:        
                # se achou um livro com o titulo, retorna o a linha completa do livro
                return aluno
    except:
        # deveria adicionar um arquivo de log para armazenar o erro
        return None


def atualizar_aluno(aluno):
    try:
        alunos = carregar_alunos()
        for idx, a in enumerate(alunos):
            if a.matricula == aluno.matricula:
                alunos[idx] = aluno
                salvar_alunos(alunos)
                return True
    except Exception as e:
        print(e)
        return False
    
    
def remover_aluno(matricula):
    try:
        alunos = carregar_alunos()
        novos_alunos = []
        for a in alunos:
            if a.id != matricula:
                novos_alunos.append(a)
        return salvar_alunos(novos_alunos)
    except Exception as e:
        print(e)
        return False
