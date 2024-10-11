"""
Desarrollar un algoritmo que permita ingresar un monto en dólares (entero). La computadora debe
mostrar cómo pagar ese monto con la menor cantidad de billetes posibles.
Ejemplo: Si ingresa 147 dólares, debe mostrar:
▪ 1 billete de U$S 100
▪ 0 billetes de US$ 50
▪ 2 billetes de US$ 20
▪ 0 billetes de U$S 10
▪ 1 billete de U$S 5
▪ 1 billete de US$ 2
▪ 0 billetes de U$S 1

"""
CANT_100 = 100
CANT_50 = 50
CANT_20 = 20
CANT_10 = 10
CANT_5 = 5
CANT_2 = 2

amount = int(input("Ingresa el monto en dolares: "))


cant_100 = amount // CANT_100
amount = amount % CANT_100

cant_50 = amount // CANT_50
amount = amount % CANT_50

cant_20 = amount // CANT_20
amount = amount % CANT_20

cant_10 = amount // CANT_10
amount = amount % CANT_10

cant_5 = amount // CANT_5
amount = amount % CANT_5

cant_2 = amount // CANT_100
amount = amount % CANT_2

print(f"cantidadS de billetes de 100: {cant_100}")
print(f"cantidad de billetes de 50: {cant_50}")
print(f"cantidad de billetes de 50: {cant_20}")
print(f"cantidad de billetes de 50: {cant_10}")
print(f"cantidad de billetes de 50: {cant_5}")
print(f"cantidad de billetes de 50: {cant_2}")
print(f"cantidad de billetes de 50: {amount}")
