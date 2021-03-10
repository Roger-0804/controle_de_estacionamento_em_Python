num = int(input('Digite um numero:'))

u= num//1 %10
d=num//10%10
c=num//100%10
m=num//1000%10
#para saber a unidade, dezena, centena em milhar do numero, foi utilizado o operador matemático de divisão exata, dividindo pelo o valor de casas que se desejava
#encontar , e depois utiliza o operador de resto da divisão
print('o numero digitado possui com milhar  o valor: {}'.format(m))
print('o numero digitado possui com centena o valor: {}'.format(c))
print('o numero digitado possui com dezena  o valor: {}'.format(d))
print('o numero digitado possui com unidade o valor: {}'.format(u))

