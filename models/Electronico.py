from .DescuentoMixin import DescuentoMixin
from .Producto import Producto


class Electronico(DescuentoMixin, Producto):

    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia = garantia

    @property
    def garantia(self):
        return self._garantia

    @garantia.setter
    def garantia(self, valor):
        if valor <= 0:
            raise ValueError(
                "La garantía debe ser mayor que cero."
            )
        self._garantia = valor

    def calcular_precio_final(self):
        return self.aplicar_descuento(self.precio, 10)

    def __str__(self):
        return (
            f"[Electrónico] {self.nombre} | "
            f"S/ {self.calcular_precio_final():.2f} "
            f"(Garantía: {self.garantia} meses)"
        )
