# conversor de medidas

m = float(input('Uma distância em metros: '))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print(f'{m:.2f}m corresponde a {km:.2f}km, {hm:.2f}hm, {dam:.2f}dam, {dm:.2f}dm, {cm:.2f}cm e {mm:.2f}mm. ')