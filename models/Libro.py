from .Producto import Producto


class Libro(Producto):

    def __init__(self, nombre, precio, stock, autor):
        super().__init__(nombre, precio, stock)
        self.autor = autor

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        if not valor.strip():
            raise ValueError(
                "El autor no puede estar vacío."
            )
        self._autor = valor

    def calcular_precio_final(self):
        return self.precio * 1.04

    def __str__(self):
        return (
            f"[Libro] {self.nombre} | "
            f"S/ {self.calcular_precio_final():.2f} "
            f"(Autor: {self.autor})"
        )
