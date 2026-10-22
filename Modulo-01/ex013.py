salário = float(input('Qual valor do seu salário? R$'))
aumento = salário * 15 / 100
novo = salário + aumento
print('O seu novo {:.2f} em 15% de aumento fica {:.2f}.'.format(salário, novo, aumento))
