from libro import Libro

# clase de Prueba

# crear al menos tres libros con diferentes características
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", 96)
libro3 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)

# mostrar la información de cada libro
libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()

# verificar si alguno de los libros es "grande"
print("¿El libro 1 es grande?", Libro.es_grande(libro1.paginas))
print("¿El libro 2 es grande?", Libro.es_grande(libro2.paginas))
print("¿El libro 3 es grande?", Libro.es_grande(libro3.paginas))

# mostrar el total de libros creados
print("Total de libros creados:", Libro.total_libros())