# Rafael Sartori M. Santos, 186154 - Simulação 2 de ME323

from random import random

# Como utilizarei a biblioteca random, a amostra representará uma amostra COM reposição

# Configurações da população eleitora
POPULACAO = 10**4
PROPORCAO_A = 0.30

# Configuração dos testes
NUMERO_TESTES = 2000
PARTICIPANTES_AMOSTRA_1 = 26    # representa uma turma na Unicamp
PARTICIPANTES_AMOSTRA_2 = 360   # representa um curso na Unicamp


###
### Funções dos testes
###

def amostrar(participantes):
    numero_eleitores_A = 0

    for eleitor in range(0, participantes):
        # Verificamos se sorteamos um eleitor que é eleitor de A
        if random() <= PROPORCAO_A:
            numero_eleitores_A += 1
    
    return (numero_eleitores_A / participantes)


###
### Execução dos testes
###

# listas de proporções das amostras 1 e 2 respectivamente
amostras_1 = []
amostras_2 = []

# executamos os testes
for teste in range(0, NUMERO_TESTES):
    amostras_1.append(amostrar(PARTICIPANTES_AMOSTRA_1))
    amostras_2.append(amostrar(PARTICIPANTES_AMOSTRA_2))
    
# calculamos a média de cada um
media_amostras_1 = sum(amostras_1) / len(amostras_1)
media_amostras_2 = sum(amostras_2) / len(amostras_2)

# calculamos o desvio padrão de cada um
avg_dev_amost_1 = sum( (x - media_amostras_1)**2 for x in amostras_1) / len(amostras_1)
avg_dev_amost_2 = sum( (x - media_amostras_2)**2 for x in amostras_2) / len(amostras_2)

print('p^_1 = ', media_amostras_1 * 100, ' dp_p^_1 = ', avg_dev_amost_1 * 100)
print('p^_2 = ', media_amostras_2 * 100, ' dp_p^_2 = ', avg_dev_amost_2 * 100)

# mostramos em gráficos