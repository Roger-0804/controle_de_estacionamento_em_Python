'''33.Faça um programa que leia 3 numeros e mostre qual é o valor maior e qual é o valor menor:'''

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero :'))
num3 = int(input('Digite um numero :'))
#comparando qual é o maior valor:
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
#comparando qual é o menor valor:
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print('O numero {} é o menor'.format(menor))
print('o numero {} é o maior'.format(maior))
