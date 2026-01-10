original_name = "juan"
original_password = int("123")


name = input("ingrese su name:   ")
password = int(input("ingrese su contraseña:   "))

conflict = original_name == name and original_password == password

print("\n",conflict)
