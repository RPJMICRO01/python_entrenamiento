import random

nombre = input("ingrese su nombre:  ")

apellido = input("cual es tu apellido:  ")

año_nacimiento  = input("cual es tu año de nacimiento:  ")

random_number = str(random.randint(1000, 9999))

print("--" * 22)
print("su id unico es")
print((nombre[0:2]).strip().upper() + (apellido[0:2]).strip().upper() + año_nacimiento.strip()[-2:] + random_number ) 
