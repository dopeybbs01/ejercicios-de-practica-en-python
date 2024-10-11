"""
Script en python que genere un numero aleatorio entre 1 y 10
y le pida al usuario que intente adivinarlo. Si adivina el
numero que lo felicite por su logro.

"""
print("Adivina el numero\n")

# agrega el modulo randon a mi programa y con
# ello me permite generar numero aleatorios.

import random

secret_number = random.randint(1,10)

user_number = int(input("Ingrese un numero\n"))

if user_number == secret_number:
    print("Felicidades. Logro superado")
print("adios")