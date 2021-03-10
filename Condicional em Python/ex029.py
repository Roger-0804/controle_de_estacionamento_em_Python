'''29.Escreva um programa que leia a velocidade de um carro .Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.'''


print('-'*10,'Radar Eletronico','-'*10)
vel=float(input('* Qual a velocidade do veiculo?'))
if vel>80:
    print('O veiculo ultrapassou o limite da via : 80 km/h')
    multa=(vel-80)*7
    print('A sua multa será de :R$ {}'.format(multa))
print('Tenha um bom dia e  dirija com seguranca')

