"""
Desarrollar un algoritmo que permita ingresar una hora del día (entre 0 y 23, si no, informar un error). La computadora debe mostrar a qué momento del día pertenece según lo siguiente:

▪ Madrugada: Entre 0 y 5, inclusive
▪ Mañana: Entre 6 y 11, inclusive
▪ Mediodía: Entre 12 y 13, inclusive
▪ Tarde: Entre 14 y 19, inclusive
▪ Noche: Entre 20 y 23, inclusive

"""
LOWER_LIMIT = 0
EARLY_MORNING_LIMITS = 5
MORNING = 11
NOON = 13
AFTERNOON = 19
UPPER_LIMIT = 23

hour = int(input(f"Ingrese un horario entre {LOWER_LIMIT} y {UPPER_LIMIT}: "))

if hour < LOWER_LIMIT:
    print("La hora no puede ser negativa.")
elif hour > UPPER_LIMIT:
    print(f"La hora no puede ser mayor que {UPPER_LIMIT}")
elif hour <= EARLY_MORNING_LIMITS:
    print("Es de madrugada.")
elif hour <= MORNING:
    print("Es la mañana.")
elif hour <= NOON:
    print("Es el mediodia.")
elif hour <= AFTERNOON:
    print("Es la tarde.")
else:
    print("Es la noche.")