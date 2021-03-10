'''Crie um programa que simule o funcinamento de um caixa eletrônico. No início pergunte ao usuário qual será o valor sacado, e o programa vai informar quantas cédulas de cada valor serão entregues,  considerando que o caixa possui cédulas de R$ (50, 20, 10, 1).'''
print('$'*10,'Banco Santander','$'*10)
saque = int(input('\033[1;35mQual o valor que você quer sacar?\n R$ \033[m'))
total = saque
contCedula =0
nota =50
while True:
    if total >= nota:
        total -= nota
        contCedula += 1
    else:
        if contCedula > 0:
            print(f'\033[1;32mRetire do caixa: \033[30m{contCedula}\033[m notas de \033[1;34m{nota}\033[m reais\033[m')
        if nota == 50:
            nota =20
        elif nota ==20:
            nota =10
        elif nota == 10:
            nota =1
        contCedula =0
        if total ==0:
            break

