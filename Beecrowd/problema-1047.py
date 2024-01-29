from datetime import datetime, timedelta

# Entradas
entradas = input()

# Organização
vetor = entradas.split()
hora_inicio = int(vetor[0])
minuto_inicial = int(vetor[1])
hora_final = int(vetor[2])
minuto_final = int(vetor[3])

# Formatação
horaI = "{}:{}".format(hora_inicio, minuto_inicial)
horaF = "{}:{}".format(hora_final, minuto_final)

# Define os tempos
tempo_inicial = datetime.strptime(horaI, "%H:%M")
tempo_final = datetime.strptime(horaF, "%H:%M")

# Calcula a diferença
diferenca = tempo_final - tempo_inicial

# Extrai a diferença em horas e minutos
horas = diferenca.seconds // 3600
minutos = (diferenca.seconds % 3600) // 60

# Exibe a diferença
if hora_inicio == hora_final and minuto_inicial == minuto_final:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
