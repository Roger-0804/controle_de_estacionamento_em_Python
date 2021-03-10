'''91.Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.Guarde esses resultados em um dicionário.No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior numero no dado.'''
from random import randint
from time import  sleep
from operator import itemgetter
jogo = { 'Jogador 1':randint(1,6),
         'Jogador 2':randint(1,6),
         'Jogador 3':randint(1,6),
         'Jogador 4':randint(1,6)}
ranking = list()
print('Valores Sorteados:')
for k ,v in jogo.items():
    print(f'{k} tirou :{v} no dado')
    sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('=-'*15,'RANKING','=-'*15)
print(ranking)
print('-'*60)
print('==    Clasificação   ==')
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar:{v[0]} com {v[1]} pontos !!')
    sleep(0.9)



