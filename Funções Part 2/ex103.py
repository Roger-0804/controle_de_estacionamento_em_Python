'''Faça um programa que tenha uma funçãp chamada ficha(), que receba dois parâmetros opcionais: O nome de jogador e quantos gols ele marcou.O programa deverá ser capaz de mostrar a ficha do jogador mesmo que algum dado não tenha sido informado corretamente.'''

def ficha (jog ='<desconhecido>',gol = 0):
    print(f'{jog} marcou {gol} gol(s) no campeonato.')


# Programa Principal
n = str(input('Qual o nome do Jogador? '))
g = str(input(f'Quantos gols {n} marcou?'))
if g.isnumeric():
     g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol =g)
else:
    ficha(n,g)
