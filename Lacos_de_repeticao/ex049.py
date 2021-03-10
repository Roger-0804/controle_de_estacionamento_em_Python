'''49.Refaça o desafio 09, mostrando a tabuada de um numero que o usuário escolher, só que agora utilizando o laço FOR:'''

num = float(input('Digite o valor que se deseja saber a tabuada:'))
for c in range(0,11):
    multiplicacao = num * c
    print('{:.0f} x {} = {:.0f}'.format(num,c,multiplicacao))
   