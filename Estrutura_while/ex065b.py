'''65 Crie um programa que leia vários numeros inteiros pelo teclado.No final da execução, mostre a média entre todos valores e qual foi o maior e o menor valores lidos.O programa deve perguntar ao usuario se ele quer continuar ou não a digitar os valores.'''
resp ='S'
media = cont = soma = maior = menor = 0
while resp == 'S':
    numero = float(input('Digite um valor :'))
    soma += numero
    cont += 1
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Deseja digitar mais algum valor? [S/N]')).upper()[0]
media = soma / cont
print('=-'*50)
print(f'Você digitou {cont} numeros e a media de valor entre eles é de {media:.3f}')
print(f'* O maior valor é  {maior}\n* O menor é {menor}')

