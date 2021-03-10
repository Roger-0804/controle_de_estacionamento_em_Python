#Exercicio para fatiar um numero em Python
num=int(input('Leia um numero:'))
u=num//1%10
d=num//10%10
c=num//100%10
m=num//1000%10
print('Analisando um numero{}'.format(num))
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))