'''60 Faça um programa que leia um numero qualquer e mostre seu fatorial'''
f = 1
n = int(input('Digite um numero: '))
c = n
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ',end='' )
    f = f * c
    c -= 1
print(f'{f}',end='')
