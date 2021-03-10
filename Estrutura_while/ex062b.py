'''62 Melhore o desafio 61, perguntando para o usuario se ele deseja que quer mostrar mais alguns termos.O programa  encerra quando ele disser que quer mostrar os termos  .'''
print('Gerador de PA')
print('=-'*20)
primeiro = int(input('Digite o primeiro termo da progressão:'))
razao = int(input('Qual é a razão da progressão? '))
termo  = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} => ',end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você deseja mostrar ?'))
print(f'Progressão finalizada, foram mostrados um total de {total} termos')


