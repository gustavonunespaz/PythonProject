# contabilidade

saldo = float(input('Qual o saldo atual? '))
luz = float(input('Qual o valor da conta de luz? '))
agua = float(input('Qual o valor da conta de água? '))
internet = float(input('Qual o valor da conta de internet? '))
credito1 = float(input('Qual o valor do cartão de crédito Nubank? '))
credito2 = float(input('Qual o valor do cartão de crédito Azul? '))
credito3 = float(input('Qual o valor do cartão de crédito Renner? '))

total = luz + agua + internet + credito1 + credito2 + credito3
print('O valor total das contas é de: ', total)
print('Seu saldo atual é de: ', saldo - total)
