from datetime import datetime

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
    
    # metodo de clase para crear un toyota nuevo del año actual
    @classmethod
    def toyota_nuevo(cls, modelo):
        año_actual = datetime.now().year
        return cls("Toyota", modelo, año_actual, 0)

    # metodo estatico para comparar kilometraje de dos autos
    @staticmethod
    def mismo_kilometraje(auto1, auto2):
        if auto1.kilometraje == auto2.kilometraje:
            return "Tienen el mismo kilometraje"
        else:
            return "No tienen el mismo kilometraje"


    # metodo de clase adicional crear un auto usado con parámetros
    @classmethod
    def crear_usado(cls, marca, modelo, año, kilometraje):
        return cls(marca, modelo, año, kilometraje)


    # metodo estático adicional validar si un kilometraje es válido (no negativo)
    @staticmethod
    def kilometraje_valido(kilometraje):
        if kilometraje >= 0:
            return "El kilometraje es válido."
        else:
            return "Error: El kilometraje no puede ser negativo."



        