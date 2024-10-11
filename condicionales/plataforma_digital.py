"""
Scritpt en python que simule un sistema de validación de una plataforma digital. El usuario deberá proporcionar tanto su nombre como la contraseña. Si los valores coinciden con los previamente almacenados entonces se le dará la bienvenida, sino se le indicará que hubo un error.

"""

# Declaraciones de constante.

USER_NAME = "iani"
PASSWORD = 123456

print("Proporciona los siguientes datos:")
user_name = input("Usuario: ")
password = int(input("Contraseña: "))

if user_name == USER_NAME and password == PASSWORD:
    print(f"Bienvenido a tu cuenta {user_name}.")
else:
    print("Datos incorrectos.")

print("Que tengas un buen día")