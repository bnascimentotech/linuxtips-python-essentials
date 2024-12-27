#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala 
que frequentam  cada uma das atividades.

Usando Dicionários...
"""

from pprint import pprint

__version__ = "0.3.0"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"], 
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

# Busca alunos da sala em cada atividade
def alunos_atividade(sala, atividade):
    
    alunos_atividade = []
    
    for aluno in sala:
        if aluno in atividade:
            alunos_atividade.append(aluno)
    
    return alunos_atividade

    # A mesma operação em apenas uma linha
    # return [aluno for aluno in sala if aluno in atividade]

# Listar alunos em cada atividade por sala
for atividade, lista_alunos in atividades.items():

    print(f"Alunos da atividade: {atividade}")
    print("-" * 40)

    atividade_sala1 = alunos_atividade(sala1, lista_alunos)
    atividade_sala2 = alunos_atividade(sala2, lista_alunos)

    print("Sala 1: ", atividade_sala1)
    print("Sala 2: ", atividade_sala2)

    print()
    print("#" * 40)
