'''38.Escreva um programa que leia dois numeros e compare-os, mostrando na tela uma mensagem:
-O primeiro valor é maior:
-O segundo valor é maior:
-Não existe valor maior, os dois são iguais:
'''

print('\033[0;33m=-\033[m'*20,'\033[1;35mComparando dois numeros\033[m','\033[0;33m=-\033[m'*20)

num1 = float(input('Digite o primeiro valor:'))
num2 = float(input('Digite o segundo valor:'))

if num1 > num2:
    print('\033[1;31;40mO primeiro valor é o maior\033[m')
elif num2 >num1:
    print('\033[1;33;44mO segundo valor é o maior\033[m')
else:
    print('\033[1;35;40mAmbos são iguais\033[m')
