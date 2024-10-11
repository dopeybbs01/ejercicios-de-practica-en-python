"""
Script en python que solicite al usuario que intente adivinar
un número entre 1 y 10. Si el usuario adivino entonces lo felicite por su logro; en caso contrario que le indique el número secreto

"""
import random

secret_number = random.randint(1,10)

print("Acabo de generar un número secreto entre 1 y 10")
number = int(input("¿Cúal crees que sea mi numero secreto? "))

if secret_number == number:
    print("felicidades logreo desboqueado")
else:
    print(f"Fallaste el numero era {secret_number}")

print("Que tengas un bonito día.")