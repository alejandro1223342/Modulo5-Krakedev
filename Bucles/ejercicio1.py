lista = [1,2,3,4,5,"Anthony", "Pedro",1,2,3,5,6,6,"Anthony"]

elemento = "Anthony"

for i in lista:
    #print(i, end = (", "))
    if elemento == i:
        print(f"El elemento {elemento} esta dentro de la lista")