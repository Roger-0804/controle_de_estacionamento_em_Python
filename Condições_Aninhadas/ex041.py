'''41.A confederação Nacional de Natação ´precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria , de acordo coma idade:

# Até 9 anos: mirim
# Até 14 anos : infantil
# Até 19 anos: junior
# Até 25 anos : Sênior
# Acima: master'''
from datetime import date
print('*'*20,'Confederação Nacional de Natação','*'*20)

nasc = int(input('Qual a seu ano de nascimento ?'))
ano = date.today().year

idade = ano - nasc
if idade <= 9:
    print('Sua categoria será :Mirim, pois você tem {} anos'.format(idade))
elif idade <= 14:
    print('Sua categoria será : Infantil , pois você tem {} anos'.format(idade))
elif idade <= 19:
    print('Sua categoria será : Junior , pois você tem {} anos'.format(idade))
elif idade == 25:
    print('Sua categoria será : Sênior, pois você tem {} anos'.format(idade))
else:
    print('Sua categoria será : Master, pois você tem {} anos'.format(idade))
