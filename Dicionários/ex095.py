'''95. Aprimore o desafio 93,para que o programa funcionw com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador'''
lista = list()
jogador = dict()
partidas=list()
while True:
    jogador.clear()
    jogador['nome']= str(input('Nome do jogador:'))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou ?'))
    partidas.clear()
    for c in range(0,tot):
        partidas.append(int(input(f'Quantos gols {jogador["nome"]} fez na {c+1}° partida?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    lista.append(jogador.copy())
    while True:
        resp =str(input('Quer continua [S/N] ?')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda somente S ou N')
    if resp == 'N':
        break
print('=-'*40)
print('cod',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('=-'*40)
for k,v in enumerate(lista):
    print(f' {k:>3}',end='')
    for d in v.values():
        print(f' {str(d):<15}',end='')
    print()
print('=-'*40)
while True:
    busca = int(input('Mostar os dados de qual jogador? (999) p/ parar'))
    if busca == 999:
        break
    if busca >= len(lista):
        print(f'ERRO! não existe jogador com o codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {lista[busca]["nome"]}:')
        for i,g in enumerate(lista[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols')
    print('=-'*40)
print('<< VOLTE SEMPRE >>')
