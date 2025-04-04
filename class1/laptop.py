class Laptop :
    def __init__(self,marca,procesador,memoria,costo = 500, impuesto = 10):
        self.marca = marca
        self.procesador = procesador
        self.memoria = memoria
        self.costo = costo
        self.impuesto = impuesto

    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo * descuento)/100

laptop_Pepito = Laptop("Lenovo", "i7", 32)

print(laptop_Pepito.__dict__)
print(laptop_Pepito.valor_final())
print(laptop_Pepito.valor_descuento(10))

