'''51.Desenvolva um programa que leia o primeiro termo e a razão de uma PA .No final, mostre os 10 primeiros termos dessa progressão:'''

print('\033[1;30m{:=^50}\033[m'.format('\033[1;32mProgressao Aritmética\033[m'))
p1 = int(input('\033[7;30mDigite qual sera o primeiro termo da progressão:\033[m'))
passo = int(input('Qual será a razão dessa progressão?'))
decimo =  p1 + (10-1) * passo #Formula usada para calcular o décimo termo de uma progressão aritmética considerando  a razao.
for c in range(p1,decimo+passo,passo):
    print('{}'.format(c),end=' => ')
print('Fim')
