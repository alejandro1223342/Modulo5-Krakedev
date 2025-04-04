#Listas
planetas = ["Mercurio","Venus","Tierra","Marte","Jupiter","Saturno","Urano","Neptuno", 5 ,4.5, True]

#print(planetas[-3])
#Si le dejo todo vacio imprime toda las lista
#print(planetas[2: ])

#print(len(planetas))
#print(planetas[8])

#TRABAJAR CON UNA LISTA DE NUMEROS

gravedad_en_planetas = [0.378, 0.907, 1 , 0.377,2.36,0.916, 0.889, 1.12]
peso_bus = 124054 #Newtons, en la tierra

print(f"En la Tierra, un autobus de dos pisos pesa {peso_bus} N")

print(f"En Mercurio, un autobus de dos pisos pesa {peso_bus * gravedad_en_planetas[0]} N")


print(f"Lo mas Liviano que seria un autobus en el sistema solar es {peso_bus * min(gravedad_en_planetas)} N")
print(f"Lo mas Pesado que seria un autobus en el sistema solar es {peso_bus * max(gravedad_en_planetas)} N")