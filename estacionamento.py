lista = '00','01','02','03','04'
cheia =[]
while  len(lista) > len(cheia):
    vaga  = (int(input('Digite qual vaga deseja ocupar?')))
    if lista[vaga] in cheia:
        print('Erro vaga ocupada!')
        cheia.pop(-1)
    cheia.append(lista[vaga])
    print(f'A vaga {lista[vaga]} foi ocupada com sucesso!!')
    print(sorted(cheia))
print('O estacionamento está lotado!!')