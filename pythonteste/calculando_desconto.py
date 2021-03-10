produto=float(input('Digite o valor da mercadoria:'))
desconto=((produto)-(5/100*produto))
print('O valor da mercadoria é R$ {:.3f}, e com desconto é de :R${:.3f}'.format(produto,desconto))
