'''.70 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá  perguntar se o usuário vai continuar.No final mostre:
a, Qual o total gasto na compra
b, Quantos produtos custam mais de R$ 1.0000,00
c, Qual o nome do produto mais barato.'''
soma = cont = menorPreco = 0
maisbarato= ''
while True:
    print('-'*10,'Lojas Tabajara','-'*10)
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o preço do produto acima:R$ '))
    continua =' '
    while continua not in 'SN':
        continua = str(input('deseja continuar?[S/N] ')).upper().strip()[0]
        soma += valor
        if valor >= 1000:
            cont +=1
        if cont == 1 or valor < menorPreco:
            menorPreco = valor
            maisbarato = produto
    if continua == 'N':
        break
print(f'O valor total da compra foi de {soma:.2f}')
print(f'Tivemos {cont} produtos com valor acima de R$ 1.000,00')
print(f'O produto mais barato da lista foi: {maisbarato}')
print('Fim do cadastro!!!')


