'''27.Faca um programa  que leia o nome completo de uma pessoa ,mostrando em seguida o primeiro e o ultimo nome separadamente:'''

nome = str(input('Digite o seu nome completo:'))
dividido=nome.split()
print('* O seu primeiro nome é:{}'.format(dividido[0]))
print('* O seu ultimo nome é:{}'.format(dividido[-1]))
