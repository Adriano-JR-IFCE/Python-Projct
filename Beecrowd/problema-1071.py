# SOMA DE IMPARES CONSECUTIVOS I

# Entradas
valor1 = int(input())
valor2 = int(input())

# Ordenação
inicio = 0
fim = 0
if valor1 < valor2:
    inicio = valor1
    fim = valor2
else: 
    inicio = valor2
    fim = valor1

# Cálculo
somador = 0
while inicio <= fim:
    if inicio % 2 != 0:
        somador += inicio
    inicio+=1

print(somador)