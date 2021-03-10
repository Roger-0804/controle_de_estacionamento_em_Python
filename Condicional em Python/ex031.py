'''31.Desenvolva um programa que pergunte a distância de uma viagem em km, calcule o preço da passagem,cobrando R$ 0,50 por km para viagens de ate 200km e R$ 0,45 para viagens mais longas, '''


print('-'*10,'Companhia Aérea','-'*10)
dist=float(input(' * Qual a distância em Km da sua viagem?'))

pas=(dist*0.50 if dist==200 else dist*0.45)
print('A sua passagem é de R${}'.format(pas))

