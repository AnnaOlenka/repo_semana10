from models import Producto

class Libro(
    Producto
):

    def __init__(
            self,
            nombre,
            precio,
            stock,
            autor):

        super().__init__(
            nombre,
            precio,
            stock
        )

        self.autor = autor

    def calcular_precio_final(self):
        return self.precio * 1.04