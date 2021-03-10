'''77.Crie um programa que tenha uma tupla com várias palavras(não usar acentos), depois disso você deve mostrar para cada palavra, quais são suas vogais:'''

box = ('Alfabeto','Dicionario','Bicicleta','Biblioteca','Leite','Mamae')
#Na tuplas, cada palavra também é considerada como uma lista
print('-='*30)
for p in box:
    print(f'\nNa palavra {p.upper()} temos as vogais: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(),end='')

