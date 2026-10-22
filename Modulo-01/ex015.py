dias = int(input('Quantos dias ficou com o carro alugado? '))
km = float(input('Quantos km rodados? '))
valor_dias = dias * 60
valor_km = km * 0.15
total = valor_dias + valor_km
print('Ele ficou com o carro por {} dias e rodou {:.2f}km, total a pagar será {:.2f}.'.format(dias, km, total))
