l=float(input('Qual a largura da parede: ?'))
a=float(input('Qual a altura da parede? :'))
area=l*a
print('Sua parede tem a dimensão de {:.0f} x {:.0f} e sua área é de {}m².'.format(l,a,area))
tinta=area/2
print('para pintar essa parede , voce vai precisar de {}l de tinta.'.format(tinta))