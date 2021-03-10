'''Faça um programa que tenha uma função chamada maior( ) que receba  varios parâmetros com valores inteiros.Seu programa tem que analisar todos os valores e dizer qual é o maior deles'''
from time import sleep
def maior(*num):
    cont = mai = 0
    print('=-' * 20)
    print(f'Analisando os dados....')
    for n in num:
        print(f' {n}',end='')
        sleep(0.5)
        if cont == 0:
            mai = n
        else:
            if n > mai:
                mai = n
        cont += 1

    print(f'\n Ao todo foram analisados {cont} valores')
    print(f' Dentre os valores... {mai} é o maior deles')







#Programa Principal
maior(1,2,3)
maior(3,5,1)