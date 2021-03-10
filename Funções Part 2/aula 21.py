
'''def contador(i ,f ,p):

    """

    :param i: Informa qual será o inicio da contagem
    :param f: Informa qual será o final da contagem
    :param p: Informa qual será o passo da contagem
    :return: Sem retorno
    # Conceito de Docstrings
    """
    c = i
    while c <= f:
        print(f' {c} ',end='')
        c += p
    print('Fim')



contador(2,20,2)
help(contador)'''

# Argumentos Opcionais

'''def somar(a = 0,b = 0,c = 0):
    s = a + b + c
    print(f'{s}')


somar(3)'''

# Escopo de variáveis
# Ex:

def funcao():
    N1 = 4
    print(f'N1 dentro vale {N1}')

N1 = 2
funcao()
print(f'N1 fora vale {N1}')

