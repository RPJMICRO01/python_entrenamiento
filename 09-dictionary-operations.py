#Creamos un dict de personas con clave y valor
persona = {
    "nombre" : "sergio",
    "edad" : 30,
    "ciudad" : "mexico"
}

# Modificar un valor del diccionario
persona["edad"] = 35
print(f"Diccionario de personas:  {persona}")

# Agregar un nuevo elemento
persona["profesion"] = "Ingeniero"
print(f"Diccionario de persona:  {persona}")

# Eliminar un elemento
del persona["ciudad"]
print(f"Diccionario de persona:  {persona}")

persona.pop("profesion")
print(f"Diccionario de persona:  {persona}")

#Iterar los elementos de un dict (llave, valor), lo toma como una tupla
for llave, valor in persona.items(): # items para llave valor
    print(f"Llave: {llave}, Valor:  {valor}")

# Obtener los valores
print(f"\nValores del diccionario:  ")
for valor in persona.values():
    print(f"- Valor: {valor}")

# Obtener las llaves
print(f"Impresion de las llaves del diccionario:")
for llave in persona.keys():
    print(f"- {llave}")
