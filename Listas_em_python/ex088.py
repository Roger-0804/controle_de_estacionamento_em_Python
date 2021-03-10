'''88. Faça um programa que ajude um jogador da mega-sena a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
lista=[]
geral =[]
print('*'*10,'Mega Sena','*'*10)
quant =int(input('Quantos palpites deseja fazer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    geral.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 10, 'preparando os palpites', '-' * 10)
print()
sleep(0.8)
for i,l in enumerate(geral):
    print(f'Jogo{i+1}:{l}')
    sleep(0.5)
print()
print('$'*10,'Boa sorte','$'*10)




