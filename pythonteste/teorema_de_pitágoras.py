from math import hypot
print('-'*10,'Caculando a hipotenusa','-'*10)
co=float(input('Informe um valor para o cateto oposto:'))
ca=float(input('Informe um valor para o cateto  adjacente:'))
h=hypot(ca,co)
print('O valor da hipotenusa do triângulo  é de :{:.1f}'.format(h))
