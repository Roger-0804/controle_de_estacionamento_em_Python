'''57 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a  digitação novamente até ter um valor correto.'''

sexo = str(input('informe o seu sexo [M/F]')).upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados errados,Informe o seu sexo [M/F]')).upper()[0]
print('O sexo informado corresponde a {}'.format(sexo))
print('Acabou')