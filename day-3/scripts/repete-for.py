#!/usr/bin/env python3

# numbers = [1, 2, 3, 4, 5, 6]
# numbers = range(1, 7) # Full range
# numbers = range(1, 11, 2) # Com steps
# numbers = range(1, 11) # Somente pares

# Iterable
# for number in numbers:
#     par = number % 2 == 0
#     if par:
#         print(number)
#     else:
#         # continue 
#         break
#     print(f"Mais código com {number}...")

# Programação Estruturada / Imperativa
original = [1, 2, 3]

# For loop / Laço for
dobrada = []

for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Programação Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict Comprehension
dados = {
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt")
    if ":" in line
}
# Mesma operação em Programação Estruturada
# dados = {}
# for line in open("post.txt"):
#     if ":" in line:
#         key, valor = line.split(":")
#         dados[key] = valor.strip()

print(dados)
