'''80. Crie um programa onde os usuarios possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort() ).No final mostre a lista ordenanda na tela.'''
val=[]
mai =0
for c in range(0,5):
    v =int(input('Digite um valor: '))
    if c == 0 or v > val[-1]:
        val.append(v)
        print(f'Adicionado na ultima posição da lista!!!')
    else:
       pos =0
       while pos < len(val):
         if v <= val[pos]:
            val.insert(pos,v)
            print(f'Adicionado na posição {pos} da lista...')
            break
         pos+=1
print(f'=-'*30)
print(f'Os valores digitados em ordem forma{val}')


