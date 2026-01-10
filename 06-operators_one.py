x,y=5,10

print(f"x = {x}  . y =  {y}")

x,y=y,x


print(f"x = {x}  . y =  {y}")

nombre, apellido = input("ingres tu nombre y apellido separado por una coma:  ").split(',')
print(f"Nombre {nombre.strip()} apellido {apellido.strip()}")
