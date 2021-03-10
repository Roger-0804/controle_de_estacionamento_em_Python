nome =input('Digite seu nome :').strip()
print('O seu nome em maiusculo é {}'.format(nome.upper()))
print('O seu nome em minusculo é {}'.format(nome.lower()))
print('O seu nome possui {} letras'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome possui {} letras'.format(nome.find(' ')))
#metodo utilizando o operador '.find(), para achar os espaços em branco na string
separa=(nome.split())
print('o seu primeiro nome possui {} letras'.format(len(separa[0])))
'''metodo acima utilizando uma variável'separa , que recebe o valor da variavel nome, com o operador .split() que separa as strings em indices , e depois mostra
indice  na variavel: 'separa',contando a quantidade de caracteres que ela possui.'''


