# média de notas

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))

m = (n1 + n2) / 2

print(f'A media entre {n1} e {n2} é {m:.2f}')

if m >= 6:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')