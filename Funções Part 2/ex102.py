'''Crie um programa que tenha uma função  fatorial() que receba dois parametros: o primeiro  que indique o numero a calcular e o outro chamado show,que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de calculo fatorial.'''
def fatorial(num,show=False):
    """
    => Função fatorial( ) calcula o fatorial de um número
    :param num: Parâmetro para calcular um número
    :param show:Parâmetro para mostrar o calculo do fatorial
    :return: retorna o valor dos valores fatorados de um numero multiplicados e mostrando o resultado da multiplicação
    """
    f = 1
    print('=-' * 20)
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f
    print('=-'*20)

# Programa Principal
print(fatorial(12,show=True))


