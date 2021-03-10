''' Faça um programa que tenha uma função chamada contador( ) que receberá três parãmetros: inicio, fim e passo e realize a contagem.Seu programa tem que realizar três contagens através da função criada:
A) De 1 a 10 , de 1 em 1
B) De 10 até 0 de 2 em 2
C) Uma contagem personalizada'''
from time import sleep
def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('=-' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} '  ,end='',flush=True)#Correção da biblioteca time pra resolver um problema de buffer
            sleep(0.5)
            cont += p
            print( '=> ',end='',flush=True)#Correção da biblioteca time pra resolver um problema de buffer
            sleep(0.3)
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end='', flush=True)#Correção da biblioteca time pra resolver um problema de buffer
            sleep(0.5)
            cont -= p
            print(' => ',end='', flush=True)#Correção da biblioteca time pra resolver um problema de buffer
            sleep(0.3)
        print('FIM')
#Programa principal
contador(1,10,1)
contador(10,1,2)
print('=-'*20)
print('Agora é sua vez de personalizar a contagem...')
ini = int(input('Inicio: '))
fim = int(input('FIm:  '))
pas = int(input('Passo:'))
contador(ini,fim,pas)











