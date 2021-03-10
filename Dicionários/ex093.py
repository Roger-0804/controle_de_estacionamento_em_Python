'''93.Crie um programa que gerencie o aproveitamento de um jogador de futebol.O programa vai ler o nome do jogador e quantas partidas ele jogou.Depois  vai ler a quantidade de  gols feitos em cada partida.No final,tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

jogador =dict()
partidas =[]
jogador['nome'] =str(input('Nome:'))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0,tot):
    partidas.append(int(input(f'    Quantos gols na partida  {c+1}? ')))
jogador['gols'] =partidas[:]
jogador['Total'] = sum(partidas)
print('=-'*30)
print(jogador)
print('=-'*30)
print(f'O jogador {jogador["nome"]} fez um total de {jogador["Total"]} gols')
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas')
for i,v in enumerate(jogador['gols']):
    print(f'    => Na  {i+1}° partida ,fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols.')


