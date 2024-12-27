#!/usr/bin/env python3
"""Hello World Multi Línguas

Dependendo da língua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variável de ambiente LANG devidamenete configurada. Exemplo:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.2" 
__author__ = "Bruno Nascimento"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

# Ordem de Complexidade O(1) - Sets (Hash Table)
msg = {
    # "en_US": "Hello World!",
    "C.UTF": "Hello World!", # Inglês no WSL2
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!"
}

# Ordem de Complexidade O(n) - Condicionais
# if current_language == "pt_BR":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjour Monde!"

print(msg[current_language])
