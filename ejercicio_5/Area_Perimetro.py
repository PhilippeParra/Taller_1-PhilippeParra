"""PROGRAMA PARA HALLAR EL
AREA Y PERIMETRO DE UN CIRCULO"""

#input

R = input("Digite el Radio de la circunferencia: ")
R = int(R)

import math
P = math.pi

#processing
Z1 = P * (R**2)
Z2 = 2 * P * R

#output

print("El area del circulo con Radio de " + str(R) + "cm es de " + str(Z1) + "cm \nY su Perimetro es de " + str(Z2) + "cm")