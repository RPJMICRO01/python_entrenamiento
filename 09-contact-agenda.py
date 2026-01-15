print("*** Agenda de Contacos ***")

agenda = {

    "Carlos" : {
        "telefono" : "55667711",
        "email" : "carlos@mail.com",
        "direccion" : "Calle Principal"
    },
    "Maria": {
        "telefono" : "99887733",
        "email" : "maria@mail.com",
        "direccion" : "Avenida Central 456"
    },
    "Pedro": {
        "telefono" : "55139078",
        "email" : "pedro@mail.com",
        "direccion" : "Plaza Mayor 789"
    }
}
print(agenda)

# Acceder a la informacion de un contacto en especifico
print(f"""Informacion del contacto de Maria:
    Telefono: {agenda["Maria"]["telefono"]}
    Email: {agenda["Maria"]["email"]}
    Direcion: {agenda["Maria"]["direccion"]}
""")

# Agregar un nuevo contacto
agenda["Ana"] = {
    "telefono" : "55678392",
    "email" : "ana@mail.com",
    "direccion" : "Calle Salvador Diaz 321"
}

#
print(agenda)

# Eliminar un contacto existente
agenda.pop("Pedro")
print(agenda)

print("\nContactos en la Agenda")
for nombre, detalles in agenda.items():
    print(f"""Nombre : {nombre}
    Telefono: {detalles.get("telefono")}
    Email: {detalles.get("email")}
    Direccion: {detalles.get("direccion")}
""")
