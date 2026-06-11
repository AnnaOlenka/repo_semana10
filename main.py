from models import (
    Electronico,
    Libro
)

from utils.exceptions import (
    ValidationError,
    NotFoundError
)

productos = []


def agregar_producto():

    try:

        tipo = input(
            "\n1. Electrónico\n"
            "2. Libro\n"
            "Seleccione: "
        )

        nombre = input("Nombre: ")
        precio = float(
            input("Precio: ")
        )

        stock = int(
            input("Stock: ")
        )

        if tipo == "1":

            garantia = int(
                input(
                    "Garantía (meses): "
                )
            )

            producto = Electronico(
                nombre,
                precio,
                stock,
                garantia
            )

        elif tipo == "2":

            autor = input(
                "Autor: "
            )

            producto = Libro(
                nombre,
                precio,
                stock,
                autor
            )

        else:
            raise ValidationError(
                "Tipo inválido."
            )

        productos.append(producto)

    except ValidationError as e:
        print("ERROR:", e)

    except ValueError:
        print(
            "Debe ingresar valores numéricos."
        )

    else:
        print(
            "Producto agregado correctamente."
        )

    finally:
        print(
            "Operación finalizada."
        )


def listar_productos():

    if not productos:
        print("No hay productos.")
        return

    for i, p in enumerate(
            productos,
            start=1):
        print(f"{i}. {p}")


def buscar_producto():

    try:

        nombre = input(
            "Nombre a buscar: "
        )

        for producto in productos:
            if (
                producto.nombre.lower()
                ==
                nombre.lower()
            ):
                print(producto)
                return

        raise NotFoundError(
            "Producto no encontrado."
        )

    except NotFoundError as e:
        print("ERROR:", e)


def menu():

    while True:

        print("\n===== MENU =====")
        print("1. Agregar")
        print("2. Listar")
        print("3. Buscar")
        print("4. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_producto()

        elif opcion == "2":
            listar_productos()

        elif opcion == "3":
            buscar_producto()

        elif opcion == "4":
            print("Fin del programa.")
            break

        else:
            print(
                "Opción inválida."
            )


if __name__ == "__main__":
    menu()