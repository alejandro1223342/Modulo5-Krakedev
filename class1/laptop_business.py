import random
from laptop import Laptop  

class Laptop_Business(Laptop):
    def __init__(self, marca, procesador, memoria, almacenamiento, duracion_bateria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        self.almacenamiento = almacenamiento
        self.duracion_bateria = duracion_bateria

    def realizar_diagnostico_sistema(self):
        resultado_diagnostico = super().realizar_diagnostico_sistema()
        
        resultado_diagnostico["ALMACENAMIENTO"] = "OK" if self.almacenamiento >= 256 else "Ampliar almacenamiento"
        resultado_diagnostico["DURACIÓN DE BATERÍA"] = "Buena" if self.duracion_bateria >= 6 else "Revisar batería"
        
        conectividad = self.verificar_conectividad_red()
        resultado_diagnostico["CONECTIVIDAD DE RED"] = conectividad
        
        return resultado_diagnostico

    def verificar_conectividad_red(self):
        conectividad = {
            "Wi-Fi disponible": random.choice([True, False]),
            "Acceso a servidores empresariales": random.choice([True, False]),
            "Latencia aceptable": random.choice([True, False])
        }
        return conectividad
