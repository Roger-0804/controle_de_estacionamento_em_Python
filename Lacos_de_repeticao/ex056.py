'''56.Desenvolva um programa que leia o nome , idade e sexo de 4 pessoas.No final do programa mostre:
* A media de idade do grupo
* Qual é o nome do  homem mais velho
* Quantas mulheres tem menos de 20 anos.'''
somaidade = 0
mediaidade = 0
homemMaisVelho = 0
nomeHomem = 0
mulherMaisNova = 0
for cont in range(1,5):
    nome = input('Qual é o seu nome?').strip()
    idade =  int(input('Qual a sua idade?'))
    sexo = input('Qual o seu sexo [ M/F]').strip()
    print(('-='*20))
    somaidade += idade
    if cont  == 1  and sexo in 'Mm':
        homemMaisVelho  = idade
        nomeHomem = nome
    if sexo in 'Mm' and idade > homemMaisVelho:
        homemMaisVelho = idade
        nomeHomem = nome
    if  sexo in 'Ff' and idade < 20:
        mulherMaisNova += 1
mediaidade = somaidade / 4
print('''A media de idade é de {} anos \n O homem mais velho é {} \n Temos {} mulheres com menos de 20 anos'''.format(mediaidade,nomeHomem,mulherMaisNova))





