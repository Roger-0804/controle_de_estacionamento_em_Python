'''pessoas = { 'nome': 'Gustavo','sexo':'M','idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.items())
pessoas['nome'] = 'Leandro'
for k,v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil =[]
estado1 = {'uf': 'Rio de janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['sigla'])'''

'''estado = dict()
brasil =[]
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem a valor {v}.')'''
dados =[]

filmes =dict()

filmes1 ={ 'Nome':'John Wick','Ator':'Keanu Reeves','Gênero':'Ação'}
filmes2 ={ 'Nome': 'Titanic','Ator':'Leonardo diCaprio','Gênero':'Suspense'}
filmes1['ano'] = 2017
filmes2['ano'] = 1997
dados.append(filmes1.copy())
dados.append(filmes2.copy())
filmes['Gênero'] ='Luta'
print(f'O filme {filmes2["Nome"]} é do tipo :{filmes2["Gênero"]}')
print(filmes2.keys())
print(filmes2.items())
'print(dados)'