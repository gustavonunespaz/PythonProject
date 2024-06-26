# angulo

import math

angulo = float(input("Qual o valor do angulo? "))

seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f"O seno de {angulo} é {seno:.2f}.")
print(f"O cosseno de {angulo} é {cos:.2f}.")
print(f"A tangente de {angulo} é {tan:.2f}.")