def imprimir_detalle_persona(**kwargs):
    print("\nValores recibidos: ")
    for llave, valor in kwargs.items():
        print(f"{llave}:{valor}")

# llamar a la funcion
imprimir_detalle_persona(nombre="Karla", edad=30, ciudad="Mexico")
imprimir_detalle_persona(nombre="Carlos", edad=28, ciudad="guadalajara",puesto="Gerente")
