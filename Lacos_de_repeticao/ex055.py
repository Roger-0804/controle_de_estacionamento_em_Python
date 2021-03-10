'''55.Faça um programa que leia o peso de cinco pessoas , no final, mostre qual foi o maior peso e o menor peso lido.'''
peso_menor = 0
peso_maior = 0
for p in range(1,6):
    peso = float(input('Peso da {}° pessoa:'.format(p)))
    if p == 1:
        peso_menor = peso
        peso_maior = peso
    else:
        if peso < peso_menor:
            peso_menor = peso
        if peso > peso_maior:
            peso_maior = peso
print('O menor peso lido foi de {}'.format(peso_menor))
print('O maior peso lido foi de {}'.format(peso_maior))

