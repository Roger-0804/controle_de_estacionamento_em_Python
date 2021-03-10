'''85.Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantém separado os valores pares e ímpares.No final mostre os valores pares e ímpares em ordem crescente. '''
lista =[ [],[]]
for c in range(1,8):
    v = int(input('Digite o {}° numero: '.format(c)))
    if v % 2 ==0:
        lista[0].append(v)
    else:
        lista[1].append(v)
print('-='*30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares são: {lista[0]}')
print(f'OS valores ímpares são: {lista[1]}')


