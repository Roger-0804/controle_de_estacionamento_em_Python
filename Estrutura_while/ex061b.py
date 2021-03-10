'''61 Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, msotrando os 10 primeiros termos da progressão usando uma estrutura WHILE.
'''
from time import sleep
primeiro = int(input('Digite o primeiro termo dessa progressão:'))
razao = int(input('Qual será a razao da PA? '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f' {termo} =>', end='')
    termo += razao
    cont += 1
    sleep(0.5)
print('Fim')
