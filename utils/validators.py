from utils.exceptions import ValidationError


def validar_precio(precio):
    if precio <= 0:
        raise ValidationError(
            "El precio debe ser mayor que cero."
        )


def validar_stock(stock):
    if stock < 0:
        raise ValidationError(
            "El stock no puede ser negativo."
        )