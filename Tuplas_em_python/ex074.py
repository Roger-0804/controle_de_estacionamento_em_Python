'''74. Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.Depois disso mostre a listagem de numeros gerados   e também indique o menor e o maior  que estão na tupla:'''

from random import randint
numeros = (randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20))
print(f'Os numeros sorteados foram: ',end='')
for n in numeros:
    print(f'{n}',end=' ')
print(f'\nO maior valor sorteado foi: {max(numeros)}')
print(f'O menor valor sorteado foi: {min(numeros)}')

