# conversão

n = float(input("Quanto dinheiro você tem na carteira? R$"))
tx = float(input("Qual a taxa de câmbio do dólar hoje? US$"))
d = n / tx
print(f"Com R${n} você pode comprar US${d:.2f}")