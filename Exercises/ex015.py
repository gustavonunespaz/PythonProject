# aluguel de carro

dias = int(input('Por quantos dias alugou o carro? '))
km = float(input('Quantos KM rodados? '))

pago = (dias * 60) + (km * 0.15)

print(f'O total a pagar e de R${pago:.2f}\n O valor a pagar pelos dias é de R${dias * 60:.2f}\n O valor a pagar pelos KM rodados é de R${km * 0.15:.2f}')