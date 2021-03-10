'''.69 Crie um programa que leia a idade e  o sexo de várias pessoas.A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer continuar ou não continuar.No final mostre
a, Quantas pessoas tem mais de 18 anos:
b, Quantos homens foram cadstrados :
c, Quantas mulheres tem menos de 20 anos: '''

idade18 = homem=mulher20= 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o seu sexo [M/F]')).upper().strip()[0]
    if idade >= 18:
        idade18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N] ?')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Temos {idade18} pessoas com idade acima dos 18 anos')
print(f'Temos {homem} homens cadastrados')
print(f'E também {mulher20} mulheres com idade abaixo dos 20 anos.')


