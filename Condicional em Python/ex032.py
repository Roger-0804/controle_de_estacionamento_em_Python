'''32.Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''


from datetime import date    # Bibioteca importada para se trabalhar com datas.
print('-'*10,'Ano Bissexto','-'*10)
ano=int(input('Qual é o ano que você quer analisar?,coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano =date.today().year    # Metodo da classe 'date' que utiliza a data atual do sistema
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))