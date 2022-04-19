"""PROGRAMA PARA DEVOLVER EL
INVERSO DE UN NUMERO DADO"""

#input

def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10

    return numero

#processing

numero = int(input("Digite el numero a invertir: "))
numero_invertido = invertir_numero(numero)

#output

print("El dado el numero " + str(numero) + " su inverso es " + str(numero_invertido))
