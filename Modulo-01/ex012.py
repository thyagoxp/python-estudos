preço = float(input('Qual valor do produto? R$'))
desconto = preço * 5 / 100
valor = preço - desconto
print('O valor do produto era {:.2f} e com 5% de desconto fica {:.2f}'.format(preço, valor, desconto))

