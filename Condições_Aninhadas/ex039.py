'''39.Faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade:
* Se ele ainda vai se alistar no serviço militar:
* Se é a hora de se alistar:
* Se já passou do tempo de alistamento:'''


from datetime import date

print('\033[1;33m<\033[m'*10,'\033[4;34mServico Militar Obrigatório\033[m','\033[1;33m>\033[m'*10)

print('''\033[1;30mDigite o seu sexo
[ M ] para Masculino.
[ F ] para Feminino. \033[m''')
opcao = str(input('\033[7mDigite aqui:\033[m')).upper()

if opcao == 'F':
    print('\033[1;31mVocê não precisa se alistar\033[m')

elif opcao == 'M':
    nascimento = int(input('Qual seu ano de nascimento?'))
    ano_atual = date.today().year
    idade = ano_atual - nascimento

    if  idade < 18:
        falta = 18 - idade
        data = nascimento +18
        print('\033[1;33m* Voce ainda não esta na idade de alistamento ,faltam {} anos para você se alistar\033[m'.format(falta))
        print('\033[7;32m O seu alistamento será em {}\033[m'.format(data))

    elif idade == 18:
        print('\033[1;34m* Você já esta na idade de alistamento, compareça o serviço militar mais proximo de sua casa, Marinha, Exército ou Aeronáutica\033[m')

    else :
        passou = idade -18
        data = nascimento + 18
        print('\033[1;30m Sua data  de alistamento foi em {}\033[m'.format(data))
        print('\033[1;31m * Você já passou do prazo em {} anos , compareça a junta militar para regularizar sua situação\033[m'.format(passou))
else:
    print('Opção Inválida, por favor digite entre  M ou F ')
