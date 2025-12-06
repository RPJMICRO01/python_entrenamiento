#variables
nombre = "Ubaldo Acosta Soto"
nombre_empresa = "Global Mentoring"
extension_del_dominio = ".com.mx"

#todo a minusculas
nombre_minusculas = nombre.lower()
nombre_empresa_minuscula = nombre_empresa.lower()

#vamos a hacer los remplazos necesarios
nombre_usuario = nombre_minusculas.replace(" " , ".")
nombre_trabajo = nombre_empresa_minuscula.replace(" " , "")

print("*** Generador email ***")
print("nombre de usuario:  ", nombre)
print("nombre usuario normalizado:  ", nombre_usuario + "\n")

print("nombre de empresa:  ", nombre_empresa)
print("extension del dominio:  ", extension_del_dominio)
print("dominio personalizado:  " "@" + nombre_trabajo + extension_del_dominio + "\n")


print("Email generado final: " , nombre_usuario+"@"+nombre_trabajo+extension_del_dominio)
