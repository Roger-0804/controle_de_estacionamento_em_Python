'''.66 Crie um programa que leia vários numeros inteiros pelo teclado.O programa só vai parar quando o usuário digitar 999, que é a condição de parada.No final, mostre quantos números foram digitados e qual foi a soma entre eles.(Desconsiderando O FLAG).'''
soma = 0
c = 0
while True:
    n = int(input('Digite um  numero:'))
    if n == 999:
        break
    c += 1
    soma +=n
print(f'O total de números digitados é igual a {c} e a soma  entre eles é de {soma}')
