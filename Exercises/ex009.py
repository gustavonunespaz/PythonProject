# tabuada

x = float(input('Digite um número: '))
r = int(input('Quantas tabuadas? '))

print(f'{x} x 1 = {x*1}')
print(f'{x} x 2 = {x*2}')
print(f'{x} x 3 = {x*3}')
print(f'{x} x 4 = {x*4}')
print(f'{x} x 5 = {x*5}')
print(f'{x} x 6 = {x*6}')
print(f'{x} x 7 = {x*7}')
print(f'{x} x 8 = {x*8}')
print(f'{x} x 9 = {x*9}')
print(f'{x} x 10 = {x*10}')
print('')
for i in range(1, r+1):
    print(f'{x} x {i} = {x*i}')