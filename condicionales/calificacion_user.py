"""
script en python que le solicite al usuario una calificacion y una cantidad de asitencia a un curso. Si la calificación y cantidad de asistencias son aprobatorias entonces se le felicita por su logro; en caso contrario se le indicará en que falló. La calificación mínima aprobatoria será de 60 y la cantidad mínima de asistencias será de 24.

"""

MINIMUM_QUALIFICATION = 60
MINIMUM_ASSISTENCE = 24

print("Porfavor ingrese sus datos")
qualification = int(input("Calificación: "))
assistence = int(input("Aistencias: "))

if qualification >= MINIMUM_QUALIFICATION and assistence >= MINIMUM_ASSISTENCE:
    print("Felicidades, aprobaste el curso.")

elif qualification < MINIMUM_QUALIFICATION and assistence >= MINIMUM_ASSISTENCE:
    print(f"Calificación insuficiente. La cantidad minima es: {MINIMUM_QUALIFICATION}")

elif qualification >= MINIMUM_QUALIFICATION and assistence < MINIMUM_ASSISTENCE:
    print(f"Asistencias insuficientes. La cantidad minima es: {MINIMUM_ASSISTENCE}")
else:
    print("Calificació y asistencias insuficientes.")