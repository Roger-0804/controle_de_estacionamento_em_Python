'''.72 Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.'''

valores =('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    continua = ''
    while continua in 'S':
        numero = int(input('Digite um número entre 0 e 20: '))
        print( f'O numero digitado corresponde por extenso a :{valores[numero]}')
        continua = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    else:
        print('Fim do programa')
        break
















