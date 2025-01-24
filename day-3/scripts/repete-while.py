#!/usr/bin/env python3

# While - Enquanto

n = 0
# while True: # loop infinito
#     print(n)
#     n += 1

while n < 101: # condicao de parada
    # if n >= 40 and n <= 60:
    #     # break
    #     n += 1
    #     continue    
    if n % 2 != 0: # somente numeros pares
        n += 1
        continue
    print(n)
    n += 1
