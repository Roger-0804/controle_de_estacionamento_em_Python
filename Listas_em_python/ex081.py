'''81. Crie um programa que leia varios numeros inteiros e coloque-os em uma lista.Depois disso mostre:
a, Quantos numeros foram  digitados:
b,  A lista de valores ordenada de forma decrescente:
c, Se o valor : 5 foi digitado e está ou não na lista.'''

lista= list()
while True:
     lista.append(int(input('Digite um valor: ')))
     resp = str(input('Quer continuar [S/N]? '))
     if resp in 'Nn':
        break
print(f'Foram digitados : {len(lista)} valores')
lista.sort(reverse=True)# Imprime na tela a lista em ordem  decrescente
print(f'A lista em ordem decrescente é :{lista}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não apareceu em nenhuma posição da lista')


