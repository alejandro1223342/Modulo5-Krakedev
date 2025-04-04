from datetime import datetime

nombre_paciente = []
edad = []

año_actual = datetime.now().year

def agregar_nombre(nombre):
    nombre_paciente.append(nombre)

def agregar_edad(año_nacimiento):
    edad_actual = año_actual - int(año_nacimiento)
    edad.append(edad_actual)
