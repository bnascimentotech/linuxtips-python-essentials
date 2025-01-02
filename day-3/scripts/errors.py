#!/usr/bin/env python3
"""
"""

__version__ = "0.1.0" 
__author__ = "Bruno Nascimento"
__license__ = "Unlicense"

import os
import sys

# MÉTODO 1 -> LBYL - Look Before You Leap
# if os.path.exists("names.txt"):
#     print("O arquivo existe")
#     input("...") # Race condition
#     names = open("names.txt").readlines()
# else:
#     print("[Error] File `names.txt` not found.")
#     sys.exit(1)

# if len(names) >= 3:
#     print(names[2])
# else:
#     print("[Error] Missing name in the list.")
#     sys.exit(1)


# MÉTODO 2 -> EAFP - Easy to Ask Forgiveness than Permmission

# Bare exception
# try:
#     names = open("names.txt").readlines() # FileNotFoundError
#     1 / 0 # ZeroDivisionError
#     print(names.banana) # AtributeError
# except: # Bare except
#     print("[Error] File `names.txt` not found.")
#     sys.exit(1)

# Tratamento específico para cada caso
# try:
#     names = open("names.txt").readlines() # FileNotFoundError
#     1 / 1 # ZeroDivisionError
#     print(names.append) # AttributeError
# except FileNotFoundError:
#     print("[Error] File `names.txt` not found.")
#     sys.exit(1)
# except ZeroDivisionError:
#     print("[Error] You cannot divide by zero.")
#     sys.exit(1)
# except AttributeError:
#     print("[Error] List doesn't have attribute `banana`.")
#     sys.exit(1)

# Mais próximo a um uso real
try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"[Error] {str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
# OU
# except (FileNotFoundError, AttributeError) as e:
#     print(f"[Error] {str(e)}.")
#     sys.exit(1)
# else: # Executa se não houver erro
#     print("Sucesso!!!")
# finally: # Executa independente de erro
#     print("Execute isso sempre!")

# Erros não definidos. Capturando um erro por "conta própria" (não pré-definido)
# try:
#     raise RuntimeError("Ocorreu um erro")
# except Exception as e:
#     print(str(e))

try:
    print(names[2])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)
