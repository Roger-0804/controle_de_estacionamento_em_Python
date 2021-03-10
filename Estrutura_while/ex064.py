'''.64 Crie um programa que leia vários numeros inteiros pelo teclado.O programa só vai parar quando o usuário digitar o valor : 999 ,  que é a condição de parada.No final mostre quantos numeros foram digitados e qual foi a soma entre eles, desconsiderando o flag.'''
soma = numero = cont = 0
numero = int(input('Digite um valor:'))
while numero != 999:
    soma = soma + numero
    cont = cont + 1
    numero = int(input('Digite um valor:'))
print('O valor total da soma é de {}'.format(soma ))
