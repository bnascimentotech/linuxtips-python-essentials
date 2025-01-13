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
__version__ = "0.1.4" 
__author__ = "Bruno Nascimento"
__license__ = "Unlicense"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

# Nossa instância
log = logging.Logger("logs.py", log_level)

# Level
ch = logging.StreamHandler()
ch.setLevel(log_level)

# Formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)

# Destino
log.addHandler(ch)

arguments = {"lang": None,"count": 1}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use `=`, you used %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    
    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    
    # TODO: Usar repetição
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = current_language = input("Choose a language: ")

current_language = current_language[:5]

msg = {
    "C.UTF": "Hello World!", # Inglês no WSL2
    "en_US": "Hello World!",    
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!"
}

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from {list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
)
