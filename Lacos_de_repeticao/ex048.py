''' 48.Faça um programa que calcule a soma entre todos os numero impares que são mutiplos de 3, e que se encontram no intervalo de 1 até 500:'''
soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} valores é de {}'.format(cont,soma))
