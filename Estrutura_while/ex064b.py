'''64 Crie um programa que leia vários numeros inteiros  pelo teclado.O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.No final mostre quantos números foram digitados e qual foi a soma entre eles. '''
s = c = 0
n = int(input('Digite um numero: '))
while n != 999:
    s += n
    c += 1
    n = int(input('Digite um numero: '))
print(f'Foram digitados um total de {c} numeros e a soma entre eles é igual a {s}')