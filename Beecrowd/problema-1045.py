# TIPOS DE TRIÂNGULOS
# Entradas
lado1, lado2, lado3 = input().split()

# Conversão
hipotenusa = float(lado1)
lado2 = float(lado2)
lado3 = float(lado3)

# Definição de Hipotenusa
if hipotenusa > lado2 > lado1:
    pass
elif hipotenusa > lado1 >lado2:
    pass
elif lado1 > hipotenusa >lado2:
    troca = lado1
    lado1 = hipotenusa
    hipotenusa = troca
    troca = 0
    pass
elif lado2 > hipotenusa >lado1:
    troca = lado2
    lado2 = hipotenusa
    hipotenusa = troca
    troca = 0
    pass
elif lado2 > lado1 > hipotenusa:
    troca = lado2
    lado2 = hipotenusa
    hipotenusa = troca
    troca = 0
    pass
elif lado1 > lado2 > hipotenusa:
    troca = lado1
    lado1 = hipotenusa
    hipotenusa = troca
    troca = 0
    pass
# Comparações
if hipotenusa >= lado2 + lado3:
    print("NAO FORMA TRIANGULO")
elif (hipotenusa * hipotenusa) == (lado2 * lado2) +(lado3 * lado3):
    print("TRIANGULO RETANGULO")
elif (hipotenusa * hipotenusa) > (lado2 * lado2) +(lado3 * lado3):
    print("TRIANGULO OBTUSANGULO")
elif (hipotenusa * hipotenusa) < (lado2 * lado2) +(lado3 * lado3):
    print("TRIANGULO ACUTANGULO")

# Comparações Extras
if hipotenusa == lado2 == lado3:
    print("TRIANGULO EQUILATERO")

if hipotenusa == lado2 or lado2 == lado3:
    print("TRIANGULO ISOSCELES")