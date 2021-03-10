'''54.Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''
from datetime import date
contM = 0
contm = 0
for c in range(1,8):
    nasc = int(input('Digite seu ano de nascimento:'))

    ano = date.today().year
    idade = ano - nasc

    if idade < 18:
        contm +=1
    else:
        contM +=1

print('\033[1mExistem \033[1;34m{}\033[m pessoas menores de idade e \033[1;31m{}\033[m pessoas maiores de idade\033[m'.format(contm,contM))


