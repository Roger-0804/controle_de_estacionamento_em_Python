'''Faça um programa que leia nome e media de um aluno,guardando também a situação em um dicionário.No final, mostre o conteúdo da estrutura na tela.'''

nome = str(input('Nome: '))
media = float(input(f'Media de {nome}:'))
resultado = {}
resultado['Nome'] = nome
resultado['Media'] = media
if media >= 7:
    resultado['situacao'] = 'aprovado'
elif 5 <= media < 7:
    resultado['situação'] = 'Em recuperação'
else:
    resultado['situacao'] = 'reprovado'
'''print(f'Media igual a {media}')'''
for k ,v in resultado.items():
    print(f'{k} é igual a {v}')
