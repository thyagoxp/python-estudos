real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.03
euro = real / 5.65
print('Com R${:.2f} você pode comprar US${:.2f}, e pode comprar EU${:.2f}'.format(real, dolar, euro))
