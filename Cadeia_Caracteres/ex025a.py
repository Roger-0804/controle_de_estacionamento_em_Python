'''25.Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome:'''

nome=str(input('DIGITE SEU NOME:')).strip()
print('O seu nome possui Silva? \n{}'.format('SILVA' in nome.upper()))