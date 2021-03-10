'''96. Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular (Largura e comprimento) e mostre a área do terreno.'''
def area( l , c):
    a = l * c
    print(f'A area do terreno de {l:.2f}  x {c:.2f}. é de {a:.3f}mts²')

#programa principal
print('=-'*20)
print('<<<<Calculando a area do terreno>>>>')
l = float(input('Qaul  a largura em (mts) ?'))
c = float(input('Qual o  comprimento em (mts) ?'))
area( l, c )

