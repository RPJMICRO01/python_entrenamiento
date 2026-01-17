def imprimi(nombre,apellido=None,edad=0):
    print(f"Persona: nombre {nombre}, apellido {apellido}, edad {edad}")

# Primero llamamos la funcion pasamos los argumentos de manera posicional
imprimi("Ricardo","Quintana",32)
# aqui se pueede intercambiar el orden de los argumentos
imprimi(nombre="Ricardo",edad=21,apellido="Quintana")
# aqui se pueden dejar algunos valores por default
imprimi(nombre="Ricardo")
