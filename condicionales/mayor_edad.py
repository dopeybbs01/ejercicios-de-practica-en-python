"""
Script en python que solicite la edad del usuario y si
esa edad es mayor o igual a 18 indicale que ya es mayor de
edad.

"""
print("Saber si eres mayor de edad\n")
adult = 18
user_age = int(input("Ingresa tu edad\n"))

if user_age >= adult:
    print("Felicidades. Eres mayor de edad")
print("Que tengas un buen dia")