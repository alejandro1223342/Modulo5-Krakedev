from auto import Auto

mi_auto = Auto("Toyota", "Corolla", 2022)
mi_auto.mostrar_informacion()
mi_auto.estado_auto()

mi_auto.actualizar_kilometraje(15000)
mi_auto.mostrar_informacion()
mi_auto.estado_auto()

mi_auto.realizar_viaje(60000)
mi_auto.mostrar_informacion()
mi_auto.estado_auto()

mi_auto.actualizar_kilometraje(10000)  #  kilometraje menor al actual
mi_auto.realizar_viaje(-500)           # kilómetros negativos


# crear un auto Toyota nuevo
auto1 = Auto.toyota_nuevo("Yaris")
auto1.mostrar_informacion()

# crear un auto usado
auto2 = Auto.crear_usado("Honda", "Civic", 2018, 75000)

# comparar kilometrajes
print("¿Tienen el mismo kilometraje?", Auto.mismo_kilometraje(auto1, auto2))

# Validar un kilometraje
print("¿Es válido el kilometraje -50?", Auto.kilometraje_valido(-50))
print("¿Es válido el kilometraje 5000?", Auto.kilometraje_valido(5000))