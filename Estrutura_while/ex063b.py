'''63 EScreva um programa que leia um numero inteiro ( n ) qualquer e mostre na tela os ( n) primeiros termos de uma sequencia Fibonacci'''
num = int(input('Quantas vezes você quer repetir a sequencia?'))
n1 = 0
n2 = 1
print(f'{n1} => {n2}',end='')
cont = 3
while cont <= num:
    n3 = n1 + n2
    print(f' => {n3}', end='')
    n1 = n2
    n2 = n3
    cont +=1
print('Fim')