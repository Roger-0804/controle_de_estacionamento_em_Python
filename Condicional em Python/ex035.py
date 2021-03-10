'''35.Desenvolva um programa que leia três retas e diga ao usuário se elas podem ou não formam um triângulo:'''


print('-'*20,'\033[7;33;41mCriando triângulos\033[m','-'*20)

a = float(input('Digite o valor do lado a:'))
b = float(input('Digite o valor do lado b:'))
c = float(input('digite o valor do lado c:'))

if  a<b+c and b<c+a and c<a+b:
    print('Os lados formam um triângulo')
else:
    print('Os lados nao formam um triangulo')
