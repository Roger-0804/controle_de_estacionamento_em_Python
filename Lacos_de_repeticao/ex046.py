'''46.Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 atá 0, com uma pausa de 1 segundo entre eles:'''

print('{:*^50}' .format(' Reveillon em Copacabana '))
from time import sleep

print('O ano ta acabando contagem regressiva:')
for c in range(10,0,-1):
    sleep(0.5)
    print(c,end='')
    print('.',end='')
    sleep(0.2)
    print('.', end='')
    sleep(0.2)
    print('.', end='')
    sleep(0.2)
    if c == 0:
        sleep(1)
    import emoji
print(emoji.emojize("\033[1;30mFeliz ano Novo\033[m \033[1;31m:fireworks:\033[m",use_aliases=True))


