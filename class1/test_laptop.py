
from laptop import Laptop
laptop_Pepito = Laptop("Lenovo", "i7", 32)
laptop_Maria = Laptop("Lenovo", "i7", 32,600)

print(Laptop.comparar_costo(laptop_Pepito,laptop_Maria))


# print(laptop_Pepito.__dict__)
# print(laptop_Pepito.valor_final())
# print(laptop_Pepito.valor_descuento(10))