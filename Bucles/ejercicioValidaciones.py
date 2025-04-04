datos = []
cantidad = int(input("¿Cuántos datos deseas ingresar?: "))

for i in range(cantidad):
    dato = input(f"Ingrese el dato {i+1}: ")
    
    # validar si es un número entero
    if dato.isnumeric():
        datos.append(int(dato))
    
    # validar si es un número decimal
    elif dato.replace('.', '', 1).isdigit():
        datos.append(float(dato))
    
    # validar si es un string sSolo letras sin números ni símbolos
    elif dato.isalpha():
        datos.append(dato)
    
    else:
        print(f"El dato '{dato}' no se considera válido y no se agregará a la lista.")
        
# resultado lista final
print(f"\nSu lista es: {datos}")
