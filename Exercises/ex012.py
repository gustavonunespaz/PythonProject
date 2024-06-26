# desconto

p = float(input('Qual o preço do produto? '))
d = float(input('Qual o desconto? '))

n = p - (p * d / 100)

print(f'O valor do seu produto é R${p:.2f} com desconto de {d:.0f}% fica R${n:.2f}.')
