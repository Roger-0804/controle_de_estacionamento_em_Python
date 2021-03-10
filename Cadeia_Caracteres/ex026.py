'''Faça um programa que leia uma frase pelo teclado e mostre:

*Quantas vezes aparece a letra"A":
*Em que posição ela aparece a primeira vez:
*Em que posição ela aparece a ultima vez:
'''

frase=str(input('Digite uma frase:')).lower().strip() # O objeto frase recebeu os metodos para passar a string toda para mauiscula e juntar os espacos antes e depois dela 
print(' A letra: A aparece  {} vezes'.format( frase.count('a')))
print('Ela aparece pela primeira vez na {}ºposicao'.format(frase.find('a')+1))
print('Ela apareceu pela última  vez na {}ºposicão'.format(frase.rfind('a')+1))
