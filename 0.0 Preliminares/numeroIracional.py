import math

pitagoras = lambda x, y: math.sqrt(x**2 + y**2)
pi = lambda circumference, diameter: circumference/diameter

print(pitagoras(1, 1))
print(pi(59.69, 19))

