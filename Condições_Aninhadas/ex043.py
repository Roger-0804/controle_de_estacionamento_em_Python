'''43.Desenvolva uma lógica que leia o peso  e a altura de uma pessoa , calculando seu IMC e mostre seu status de acordo com a tabela abaixo:
 * Abaixo de 18.5 : Abaixo do peso
 * Entre 18.5 e 25 : Peso Ideal
 * 25 até 30 : Sobrepeso
 * 30 até 40 : Obesidade
 * Acima de 40: Obesidade Mórbida'''

print('-'*20, ' Calculo de IMC ','-'*20)

peso = float(input('Digite o seu peso:'))
altura = float(input('Digite a sua altura:'))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Você está com o peso abaixo do ideal seu IMC é de {:.1f}'.format(imc))
elif imc  <= 25:
    print('Parabéns você está com seu peso ideal seu IMC é de {:.1f}'.format(imc))
elif imc <= 30:
    print('O seu peso está um pouco acima , você está com sobrepeso IMC:{:.1f}'.format(imc))
elif imc <= 40:
    print('Você está com começo de obesidade , faca uma dieta IMC :{:.1f}'.format(imc))
else:
    print('Você tem Obesidade Morbida, procure um médico e se cuide IMC: {:.1f}.'.format(imc))

