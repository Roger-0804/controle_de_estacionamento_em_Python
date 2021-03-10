'''84.Faça um programa que leia o nome e o peso de várias pessoas guardando tudo em uma lista.No final mostre:
a, Quantas pessoas foram cadastradas
b, Uma listagem com as pessoas mais pesadas
c, Uma listagem com as pessoas mais leves'''
pessoas=[]
grupo=[]
mai = men = 0
while True:
    pessoas.append(str(input('Nome:')))
    pessoas.append(float(input('Peso: ')))
    if len(grupo) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    grupo.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'O total de pessoas cadastradas são: {len(grupo)} pessoas ')
print(f'O maior peso foi de {mai}kg.\nPeso de ',end='')
for p in grupo:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso cadastrado foi de:{men} Kg.\nPeso de ',end='')
for p in grupo:
    if p[1] == men:
        print(f'[{p[0]}] ',end='')
print()

