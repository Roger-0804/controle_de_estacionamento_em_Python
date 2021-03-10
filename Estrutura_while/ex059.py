'''.59 Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2] multiplicar
[3] Maior
[4] Novos numeros
[5 Sair'''
from time import sleep
n1 = float(input('Digite o primeiro valor:'))
n2 = float(input('Digite o segundo valor:'))
escolha = 0
while escolha != 5:
    print('=-' * 30)
    escolha = int(input('''Escolha no menu qual a sua opção:
 [ 1 ] Somar \n [ 2 ] multiplicar \n [ 3 ] Maior \n [ 4 ] novos numeros \n [ 5 ] Sair do programa '''))
    if escolha == 1:
        soma = n1 + n2
        print('O resultado da opção [ 1 ] é igual a {:.0f} + {:.0f} = {:.0f}'.format(n1,n2,soma))
        print('Fim')
    elif escolha == 2:
        multip = n1 * n2
        print('O resultado da opção [ 2 ] é igual a {:.0f} x {:.0f} = {:.0f}'.format(n1,n2,multip))
    elif escolha == 3:
        if n1 > n2:
            print('{:.0f} é maior que {:.0f}'.format(n1,n2))
        else:
            print('{:.0f} é maior que {:.0f}'.format(n2,n1))
    elif escolha == 4 :
        print('Digite novos valores:')
        n1 = float(input('Digite o primeiro valor:'))
        n2 = float(input('Digite  o segundo valor:'))
    elif escolha == 5:
        print('\033[1;30mEncerrando o programa...\033[m')
        sleep(1)
    else:
        print('Opção inválida!!')
print('\033[1mFim do programa\033[m')

