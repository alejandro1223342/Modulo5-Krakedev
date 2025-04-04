pais = input("Ingrese el país (Ecuador, Colombia, Perú): ")
zona = input("Ingrese la zona (Urbana, Rural, Perimetral): ")
velocidad = int(input("Ingrese la velocidad actual (Km/h): "))

if pais == "Ecuador":
    if zona == "Urbana":
        if velocidad < 10:
            print("Velocidad demasiado baja. Mínimo permitido: 10 Km/h.")
        elif velocidad > 50:
            print("Velocidad demasiado alta. Máximo permitido: 50 Km/h.")
        else:
            print("Velocidad permitida.")
    elif zona == "Rural":
        if velocidad < 51:
            print("Velocidad demasiado baja. Mínimo permitido: 51 Km/h.")
        elif velocidad > 70:
            print("Velocidad demasiado alta. Máximo permitido: 70 Km/h.")
        else:
            print("Velocidad permitida.")
    elif zona == "Perimetral":
        if velocidad < 71:
            print("Velocidad demasiado baja. Mínimo permitido: 71 Km/h.")
        elif velocidad > 90:
            print("Velocidad demasiado alta. Máximo permitido: 90 Km/h.")
        else:
            print("Velocidad permitida.")

elif pais == "Colombia":
    if zona == "Urbana":
        if velocidad < 10:
            print("Velocidad demasiado baja. Mínimo permitido: 10 Km/h.")
        elif velocidad > 30:
            print("Velocidad demasiado alta. Máximo permitido: 30 Km/h.")
        else:
            print("Velocidad permitida.")
    elif zona == "Rural":
        if velocidad < 31:
            print("Velocidad demasiado baja. Mínimo permitido: 31 Km/h.")
        elif velocidad > 80:
            print("Velocidad demasiado alta. Máximo permitido: 80 Km/h.")
        else:
            print("Velocidad permitida.")
    elif zona == "Perimetral":
        if velocidad < 81:
            print("Velocidad demasiado baja. Mínimo permitido: 81 Km/h.")
        elif velocidad > 100:
            print("Velocidad demasiado alta. Máximo permitido: 100 Km/h.")
        else:
            print("Velocidad permitida.")

elif pais == "Perú":
    if zona == "Urbana":
        if velocidad < 10:
            print("Velocidad demasiado baja. Mínimo permitido: 10 Km/h.")
        elif velocidad > 40:
            print("Velocidad demasiado alta. Máximo permitido: 40 Km/h.")
        else:
            print("Velocidad permitida.")
    elif zona == "Rural":
        if velocidad < 41:
            print("Velocidad demasiado baja. Mínimo permitido: 41 Km/h.")
        elif velocidad > 60:
            print("Velocidad demasiado alta. Máximo permitido: 60 Km/h.")
        else:
            print("Velocidad permitida.")
    elif zona == "Perimetral":
        if velocidad < 61:
            print("Velocidad demasiado baja. Mínimo permitido: 61 Km/h.")
        elif velocidad > 120:
            print("Velocidad demasiado alta. Máximo permitido: 120 Km/h.")
        else:
            print("Velocidad permitida.")
