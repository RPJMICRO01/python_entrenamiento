print("systema de empleados")

nombre_empleados = input("ingrese su nombre:  ")

edad = int(input("ingrese su edad:   "))

salario_empleado = float(input("ingrese su salario:   "))

es_jefe_de_departamento = input("es jefe de departamento (Si o No)? ")

es_jefe_de_departamento = es_jefe_de_departamento.lower() == "si"


print("su nombre es", nombre_empleados)

print("su edad es", edad)

print("el salario del empleado es", salario_empleado)

print("es jefe de departamento", es_jefe_de_departamento)
