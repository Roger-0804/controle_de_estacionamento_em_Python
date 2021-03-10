from datetime import datetime
vagas = (1,2,3,4,5,6,7,8,9,10)
ocupado =list()
cadastrar =''
while cadastrar != 'SN':
    entrada = int(input('Qual vaga será  preenchida? '))
    if entrada not in vagas:
        print('Vaga inexistente!!')
        entrada = int(input('Digite uma vaga válida: '))
    ocupado.append(entrada)
    horario = datetime.now()
    data_e_hora = horario.strftime('%H:%M:%S')
    print(f'Vaga {entrada} preenchida as {data_e_hora} ')
    cadastrar = str(input('Deseja cadastrar mais alguma vaga ocupada [S/N] ?')).strip().upper()[0]
    if cadastrar not in 'SN':
        cadastrar = str(input('Ops...Digite apenas Sim ou Não'))
    if cadastrar == 'N':
        print(f' As vagas que  estão preenchidas são:{ocupado}')


