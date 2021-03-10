din=float(input('Qual o valor em R$ que você tem? :'))
us=float(input('Qual a cotação atual do dolar? :'))
print('Você possuiR${}'.format(din))
print('Logo você possui U$S{:.1f}'.format(din/us))
