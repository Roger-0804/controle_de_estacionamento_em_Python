'''79.Crie um programa onde o usuário possa digitar valores numéricos e cadastre-os em uma lista.Caso o numero já exista lá dentro, ele não será adicionado.No final serão exibidos todos os valores únicos digitados em ordem crescente'''
num = list()
while True:
    n = (int(input('Digite um numero: ')))
    if n not in num:
       num.append(n)# insere os valores da variável (n) na lista (num)
       print('Valor adicionado com sucesso!!')
    else:
        print('Valor ja cadastrado, tente outra vez!!')
    continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continua in 'N':
        break
num.sort()# Coloca a lista em ordem crescente
print(f'OS valores digitados são: {num}')
print('Fim do Programa!!')



