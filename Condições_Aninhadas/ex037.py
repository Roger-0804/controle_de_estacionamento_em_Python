'''37.Escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1-para binário
2-para octal
3-para hexagonal:'''

numero= int(input('Digite um numero inteiro:'))
print('''Digite qual será a base de conversão:
[ 1 ] Binário:
[ 2 ] Octal:
[ 3 ] Hexadecimal:''')

escolha = int(input('Sua opção:'))

if escolha == 1:
    print('o numero {}, na base binária é igual a {}'.format(numero,bin(numero)[2:]))
elif escolha == 2:
    print('O numero {} na base Octal , é igual a {}'.format(numero,oct(numero)[2:]))
elif escolha == 3:
    print('O numero {} na base Hexadecimal é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('Opção inválida escolha entre as três opções.')