"""
script en python que solicita la calificacion y la
 cantidad de asistencia a un curso. si la calficacion es
 mayor que 60 y la cantidad de asistencia es mayor que 20
 entonce que le indique que ha aprobado el curso.

"""
qualification = int(input("¿cual es tu calificación?\n"))
attendance = int(input("¿cual es tu cantidad de asistencia?\n"))


if qualification >= 60 and attendance > 20:
    print("Felicidades. Aprobaste el curso.")

print("sigue disfrutando tu dias")
