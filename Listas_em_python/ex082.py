'''82.Crie um  programa que vai ler varios números e colocar em uma lista.Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores ímpares digitados respectivamente. Ao final mostre os conteudos das tres listas gravados.'''

valores = []
pares=[]
impares=[]
while True:
     num= int(input('Digite um valor: '))
     valores.append(num)
     '''if num % 2 == 0:
         pares.append(num)
     else:
         impares.append(num)'''
     resp =str(input('Quer continuar:[S/N]'))
     #Metodo acima usando a estrutura condicional,para alimentar as listas pares e impares juntamente com a lista geral
     if resp in 'Nn':
         break
         ###########################################################
for i,v in enumerate(valores):
    if v % 2 ==0:
        pares.append(v)
    elif v % 2 ==1:
        impares.append(v)
        #metodo utilizando o for para separar os elementos da lista geral em duas listas pares e impares.
print(f'Os valores da lista valores são:{valores}')
print(f'Os valores pares da lista são:{pares}')
print(f'Os valores ímpares da lista são:{impares}')
