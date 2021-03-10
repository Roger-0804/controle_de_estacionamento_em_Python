'''.58 Melhore o jogo do desafio 028 onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,mostrando no final quantos palpites foram gastos para vencer.'''
from random import randint

print('-='*20,'Em que numero estou pensando...?','-='*20)
acertou = False
palpite = 0
comput = randint(0,10)
while not acertou:

    jogador = int(input('Qual é o seu palpite?'))
    palpite += 1
    if jogador ==  comput:
        acertou = True
    else:
        if jogador > comput:

            print('Menos...tente de novo!!')
        elif jogador < comput:
            print('Mais tente de novo!!')
print('Parabéns você acertou com {} palpites!!!'.format(palpite))









