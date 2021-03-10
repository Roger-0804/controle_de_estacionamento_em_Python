'''.67 Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuário.O programa será interrompido quando o número solicitado for negativo'''
c =1
while True:
    n = int(input((' Digite o  valor que deseja saber a tabuada\n Exceto valores negativos pois interrompe o calculo: ')))
    if n < 0:
        break
    else:
        for c in range(1,11):
            print(f'{n} x {c} = {n*c}')
print('Fim da Tabuada')
