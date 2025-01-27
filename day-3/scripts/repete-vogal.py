#!/usr/bin/env python3
"""
Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime
cada uma das palabras com suas vogais duplicadas.

Exemplo:
python repete-vogal.py
'Digite uma palavra (ou Enter para sair):' Python
'Digite uma palavra (ou Enter para sair):' Bruno
'Digite uma palavra (ou Enter para sair):' <Enter>
Pythoon
Bruunooo
"""

words = []

while True:
    word = input("Digite uma palavra (ou Enter para sair): ".strip())

    # Condição de parada
    if not word:
        break

    final_word = ""
    
    for letter in word:
        # TODO: Remover acentuação usando função
        # Alternativas ao if abaixo
        # if letter in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        # if letter.lower() in "AEIOUaeiou":

        # Resolvendo com if "comum" 
        if letter.lower() in "aeiouãêóíá":
            final_word += letter * 2
        else:
            final_word += letter
        
        # Resolvendo com if ternário
        # final_word += (
        #     letter * 2 
        #     if letter.lower() in "aeiouãêóíá" 
        #     else letter
        # )
    
    words.append(final_word)

# Imprime com for
# for word in words:
#     print(word)

# Imprime com desempacotamento e separador do print
print(*words, sep="\n")
