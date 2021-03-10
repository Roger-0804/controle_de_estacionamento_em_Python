'''36.Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa.O programador vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.Calcule a prestação mensal , sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.'''
print('\033[0;31m=-\033[m'*20)
print('\033[1;30m          Santander Imobiliário  \033[m')
print('\033[0;31m-=\033[m'*20)

valor = float(input('Qual o valor do imóvel a ser financiado?'))
prazo = int(input('Em quantos anos deseja financiar?'))
meses = prazo*12
finaciamento= valor/meses

salario= float(input('Agora eu preciso saber qual a sua renda mensal:'))

if finaciamento <= salario*0.30:
    print('\033[1;34m*Parabéns!! seu financiamento foi aprovado , sua parcela será de R$ {:.1f}\033[m'.format(finaciamento))
else:
    print('\033[1;32m *Infelizmente seu financiamento foi negado,sua parcela foi de {:.1f}, o que excede o permitido\033[m'.format(finaciamento))





