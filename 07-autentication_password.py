user = "jua"
password = 123

user_v = input("ingrese el user:  ")
password_v = int(input("ingrese la password:  "))

if user == user_v and password == password_v:
    print("Bienvenido al sistema")
elif user == user_v:
    print("password invalido")
elif password == password_v:
    print("usuario invalido")
else:
    print("usuario y password invalidos")
