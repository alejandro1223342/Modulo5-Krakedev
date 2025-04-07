class Libro:
    cantidad_libros = 0  # Atributo de clase para contar los libros

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        Libro.cantidad_libros += 1

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Páginas: {self.paginas}")
        print("---------------")

    @staticmethod
    def es_grande(paginas):
        return paginas > 300

    @classmethod
    def total_libros(cls):
        return cls.cantidad_libros

