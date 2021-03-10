# Escopo de Variáveis

'''def teste(b):
    global a
    a = 3
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')




a = 5
teste(a)
print(f'A fora vale {a}')'''

# Retorno de Valores

def somar(a = 0, b = 0 ,c = 0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)

print(f'Os resultados foram {r1}, {r2} e {r3} respectivamente')



def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num =  int(input('Digite um numero:'))
if par(num):
    print('É par')
else:
    print('Não é par')