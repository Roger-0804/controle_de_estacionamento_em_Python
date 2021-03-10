'''28.Escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 , e peca ao usuario tentar descobrir qual numero foi escolhido pelo computador .O programa devera escrever na tela se o usuário venceu ou perdeu'''

from random import randint
print('-'*10,'\033[7mAdvinhador de Pensamentos \033[m','-'*10)#utilização de cores em python
usuario = int(input('digite um numero inteiro entre 0 e 5:'))
comput = randint(0,5)
if comput == usuario:
    print('\033[33m O numero escolhido foi {} ,parabéns você acertou\033[m '.format(comput))
else:
    print('\033[31m  O numero escolhido foi {} ,tente outra vez\033[m'.format(comput))










