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

import logging

log = logging.Logger("alerta")

# TODO: Usar funções para ler input

info = {
    "temperatura": None,
    "umidade": None
}

while True:
    # Condição de parada
    # O dicionário está completamente preenchido
    info_size = len(info.values())
    filled_size = len([value for value in info.values() if value is not None])

    if info_size == filled_size:
        break # Para o while

    # Valida parâmetros de entrada
    for key in info.keys(): # ["temperatura", "umidade"]
        if info[key] is not None:
            continue
        try:
            info[key] = int(input(f"{key}: ").strip())
        except ValueError:
            log.error("%s inválida, digite números", key)
            break

temp, umidade = info.values() # unpacking [30, 90]

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
