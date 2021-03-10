'''42.Refaça o exercício 35, dos triângulos , acrescentando  o recurso  de mostrar que tipo de triãngulo será formado:
* Equilátero
* Isosceles
* Escaleno.
'''

print('!'*10,'Condições para se formar um triangulo e seu tipo','!'*10)

la = float(input('Digite o valor do lado a:'))
lb = float(input('Digite o valor do lado b:'))
lc = float(input('Digite o valor do lado c:'))

if la <(lb+lc) and lb<(la+lc) and lc< (la+lb):
    print('Os trê lados podem formam um triangulo do tipo:  ',end ='')
    if la == lb ==lc:
        print('Equilátero')
    elif la != lb != lc !=la:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os três lado não formam um triângulo')


