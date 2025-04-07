from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass


class EmpleadoTiempoCompleto(Empleado):
    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.2)


class EmpleadoMedioTiempo(Empleado):
    def calcular_salario(self):
        return self.salario_base + (self.salario_base * 0.1)


# clase de Prueba
empleado1 = EmpleadoTiempoCompleto("Carlos", 1000)
empleado2 = EmpleadoMedioTiempo("Ana", 600)

print(f"{empleado1.nombre} - Salario Final: ${empleado1.calcular_salario()}")
print(f"{empleado2.nombre} - Salario Final: ${empleado2.calcular_salario()}")

# lista y polimorfismo
empleados = [empleado1, empleado2]
for emp in empleados:
    print(f"{emp.nombre} tiene un salario final de: ${emp.calcular_salario()}")
