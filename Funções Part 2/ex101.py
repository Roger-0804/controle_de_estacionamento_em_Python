'''101.Crie um programa que tenha uma função chamada voto(), que vai receber como parâmetro o ano  de nascimento de uma pessoa,retornando um valor literal , indicando se uma pessoa tem o voto negado , opcional ou obrigatório.'''

def voto(ano):
    from datetime import date #Escopo de importação(A importação neste caso funcionará somente para a função, ou seja e uma classe que só funciona dentro da função voto( )
    hoje = date.today().year
    idade = hoje - ano
    print('-='*30)
    if idade < 16:
        return f'Com {idade} anos o voto é negado'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é opcional'
    else:
        return f'Com {idade} anos o voto é  obrigatório'

print('=-'*30)
nasc = int(input('Digite sua data de nascimento:'))
print(voto(nasc))
