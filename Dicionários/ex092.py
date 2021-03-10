'''92.Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com- idade) em um  dicionário se por acaso a CTPS for diferente de zero,o dicionário receberá também o ano de contratação e o salário.Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar'''
from datetime import date
from time import sleep
cadastro = dict()

cadastro['nome'] = str(input('Nome:'))
nascimento = int(input('Data de nascimento: '))
cadastro['Idade']= date.today().year -nascimento
cadastro['CTPS'] = int(input('Digite o numero da CTPS: '))
if cadastro['CTPS'] != 0:
    cadastro['Ano de Contratação'] = int(input('Qual o ano de sua primeira contratação:?'))
    cadastro['Salario'] = float(input('Qual foi o salário?\nR$:'))
    print('=-'*10,'Calculando os seus dados','-='*10)
    sleep(0.5)
    print(f'-O trabalhador com nome :{cadastro["nome"]}')
    print(f'-Com a idade de : {cadastro["Idade"]}')
    print(f'Carteira de trabalho :{cadastro["CTPS"]}')
    print(f'Foi contratado pela primeira vez em:{cadastro["Ano de Contratação"]}')
    print(f'Com um salário inicial igual a {cadastro["Salario"]}')
    print(f'-Tem a previsão de se aposentar e com {(cadastro["Ano de Contratação"] - nascimento) + 35} anos de idade')
else:
    print('=-' * 10, 'Calculando os seus dados', '-=' * 10)
    sleep(0.5)
    print(f'-O trabalhador: {cadastro["nome"]}')
    print(f'-Com idade: {cadastro["Idade"]} anos')
    print('- Não possui carteira de trabalho')
