'''.57 Faça um programa que leia o sexo  de uma pessoa, mas só aceite os valores 'F' ou 'M'. Caso esteja errado, peça a digitação novamente até ter um valor correto:'''
sexo = str(input('Informe o seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos, por favor digite o seu sexo corretamente:')).strip().upper()[0]
print('O seu sexo é {} , dados salvos com sucesso'.format(sexo))

