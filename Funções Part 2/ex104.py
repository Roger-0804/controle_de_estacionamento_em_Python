'''104.Crie um programa que tenha a função leiaInt() que vai funcionar de forma semelhante  a função input( ) do Python, só que fazendo a validação dos dados para aceitar apenas um valor numérico.
'''


def leiaInt(msg):
    valor =0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor =int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um valor numérico válido!\033[m')
        if ok:
            break
    return valor

# Programa principal
n = leiaInt(('Digite um numero: '))
print(f'Você acabou de digitar um numero:  {n}')