'''59 Crie um programa que leia dois valores e mostre  um menu na tela :
 [1] Somar [2] Multiplicar [3] Maior [4] Novos numeros [5] Sair. Seu programa deverá realizar a operação solicitada em cada caso.'''
n1 = int(input('Digite o primeiro valor  :'))
n2 =int(input('Digite o segundo valor: '))
print('-='*20,'Menu de Opcões','=-'*20)
s = m = maior = escolha = 0
while escolha != 5:
    escolha = int(input('Escolha o que deseja fazer:\n[1] Somar[2] Multiplicar[3] Maior[4] Novos Numeros [5] Sair\n'))
    if escolha == 1:
        s = n1 + n2
        print(f'O resultado da soma entre {n1} + {n2} é igual a  {s}')
    elif escolha == 2:
        m = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é igual a {m}')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        elif n1 == n2:
            print('Não existe maior ambos os valores são iguais.')
        else:
            maior = n2
            print(f'O maior valor entre {n1} e {n2} é :{maior}')
    elif escolha == 4:
        n1 = int(input('Digite um novo valor para o 1° numero:'))
        n2 =int(input('Digite um novo valor para o 2° numero: '))
    elif escolha == 5:
        print('Encerrando o programa...')
    else:
        print('Opção Inválida!!')
print('Sair')

