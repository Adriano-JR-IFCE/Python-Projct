# NÚMEROS ÍMPARES

# Entrada
parametro  = int(input())

# Encontra ímpares
for numero in range(parametro+1):
    if numero % 2 != 0:
        print(numero)

# A função range(5) cria uma sequência de números de 0 a 4.
# O loop for itera sobre esses números e os imprime.