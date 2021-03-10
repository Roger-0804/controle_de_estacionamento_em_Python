'''Faça um programa que jogue par ou ímpar com o computador. O jogo será interrompido quando o jogador PERDER mostrando na tela o total de vitórias cosecutivas que ele conquistou no final do jogo.'''

from random import randint
v = 0
print('-='*10,'Par ou Ímpar vamos jogar?','-='*10)
while True:
    jogador = int(input('Digite um numero: '))
    computador = randint(0, 10)
    soma = jogador + computador
    aposta = ' '
    while aposta  not in 'PI':
        aposta = str(input('ESCOLHA ENTRE PAR OU ÍMPAR [P/I]: ')).upper().strip()[0]
    print(f' você digitou  o numero {jogador} e sua escolha foi:  {aposta}\n Logo o  computador jogou {computador}, resultado foi {soma}')
    print('Deu PAR 'if soma % 2 == 0 else 'Deu ÍMPAR')
    if aposta == 'P':
        if soma % 2 == 0:
            print('Parabéns vitoria !!')
            v +=1
        else:
            print('Infelizmente você perdeu, mais sorte na próxima!')
            break
    elif aposta == 'I':
        if soma % 2 == 1:
           print('Parabéns vitória!!')
           v += 1
        else:
            print('Infelizmente você perdeu, mais sorte na próxima!!')
            break
print(f'Você obteve {v} vitórias')








