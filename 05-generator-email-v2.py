# variables
nombre = input("ingrese su nombre:  ")
apellido = input("ingrese su apellido:  ")
nombre_empresa = input("ingrese el nombre de la empresa:  ")
extension_del_dominio = ".com.mx"

#todo a minusculas
nombre_minusculas = nombre.lower()
apellido_minusculas = apellido.lower()
nombre_empresa_minuscula = nombre_empresa.lower()

#vamos a hacer los remplazos necesarios
nombre_usuario = nombre_minusculas.replace(" " , ".")
apellido_usuario = apellido.replace(" ", ".")
nombre_trabajo = nombre_empresa_minuscula.replace(" " , "")

print("*** Generador email ***")
print("nombre de usuario:  ", nombre)
print("apellido de usuario:  ", apellido)
print("nombre usuario normalizado:  ", nombre_usuario + "\n")

print("nombre de empresa:  ", nombre_empresa)
print("extension del dominio:  ", extension_del_dominio)
print("dominio personalizado:  " "@" + nombre_trabajo + extension_del_dominio + "\n")


print("Email generado final: " , nombre_usuario + "." + apellido_usuario +"@"+nombre_trabajo + extension_del_dominio)

