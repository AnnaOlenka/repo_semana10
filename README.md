# Sistema de Gestión de Productos — Semana 09

## Estructura del proyecto

```
main.py
models/
    __init__.py
    producto.py      ← Producto, Electronico, Libro, DescuentoMixin
utils/
    __init__.py
    exceptions.py    ← ValidationError, NotFoundError
    validators.py    ← validar_precio, validar_stock, formatear_moneda
requirements.txt
```

---

## Diagrama de clases

```
         DescuentoMixin
         + aplicar_descuento(precio, porcentaje)
                 │
                 │ (herencia múltiple)
                 │
         Producto (clase base)
         - _nombre   : str
         - _precio   : float
         - _stock    : int
         + nombre    @property (setter valida no vacío)
         + precio    @property (setter valida > 0)
         + stock     @property (setter valida >= 0)
         + calcular_precio_final() → float
         + __str__() → str
         + __del__()
                 │
        ┌────────┴────────┐
        │                 │
   Electronico          Libro
   - _garantia : int    - _autor : str
   + garantia  @property (setter valida > 0)
               + autor    @property (setter valida no vacío)
   + calcular_precio_final()   + calcular_precio_final()
     → precio con 10% descuento  → precio * 1.04 (IGV)
   + __str__()                  + __str__()
```

---

## MRO aplicado

### Orden de resolución para `Electronico`

```python
Electronico(DescuentoMixin, Producto)
```

MRO (C3 Linearization):
```
Electronico → DescuentoMixin → Producto → object
```

Cuando `Electronico.__init__` llama a `super().__init__()`, Python sigue este
orden exacto. `DescuentoMixin` no define `__init__`, por lo que la cadena
llega correctamente a `Producto.__init__`.

### Por qué herencia y no composición

| Decisión | Razón |
|---|---|
| `Electronico` y `Libro` heredan de `Producto` | Son productos — relación "es un", no "tiene un" |
| `DescuentoMixin` como mixin | Agrega comportamiento de descuento sin estado propio; reutilizable en cualquier clase sin forzar una jerarquía rígida |

---

## Capturas de ejecución

### Caso exitoso — agregar y listar productos

```
===== MENU =====
1. Agregar
2. Listar
3. Buscar
4. Salir
Opción: 1

1. Electrónico
2. Libro
Seleccione: 1
Nombre: Laptop HP
Precio: 2500
Stock: 10
Garantía (meses): 12
Producto agregado correctamente.
Operación finalizada.

Opción: 2
1. [Electrónico] Laptop HP | S/ 2250.00 (Garantía: 12 meses)
```

### Excepción 1 — ValidationError (precio inválido)

```
Opción: 1

1. Electrónico
2. Libro
Seleccione: 1
Nombre: Mouse
Precio: -50
Stock: 10
Garantía (meses): 6
ERROR: El precio debe ser mayor que cero.
Operación finalizada.
```

> `ValidationError` capturada en el bloque `except`. El bloque `finally`
> ejecuta "Operación finalizada." sin importar el resultado.

### Excepción 2 — NotFoundError (producto no encontrado)

```
Opción: 3
Nombre a buscar: Tablet
ERROR: Producto no encontrado.
```

> `NotFoundError` lanzada cuando ningún producto coincide con el nombre buscado.

---

## Requisitos

```
python>=3.11
```
