from math import sin,cos,tan,radians
ang=float(input('Digte um valor para o ângulo a ser definido:'))
s=sin(radians(ang))
c=cos(radians(ang))
t=tan(radians(ang))
print(' * O valor de sen e igual a {:.3f}\n * O valor de cos é igual a {:.3f}\n * E tan é de {:.1f}'.format(s,c,t))
