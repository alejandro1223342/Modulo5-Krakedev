
from laptop import Laptop
laptop_Pepito = Laptop("Lenovo", "i7", 32)
laptop_Maria = Laptop("Lenovo", "i7", 32,600)

print(Laptop.comparar_costo(laptop_Pepito,laptop_Maria))


for numero in range(1,1001) :
    asus_laptop = Laptop.asus_laptop(numero)
    #dict para ver lo que contiene
    print(asus_laptop.__dict__)
 


# print(laptop_Pepito.__dict__)
# print(laptop_Pepito.valor_final())
# print(laptop_Pepito.valor_descuento(10))