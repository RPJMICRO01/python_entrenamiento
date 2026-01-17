# variable global
contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0

    # usarl la variable global
    global contador_global
    contador_global += 1

    contador_local += 1

    print(f"contador local: {contador_local}")
    print(f"contador global: {contador_global}\n")

incrementar_contador()
incrementar_contador()
incrementar_contador()
