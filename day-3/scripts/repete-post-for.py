#!/usr/bin/env python3

dados = {}

for line in open("post.txt"):
    if line == "---\n":
        break
    
    key, valor = line.split(":")
    dados[key] = valor

print(dados["title"])
print(dados)
