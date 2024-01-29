# SORT SIMPLES

# Entradas
entradas = input()

# Organização
original = entradas.split()
inicio = int(original[0])
meio = int(original[1])
fim = int(original[2])

# Condições
if inicio<meio<fim:
    print(inicio)
    print(meio)
    print(fim)
elif meio<inicio<fim:
    print(meio)
    print(inicio)
    print(fim)
elif inicio<fim<meio:
    print(inicio)
    print(fim)
    print(meio)
elif fim<meio<inicio:
    print(fim)
    print(meio)
    print(inicio)
elif meio<fim<inicio:
    print(meio)
    print(fim)
    print(inicio)
elif fim<inicio<meio:
    print(fim)
    print(inicio)
    print(meio)
print("")

# Impressão Final
for num in original:
    print(num)
