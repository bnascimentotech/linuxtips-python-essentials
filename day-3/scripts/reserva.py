#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma lista dos quaertos
disponíveis para alugar e o preço de cada quarto. Esta informação está 
disponível em um arquivo de texto separado por vírgulas.

`quartos.txt`
# codigo, nome, preço
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser
reservado e a quantidade de dias. No final ele exibe o valor estimado
a ser pago.

O programa deve salvar esta escolha em outro arquivo contento as reservas.

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto, o programa deve exibir uma
mensagem informando que já está reservado.
"""

import sys
import logging

RESERVAS_FILE = "reservas.txt"
QUARTOS_FILE = "quartos.txt"

# Acesso ao banco de dados

# TODO: Usar pacote csv

ocupados = {} # acumulador

try:
    for line in open(RESERVAS_FILE):
        nome_cliente, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome_cliente": nome_cliente,
            "dias": dias
        }
except FileNotFoundError:
    logging.error("Arquivo %s não existe!", RESERVAS_FILE)
    sys.exit(1)

# TODO: Usar funções para ler arquivos

quartos = {} # acumulador

try:
    for line in open(QUARTOS_FILE):
        num_quarto, nome_quarto, preco = line.strip().split(",")
        quartos[int(num_quarto)] = {
            "nome_quarto": nome_quarto,
            "preco": float(preco), # TODO: Decimal
            "disponivel": False if int(num_quarto) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo %s não existe!", QUARTOS_FILE)
    sys.exit(1)

# Programa principal
print("Reservas no Hotel Pythonico da Linux Tips")
print("-" * 52)
if len(ocupados) == len(quartos):
    print("Hotel está lotado. Tente novamente mais tarde.")
    sys.exit(0)

nome_cliente = input("Nome do cliente: ").strip()

# TODO: Usar rich.Table
print("\n***************** Lista de quartos *****************\n")
head = ["Número", "Nome Quarto", "Preço", "Disponível"]
print(f"{head[0]:<6} - {head[1]:<14} - R$ {head[2]:<9} - {head[3]:<10}")

for num_quarto, dados_quarto in quartos.items():
    nome_quarto = dados_quarto["nome_quarto"]
    preco = dados_quarto["preco"]
    disponivel = "⛔" if not dados_quarto["disponivel"] else "👍"
    
    print(
        f"{num_quarto:<6} - {nome_quarto:<14} - "
        f"R$ {preco:9.2f} - {disponivel:<10}"
    )

print("-" * 52)

# Reserva
try:
    num_quarto = int(input("Escolha um quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido. Insira apenas dígitos.")
    sys.exit(0)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")
    sys.exit(0)

try:
    dias = int(input("Quantos dias? ").strip())
except ValueError:
    logging.error("Número inválido, insira apenas dígitos.")
    sys.exit(0)

nome_quarto = quartos[num_quarto]["nome_quarto"]
preco_diaria = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_diaria * dias

# Confirmação
print(
    f"Olá {nome_cliente}, você escolheu o quarto {nome_quarto} "
    f"o valor total estimado será R$ {total:.2f}"
)

# Escreve arquivo de reservas
if input("Confirma? (digite y): ").strip().lower() in ("y", "yes", "s", "sim"):
    with open(RESERVAS_FILE, "a") as reserva_file:
        reserva_file.write(f"{nome_cliente},{num_quarto},{dias}\n")
