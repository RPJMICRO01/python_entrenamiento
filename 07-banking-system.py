respuesta = input("desea continuar dentro del sistema (Si/No):   ")

per = respuesta.lower().strip() == "no"
#ejecuta esto si per es falso
if not per:
    print("seguir dentro del sistema")
else:
    print("salir del sistema")
