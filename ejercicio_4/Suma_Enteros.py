"""PROGRAMA PARA SUMA DE LOS PRIMEROS
N ENTEROS POSITIVOS"""

#input
N = input("Indique el ultimo numero: ")
N = int(N)
X = 0

#processing
for i in range (1 , N+1):
    X = X + i

#output
print("La suma de los " + str(N) + " primeros N enteros positivos es " + str(X))