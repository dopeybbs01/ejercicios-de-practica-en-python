# Se requiere un programa que calcule la edad del usuario

print("Calculadora para saber tu edad\n")

year_birth = int(input("ingresa el año en que naciste\n"))
current_year = int(input("Ingresa el año actual\n"))

age = current_year - year_birth

print(f" Tu edad es {age} años ó {(age - 1)}")
