from informacion import agregar_nombre, agregar_edad, nombre_paciente, edad

n = int(input("¿Cuantos pacientes desea ingresar? "))

for _ in range(n):
    nombre = input("Ingrese el nombre completo del paciente: ")
    año_nacimiento = input("Ingrese el año de nacimiento del paciente: ")
    
    agregar_nombre(nombre)
    agregar_edad(año_nacimiento)

print("\nLista de nombres de los pacientes:")
print(nombre_paciente)

print("\nLista de edades de los pacientes:")
print(edad)

# determinar el paciente mayor y menor
mayor_edad = max(edad)
menor_edad = min(edad)

indice_mayor = edad.index(mayor_edad)
indice_menor = edad.index(menor_edad)

print(f"\nEl paciente mayor es: {nombre_paciente[indice_mayor]} con {mayor_edad} años.")
print(f"El paciente menor es: {nombre_paciente[indice_menor]} con {menor_edad} años.")
