"""
script en python que pregunnte al usuario cuanto indica
el termometro y si ese valor se encuentra entre 18 y 27 que
le indique que la temperatura es agradable.
"""

temp = int(input("¿Cuanto indica la temperatura?\n"))

if temp >= 18 and  temp <= 27:
    print("El clima esta agradable")

print("Nos vemos pronto")