"""
Desarrollar un algoritmo que permita ingresar un número entero positivo. La computadora debe mostrar la sucesión de números pares desde el número ingresado hasta el cero (inclusive), en unasola línea.

Ejemplo: Si ingresa 15, debe mostrar: 14 12 10 8 6 4 2 0
"""

positive__number = int(input("Ingresa un número positivo: "))

if positive__number > 0:
    if positive__number % 2 != 0:  # verificamos si el numero es
        # restamos 1 al valor introducido por el usuario
        positive__number = positive__number - 1

    counter = positive__number

    while counter >= 0:
        print(str(counter) + " ", end="")
        counter = counter-2
else:
    print("El númweo debe ser positivo.")
