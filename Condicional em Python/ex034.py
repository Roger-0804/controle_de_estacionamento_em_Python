'''34.Escreva um programa que pergunte o salario de um funcionário e  calcule seu aumento.Para salários superiores a R$ 1250,00,calcule um aumento de 10 %, para os inferiores o aumento é de 15%'''

print('-'*20,'Aumento de salário','-'*20)
sal = float(input('Digite o seu salário R$:'))
if sal<=1250:
    novo_sal=sal*1.15
else:
    novo_sal=sal*1.10
print( '* O seu novo salário será de R$ {:.2f}'.format(novo_sal))


