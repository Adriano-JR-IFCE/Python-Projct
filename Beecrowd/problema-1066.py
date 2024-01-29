# PARES, ÍMPARES, POSITIVOS E NEGATIVOS

# entradas
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

# Lista de entradas
lista = [num1, num2,num3, num4, num5]

# Saber Par ou Impar
par = 0
impar = 0
for elemento in lista:
    if elemento % 2 == 0:
        par += 1  # Incrementando o valor de 'par' em 1
    else:
        impar += 1  # Incrementando o valor de 'impar' em 1

# Saber Positivo ou Negativo
positivo = 0
negativo = 0
for elemento in lista:
    if elemento > 0:
        positivo += 1  # Incrementando o valor de 'positivo' em 1
    elif elemento == 0:
        pass
    else:
        negativo += 1  # Incrementando o valor de 'negativo' em 1



# Impressões de resultados
print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(positivo))
print("{} valor(es) negativo(s)".format(negativo))