personas = [
    {
        "nombre" : "Regina",
        "apellido" : "Flores",
        "edad" : 21
    },
    {
        "nombre" : "Alejandro",
        "apellido" : "Reyes",
        "edad" : 32
    }
]

print(personas)

# Acceder a un diccionario desde una lista
print(f"""Nombre: {personas[0].get("nombre")},
      Apellido: {personas[0].get("apellido")},
      Edad: {personas[0].get("edad")}
""")
print()

for contador, persona in enumerate(personas):
    print(f"{contador} - Persona: {persona}")
