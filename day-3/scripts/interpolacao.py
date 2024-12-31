#!/usr/bin/env python3
"""Imprime a mensage de um e-mail

NÃO ENVIE SPAM!!!
"""

__version__ = "0.1.0" 
__author__ = "Bruno Nascimento"
__license__ = "Unlicense"

email_tmpl = """
Olá, %(nome)s

Tem interesse em comprar %(produto)s?

Este produto é ótimo para resolver %(texto)s.

Clique agora em %(link)s.

Últimas unidades! Apenas %(quantidade)d disponíveis!

Preço promocional %(preco).2f
"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(
        email_tmpl
        % {
            "nome": cliente,
            "produto": "caneta",
            "texto": "escrever muito bem...",
            "link": "https://canetaslegais.com/",
            "quantidade": 2,
            "preco": 50.5
        }        
    )