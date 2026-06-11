from models import DescuentoMixin
from models import Producto

class Electronico(
    DescuentoMixin,
    Producto
):

    def __init__(
            self,
            nombre,
            precio,
            stock,
            garantia):

        super().__init__(
            nombre,
            precio,
            stock
        )

        self.garantia = garantia

    def calcular_precio_final(self):
        return self.aplicar_descuento(
            self.precio,
            10
        )