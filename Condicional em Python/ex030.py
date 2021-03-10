'''30.Crie um programa que leia um numero inteiro e mostre se ele é par ou ímpar:'''

print('-'*10,'Par ou Ímpar','-'*10)
num=float(input('Digite um numero:'))
res=num%2
if res==0:
    print('Par')
else:
    print('Ímpar')