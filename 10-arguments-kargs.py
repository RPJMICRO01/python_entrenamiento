print("*** Argumentos variables en forma de dict ***")

def superheroe_superpoderes(nombre, *args, **kwargs):
    print(f"Superheroe: {nombre} - {args} - Mas info: {kwargs}")

superheroe_superpoderes("spiderman", "Instinto Aracnido", edad=17, empresa="Marvel")
superheroe_superpoderes("Ironman","Armadura", "Playboy", edad=45)
superheroe_superpoderes("mi vecino", personalidad="Buena onda")
