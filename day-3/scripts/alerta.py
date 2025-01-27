#!/usr/bin/env python3
"""
Faça um script que pergunta ao usuário qual a temperatura atual e o índice 
de umidade do ar sendo que caso será exibida uma mensagem de aerta dependendo 
das condições:

Se temp maior 45: ALERTA!!! Perigo de calor extremo
Senão, temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido

.. temp entre 10 e 30: Normal
.. temp entre 0 e 10: Frio
.. temp <0: ALERTA: Frio extremo
"""

import sys
import logging

log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}
keys = info.keys()

# Valida parâmetros de entrada
for key in keys:
    try:
        info[key] = float(input(f"Qual a {key}? ").strip())
    except ValueError:
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)

temp = info["temperatura"]
umidade = info["umidade"]

if temp > 45:
    print("ALERTA!!! 🥵 Perigo de calor extremo!")
elif temp * 3 >= umidade:
    print("ALERTA!!! 🥵 Perigo de calor úmido!")
elif temp >= 3 and temp <= 30:
    print("😊 Normal.")
elif temp >= 0 and temp <= 10:
    print("🥶 Frio.")
elif temp <= 0:
    print("ALERTA!!! ☃️ Frio extremo!")
