
from laptop import Laptop
from laptop_gaming import Laptop_Gaming
from laptop_business import Laptop_Business

def imprimir_informe(laptop):
    informe =  laptop.realizar_informe_usi()
    for clave,valor in informe.items():
        print(f"{clave} : {valor}")
    print("\n")


laptop_Pepito = Laptop("Lenovo", "i7", 32)
laptop_Maria = Laptop("Lenovo", "i7", 32,600)
print("PEPITO :")
imprimir_informe(laptop_Pepito)





# print(Laptop.comparar_costo(laptop_Pepito,laptop_Maria))


# for numero in range(1,1001) :
#     asus_laptop = Laptop.asus_laptop(numero)
#     #dict para ver lo que contiene
#     print(asus_laptop.__dict__)
 

laptop_juanito = Laptop_Gaming("MSI", "I7", 4,"RTX")
print("JUANITO :")
imprimir_informe(laptop_juanito)
# print(laptop_juanito.realizar_diagnostico_sistema())

# laptop_oficina = Laptop_Business("HP", "i5", 16, 512, 8)
# print(laptop_oficina.realizar_diagnostico_sistema())

# print(laptop_Pepito.__dict__)
# print(laptop_Pepito.valor_final())
# print(laptop_Pepito.valor_descuento(10))

