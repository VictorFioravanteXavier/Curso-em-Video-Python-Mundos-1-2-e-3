import math


angulo = float(input('digite o angulo: '))

angulo_rad = math.radians(angulo)

seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"O seno de {angulo} graus é {seno:.2f}")
print(f"O cosseno de {angulo} graus é {cosseno:.2f}")
print(f"A tangente de {angulo} graus é {tangente:.2f}")