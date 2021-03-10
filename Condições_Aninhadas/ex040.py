'''40.Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- media abaixo de 5.0:
            reprovado
- media entre 5.0 e 6.9:
            recuperaçaõ
- media 7.0 ou superior:
            aprovado
'''

print('=-'*10,'Calculando sua média','-='*10)

nota1 = float(input('Digite a sua primeira nota:'))
nota2 = float(input('Digite a sua segunda nota:'))

media = (nota1 + nota2)/2

if media < 5.0:
    print('Aluno reprovado, sua media foi igual a : {}'.format(media))
elif media <=6.9:
    print('Aluno em recuperação sua media foi igual a :{}'.format(media))
else:
    print('Aluno aprovado você obteve uma media de :{}, Parabéns!!!!'.format(media))



