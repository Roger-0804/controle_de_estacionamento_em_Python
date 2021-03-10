'''78. Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.No final mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
valores = []
maior =0
menor =0
for c in range(0,5):
    valores.append((int(input(f'Digite um valor na posição {c}: '))))
    if c == 1:
        maior = menor =valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor =valores[c]
print(f'a lista em ordem é:{sorted(valores)}')
print(f'O maior valor digitado da lista é {maior},nas posições: ',end='')
for i,v in enumerate(valores):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor valor digitado da lista é {menor},nas posições: ',end='')
for i,v in enumerate(valores):
    if v == menor:
        print(f'{i}...',end='')


