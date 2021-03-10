from random import choice
print('-'*10,'Aluno escolhido','-'*10)
a1=str(input('primeiro aluno:'))
a2=str(input('segundo aluno:'))
a3=str(input('terceiro aluno:'))
a4=str(input('quarto aluno:'))
escolha=[a1,a2,a3,a4]
escolhido=choice(escolha)
print('O aluno escolhido sera:{}'.format(escolhido))