from utils.validators import (
    validar_precio,
    validar_stock
)

class Producto:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError(
                "Nombre inválido"
            )
        self._nombre = valor

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor):
        validar_precio(valor)
        self._precio = valor

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        validar_stock(valor)
        self._stock = valor

    def calcular_precio_final(self):
        return self.precio

    def __str__(self):
        return (
            f"{self.nombre} | "
            f"S/ {self.calcular_precio_final():.2f}"
        )

    def __del__(self):
        if hasattr(self, '_nombre'):
            print(
                f"Producto {self._nombre} eliminado"
            )


