# MÚLTIPLOS
# variáveis
num1, num2 = input().split()

# verificação 
multi = int(num2)/int(num1)

# condições
if int(multi)*int(num1) == int(num2):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")