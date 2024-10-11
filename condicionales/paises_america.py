"""
Script en python que muestre un menú con los nombres de distinto países de América y si el usuario selecciona alguna de las opciones se le mostrará el nombre de la capital de ese país.

"""

print('''               Capitles de América
      1) México
      2) Uruguay
      3) Colombia
      4) Argentina
      5) Ecuador
      6) Perú
      ''')

country = int(input("Seleccione una opción: "))

match country:
    case 1:
        print("Ciudad de MéXico")
    case 2:
        print("Montevideo")
    case 3:
        print("Bogota")
    case 4:
        print("Buenos Aires")
    case 5:
        print("Quito")
    case 6:
        print("Lima")
    case _:
        print("Opción invalida")