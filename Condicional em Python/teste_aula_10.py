'''carro=int(input('Quanto tempo de uso tem seu carro?'))
print('Carro novo'if carro<=3 else'Carro velho')'''

n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota:'))
m=(n1+n2)/2
if m>=6:
    print('Voce foi aprovado,sua media foi :{:.1f}'.format(m))
else:
    print('Você infelizmente não passou,sua media foi :{:.1f}'.format(m))