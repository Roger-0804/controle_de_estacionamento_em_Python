'''.60 Faça um programa que leia um numero qualquer e mostre o seu fatorial'''
'''f =1
n = int(input('Digite um numero:'))
c = n
print('Calculando o {} !:'.format(n), end='')
while c > 0:
   print('{}'.format(c), end = '')
   print(' x ' if c > 1 else ' = ', end='')
   f = f * c
   c -= 1
print('{}'.format(f))'''
# O algoritimo acima foi desenvolvido utilizado o método: 'WHILE'

'''f =1
n = int(input('Calcule o fatorial do numero:'))
for c in range(n,0,-1):

    print(c,end='')
    print(' x ' if c > 1 else '=',end='')
    f = f * c
    c -= 1
print('{}'.format(f))'''

# O Segundo algoritimo foi desenvolvido utilizado o método 'FOR'