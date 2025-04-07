class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"{self.marca} {self.modelo}, Año: {self.anio}"


class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo  

    def descripcion(self):
        return f"[AUTO] {super().descripcion()} - Tipo: {self.tipo}"


class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo  

    def descripcion(self):
        return f"[MOTO] {super().descripcion()} - Tipo: {self.tipo}"


# clase de Prueba
auto1 = Auto("Toyota", "Corolla", 2022, "Sedan")
moto1 = Moto("Yamaha", "R3", 2021, "Deportiva")

# mostrar la descripción
print(auto1.descripcion())
print(moto1.descripcion())

# lista de vehículos
vehiculos = [auto1, moto1, Auto("Ford", "Mustang", 2023, "Deportivo")]

# usar polimorfismo
for vehiculo in vehiculos:
    print(vehiculo.descripcion())
