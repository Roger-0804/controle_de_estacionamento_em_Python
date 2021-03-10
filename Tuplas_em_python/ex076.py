'''76.Desenvolva um programa que tenha uma tupla unica com nome de produtos e seus respectivos preços na sequencia.No final mostre uma listagem de preços, organizando os dados em forma tabular . '''

tabela = ('Arroz',25.00,
          'Feijão',7.98,
          'Açúcar',11.00,
          'Óleo',7.50,
          'Pão',6.89,
          'Manteiga',12.50,
          'Presunto /Kg',25.00)
print('=-'*30)
print(f'\033[1m{"Lista do Supermercado":^40}\033[m')
print('=-'*30)
for item in range(0,len(tabela)):
    if item %2 ==0:
        print(f'{tabela[item]:.<40}',end='')
    else:
        print(f'R$ {tabela[item]:>5.2f}')
print('=-' * 30)



