'''50.Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.Se o valor dgitado for impar ,desconsidere-o.'''
soma = 0
cont = 0
for c in range(1,7):
    n = int(input('digite {}° numero:'.format(c)))
    if n%2 ==0:
       soma += n
       cont += 1
print('Você digitou {} valores pares , e a soma entre eles é {}'.format(cont,soma))

