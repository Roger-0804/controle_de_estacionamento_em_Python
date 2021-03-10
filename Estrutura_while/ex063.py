'''.63 Escreva um programa que leia um numero inteiro 'n' qualquer e mostre na tela os 'n' primeiros elementos de uma sequencia FIBONACCI'''
num = int(input('Quantas vezes você quer a sequência?'))
n1 = 0
n2 = 1
print('{} => {} '.format(n1, n2),end='')
cont = 3
while cont <= num:
    n3 = n1 + n2
    print(' => {}'.format(n3),end='')
    n1 = n2
    n2 = n3
    cont += 1
print(' Fim ')
