"""
Escriba un programa que pida el peso (en kilogramos) y la altura (en metros) de una persona y que calcule su índice de masa corporal (imc).

Se recuerda que el imc se calcula con la fórmula imc = peso / altura 2
"""

print("CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)")
peso = float(input("¿Cuánto pesa? "))
altura = float(input("¿Cuánto mide en metros? "))

imc = peso / altura ** 2

print(f"Su imc es {round(imc, 1)}")

print("Un ímc muy alto indica obesidad. Los valores normales de imc están entre 20 y 25,")

print("pero esos límites dependen de la edad, del sexo, de la constitución física, etc." )

