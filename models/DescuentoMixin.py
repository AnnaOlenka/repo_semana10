class DescuentoMixin:

    def aplicar_descuento(
            self,
            precio,
            porcentaje):
        return precio * (
            1 - porcentaje / 100
        )