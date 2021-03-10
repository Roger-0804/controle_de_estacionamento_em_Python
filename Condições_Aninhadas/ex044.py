"""44.Elabore um programa que calcule o valor a ser pago por um produto,considerando o seu preço normal e condição de pagamento:

* A vista: (Dinheiro/Cheque:) 10% de desconto
* A vista (Cartão) 5% de desconto
* Em até 2x no cartão: preço normal
* 3x ou mais no cartão: 20% de juros."""

print('{:=^50}'.format(' \033[7;30mCaixa da loja\033[m ')) #'{:=^50}' Formataçao para centralizar o titulo e decorar em ambos os lados
print('\033[1;30mDigite a sua forma de pagamento\n\033[m' '\033[1;30m* 1- Dinheiro\n\033[m''\033[1;30m* 2-Cartão de Débito\n\033[m''\033[1;30m* 3- Credito em 2x\n\033[m''\033[1;30m* 4- Credito  em 3x ou mais\033[m')

valor = float(input('\033[1;33mQual o valor da mercadoria : R$\033[m'))
fp =int(input('\033[1;34mQual a forma de pagamento?\033[m'))

if fp == 1:
    desc =  valor - (valor*0.10)
    print('O valor a ser pago, será de R${}'.format(desc))
elif fp == 2:
    desc = valor - (valor*0.05)
    print('O valor a ser pago , será de R$ {}'.format(desc))
elif fp == 3:
    pag = valor/2
    print('O valor a ser pago sera de 2x de R$ {} que corresponde ao valor de R$ {} sem juros e descontos!!'.format(pag,valor))
elif fp == 4:
    nparc=int(input('\033[1;32mDigite em quantas vezes acima de tres deseja fazer:\033[m'))
    juros = valor +(valor*(20/100))
    parcela = juros/nparc
    print('\033[1;31m O valor a ser pago será  de  {}x de R$ {:.2f}, totalizando o valor de R$ {:.2f}\033[m'.format(nparc,parcela,juros))
else:
    print('\033[1;36mCondição Inválida\033[m')







