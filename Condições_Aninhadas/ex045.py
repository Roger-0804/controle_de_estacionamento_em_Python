'''45. Crie um programa que faça o computador jogar JOKENPÔ:'''''

from random import randint
from time import sleep
print('\033[1;30m$'*20,'\033[1;33mJOKENPÔ\033[m','\033[1;30m$\033[m'*20)

itens= ('Pedra','Papel','Tesoura')
computador = randint(0,2)

print('''\033[1;30mEscolha uma jogada
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura\033[m''')
jogador = int(input('\033[1mDigite sua opção:\033[m'))

print('\033[1;31mJO\033[m')
sleep(.5)
print('\033[1;30mKEN\033[m')
sleep(.5)
print('\033[1;32mPÔ\033[m')

if computador == 0:# Pedra
    if jogador == 0:
        print('Deu Empate')
    elif jogador == 1:
        print('O Jogador Vence!! , jogador escolheu :{}\n e o computador escolheu: {}'.format(itens[jogador],itens[computador]))
    elif jogador == 2:
        print('O computador Vence!!, jogador escolheu: {}\n e o computador escolheu: {}'.format(itens[jogador],itens[computador]))

if computador == 1: #Papel
    if jogador == 0:
        print('O computador Vence!!, jogador escolheu: {}\n e o computador escolheu: {}'.format(itens[jogador],itens[computador]))
    elif jogador == 1:
        print('Deu Empate')
    elif jogador == 2:
        print('O jogador Vence!!, jogador escolheu: {}\n e o computador escolheu: {}'.format(itens[jogador],itens[computador]))

if computador == 2: # Tesoura
    if jogador == 0:
        print('O jogador Vence!!, jogador escolheu: {}\n e o computador escolheu: {}'.format(itens[jogador],itens[computador]))
    elif jogador == 1:
        print('O computador Vence!! , jogador escolheu: {}\n e o computador escolheu: {}'.format(itens[jogador],itens[computador]))
    elif jogador ==2:
        print('Deu empate')

    else:
        print(' Opção Inválida')










