'''47.Crie um programa que mostre na tela todos os numero pares que estão no intervalo entre 1 e 50:'''
from time import sleep
for c in range(1,50,2):
    print(c+1,end=' ')
    sleep(0.3)
    print(','if c < 50 else ' ',end='')
    sleep(0.3)

