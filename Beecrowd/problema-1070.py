# SEIS NÚMEROS ÍMPARES

# Entrada
entrada = int(input())

# Controle
controle = 0

# Calculo
while controle < 6:
    if entrada % 2 != 0:
        print(entrada)
        controle += 1
    entrada += 1
    