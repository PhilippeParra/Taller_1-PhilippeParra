"""PROGRAMA PARA CALCULAR EL IVA Y 
 PRECIO DE VENTA DE UN PRODUCTO"""

print("-----------------------------------")
print("---- IVA Y PRECIO DE VENTA --------")
print("-----------------------------------")

# input

X = input("Digite el valor del producto: ")
X = int(X)
Y = input("Digite el porcentaje del iva: ")
Y = int(Y)

# processing

Z1 = (X * Y)/100
Z2 = Z1 + X

# output

print("El iva del producto con valor base de " + str(X) + " y " + str(Y) + "% de iva es " + str(Z1))

print("El valor final del Producto con valor base " + str(X) + " mas el iva del " + str(Y) + "% es" + str(Z2))