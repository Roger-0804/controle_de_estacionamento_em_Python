'''100. Faça um programa que tenha uma lista chamada numeros e duas funções  chamada sorteia() e somapar() .A primeira função vai sortear 5 numeros e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep
def sorteia(lista):
    for cont in range(1,6):
        n = randint(1,10)
        lista.append(n)
        print(f' {n} ',end='')
        sleep(0.3)
        print(f' => ',end='')
        sleep(0.3)
    print('FIM')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da  {lista} ,temos : {soma}')

# Programa Principal
numeros = list()
sorteia(numeros)
somapar(numeros)
