# RESTO DA DIVISÃO

# Entradas
inicio = int(input())
fim = int(input())

contador = inicio

# Calculo
while contador < fim:
    if contador % 5 == 2 or contador % 5 == 3:
        print(contador)
    contador +=1
