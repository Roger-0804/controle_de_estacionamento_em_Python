'''58 Melhore o joog do desafio 28, onde o cumputador vai pensar em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar. Mostrando no final quantos palpites foram necessários para vencer.'''

from random import randint
computador = randint(0,11)
acetou = False
palpite = 0
while not acetou:
    jogador = int(input('Tentando a sorte, tente adivinhar qual o numero que o computador vai pensar?'))
    palpite +=1
    if jogador == computador:
        acetou = True
    else:
        if jogador > computador:
            print('Menos...')
        elif jogador < computador:
            print('Mais...')
print(f'Parabens você acertou,voce apostou {jogador} e o computador apostou: {computador}')
print('Voce precisou de {} tentativas'.format(palpite))









