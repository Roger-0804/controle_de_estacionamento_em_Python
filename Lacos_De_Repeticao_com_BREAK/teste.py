
valor = int(input('Qual o  valor que você deseja sacar R$:'))
total = valor
contCedulas = 0
nota = 100
while True:
    if total >= nota:
        total -= nota
        contCedulas += 1
    else:
        if contCedulas > 0:
            print(f'Voce receberá:\n {contCedulas} cedulas de {nota} reais')
        if nota == 100:
            nota = 50
        elif nota ==50:
            nota =20
        elif nota ==20:
            nota =10
        elif nota ==10:
            nota = 5
        elif nota ==5:
            nota =1
        contCedulas = 0
        if total == 0:
            break



