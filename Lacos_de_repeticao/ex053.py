'''53.Crie  um programa que leia uma frase qualquer e diga se ela é ou não um PALÍNDROMO,  desconsiderando os espaços:'''

frase = str(input('digite uma frase:')).strip().upper()
palavra  =  frase.split()
junta = ''.join(palavra)
inverso = ''
inverso = junta[::-1]
print(' O inverso de {} é {}'.format(junta,inverso))
'''for letra in range (len(junta)-1,-1,-1):
    inverso += junta[letra]'''
if inverso == junta:
    print('Temos um PALÌNDROMO')
else:
    print('A Frase digitada não é um PALÌDROMO!')


