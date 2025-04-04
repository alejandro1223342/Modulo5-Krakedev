class Auto :
    def __init__(self, marca, modelo, año, kilometraje = 0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
    
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Kilometraje: {self.kilometraje}")
    
    def actualizar_kilometraje(self,kilometraje) :
        if kilometraje <= self.kilometraje:
            self.kilometraje = kilometraje
        else:
            print("No se puede reducir el kilometraje")

    def realizar_viaje(self, kilometros):
        if kilometros > 0:
            self.kilometraje += kilometros
        else:
            print("La cantidad de kilómetros debe ser positiva.")
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")

mi_auto = Auto("Toyota", "Corolla", 2022)
mi_auto.mostrar_informacion()
mi_auto.estado_auto()

mi_auto.realizar_viaje(15000)
mi_auto.mostrar_informacion()
mi_auto.estado_auto()

mi_auto.realizar_viaje(90000)
mi_auto.mostrar_informacion()
mi_auto.estado_auto()

mi_auto.realizar_viaje(-500)  # Intento inválido


        