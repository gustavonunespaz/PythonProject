# cateto cateto hipotenusa

import math
a = float(input('Cateto Adjacente: '))
b = float(input('Cateto Oposto: '))
c = math.hypot(a, b)
print(f'A hipotenusa vai medir {c:.2f}.')