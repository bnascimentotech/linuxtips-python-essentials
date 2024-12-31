#!/usr/bin/env python3
"""Calculadora Prefix

Funcionamento:

[operação] [n1] [n2]

Operações:

sum -> +
sub -> -
mul -> *
sdiv -> /

Uso:

$ prefix_calc.py sum 5 2
7

$ prefix_calc.py mul 10 5
50

$ prefix_calc.py
operação: sum
n1: 5
n2: 4
9

Os resultados serão salvos em `prefix_calc.log`
"""

__version__ = "0.1.0" 
__author__ = "Bruno Nascimento"
__license__ = "Unlicense"

import sys
import os

from datetime import datetime

# Valida argumentos
arguments = sys.argv[1:]

# TODO: Utilizar exceptions
if not arguments: # Se o usuário não inputar parâmetros
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3: # Valida a existência de 3 argumentos
    print("Número de argumentos inválidos. Digite 3 argumentos no formato: `operação n1 n2`.")
    print("Exemplo: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

# Valida operações
valid_operations = ("sum", "sub", "mul", "div")

if operation not in valid_operations:
    print("Operação inválida. Selecione uma das seguintes operações:")
    print(valid_operations)
    sys.exit(1)

validated_nums = []

# Valida números
for num in nums:

    # TODO: Utilizar while + tratamento exceptions
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    
    validated_nums.append(num)

n1, n2 = validated_nums

# Executa operação

# TODO: Usar dicionário de funções
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2

# Escreve o arquivo de log
path = os.curdir
filepath = os.path.join(path, "prefix_calc.log")
timestamp = datetime.now().isoformat()
user = os.getenv("USER", "Anonymous")

# Com with
with open(filepath, "a") as logfile:
   logfile.write(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n")

# Com print
# print(f"{timestamp} - {user} - {operation}, {n1}, {n2} = {result}\n", file=open(filepath, "a"))

# Exibe o resultado
print(f"O resultado é {result}")
