'''teste= []
teste.append('gustavo')
teste.append(40)
galera=[]
galera.append(teste[:])
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(galera)'''

'''galera=[['Joao',19],['Ana',33],['Joaquim',13],['Maria',45] ]
for p in galera:

    print(f'{p[0]} tem {p[1]} anos de idade')
    print('-' * 20)'''

galera =[]
dado=[]
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()
print(galera)
