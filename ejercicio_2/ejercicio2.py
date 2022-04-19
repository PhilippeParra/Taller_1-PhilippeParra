"""PROGRAMA PARA SACAR LA RAIZ
 ENESIMA DE UN NUMERO X"""

 #input

X = input("De un numero base: ")
X = int(X)

N = input("De el valor del exponente: ")
N = int(N)

#Processing

Z = pow( X , 1/N)

#output

print("la raiz elevada a la " + str(N) + " del numero " + str(X) + " tiene como resultado " + str(Z))