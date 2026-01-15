print("*** Diccionario en Python ***")

#Creamos un dict de personas con clave y valor
persona = {
    "nombre" : "sergio",
    "edad" : 30,
    "ciudad" : "mexico"
}

print(f"Diccionario de personas: {persona}")

# Acceder a los elementos del diccionario
print(f"Nombre: {persona["nombre"]}")
print(f"Edad: {persona.get("edad")}")
print(f"Ciudad: {persona.get("ciudad")}")
