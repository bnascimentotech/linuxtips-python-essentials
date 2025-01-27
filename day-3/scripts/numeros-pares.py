#!/usr/bin/env python3
"""
Faça um programa que imprime os números pares de 1 a 200.

Ex:
`python3 numeros_pares.py`
2
4
6
8
...
"""

# Minha resolução
# for num in range(1, 201):
#     if num % 2 == 0:
#         print(num)

# Resolução Bruno
for num in range(1, 201):
    if num % 2 != 0:
        continue
    print(num)
