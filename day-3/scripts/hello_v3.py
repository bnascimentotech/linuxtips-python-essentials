#!/usr/bin/env python3
"""Hello World Multi Línguas

Dependendo da lingua configurada no ambiente o programa exibe 
a mensagem correspondente

Como usar:

Tenha a variável LANG devidamente configurada. Exemplo:

    export LANG=pt_BR

Ou informe através do CLI argument `--lang`

Ou usuário terá que digitar.

Execução:

    python3 hello_v3.py
    ou
    ./hello.py    
"""
__version__ = "0.1.3" 
__author__ = "Bruno Nascimento"
__license__ = "Unlicense"

import os
import sys

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
    
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip() # Remove hifens hifens à esquerda e espaços antes/depois da chave

    value = value.strip() # Remove espaços antes/depois do valor

    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    
    arguments[key] = value # Se validações acima estiverem Ok atribui valores às chaves

current_language = arguments["lang"]

if current_language is None:
    
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    # "en_US": "Hello World!",
    "C.UTF": "Hello World!", # Inglês no WSL2
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!"
}

print(
    msg[current_language] * int(arguments["count"])
)
