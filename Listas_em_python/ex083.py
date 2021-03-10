'''83.Crie um programa onde o usuario digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
item = str(input('Digite a sua expressão: '))
expr =list()
for simb in item:
    if simb == '(':
        expr.append('(')
    elif simb ==')':
        if len(expr) > 0:
          expr.pop()
        else:
          expr.append(')')
          break
if len(expr) == 0:
    print('A sua expressão está válida !')
else:
    print('A sua expressão está inválida !')

