"""
Desarrollar un algoritmo que permita ingresar un número entero positivo. La computadora debe mostrar la sucesión de números pares desde el número ingresado hasta el cero (inclusive), en una sola línea:

Ejemplo: Si ingresa 15, debe mostrar: 14 12 10 8 6 4 2 0
"""

number = int(input("Ingrese un numero entero positivo "))
if number > 0:
    if number % 2 != 0:
        number = number - 1
    for counter in range(number, -1, -2):
        print(str(counter) + " ", end="")
else:
    print("ERROR. debe ingresar un numero positivo.")
