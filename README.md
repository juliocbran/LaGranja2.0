# Distribuidora de Huevos y Lacteos 'La Granja'

Sistema de gestion de recepcion, inventario y control de calidad.
Proyecto de Programacion Imperativa — Guia #01 (Python 3.9 + Tkinter).

**Integrantes:**
- Harry Ospina Mazo
- Julio Cesar Vidal Bran

## Descripcion

Aplicacion de escritorio que permite registrar los lotes de huevos y leche
que llegan a la distribuidora, visualizarlos en una tabla en tiempo real y
calcular consolidados (total del inventario, cubetas por tipo, lotes que
requieren refrigeracion especial). Toda la logica de procesamiento de datos
esta implementada con **funciones recursivas**, sin usar ciclos `for`/`while`.

## Estructura del proyecto

```

gui.py        ->  punto de entrada, arranca la aplicacion, 
                  interfaz grafica en Tkinter (formulario, tabla, resultados) 
                  nucleo de logica recursiva (calculo de totales, conteos, filtros)

README.md     -> este archivo

```

## Requisitos

- Python 3.9 o superior (incluye Tkinter en la instalacion estandar).
- Se requiere descargas comando (python -m pip install Pillow)

## Como ejecutar

Desde la carpeta del proyecto:

```bash
python gui.py
```

Se abrira la ventana de la aplicacion.

## Uso rapido

1. Completa **Tipo/Categoria**, **Cantidad** y **Precio unitario**.
2. Marca **Requiere Refrigeracion Especial** si aplica.
3. Presiona **Registrar Lote** para agregarlo a la tabla.
4. Presiona **Calcular Totales** para ver el valor total del inventario, la
   cantidad de lotes registrados y cuantos requieren refrigeracion.
5. Usa el campo **Consultar cubetas por tipo** para saber cuantas unidades
   hay registradas de un tipo especifico (ej. "Tipo AA").
6. Usa **Ver Solo Refrigerados** / **Ver Todos** para alternar el filtro
   de la tabla.
7. **Limpiar Campos** vacia el formulario para un nuevo registro.

## Funciones recursivas (GUI.py)

| Funcion | Caso base | Caso recursivo |
|---|---|---|
| `calcular_total_inventario(lista_lotes)` | Lista vacia -> retorna 0 | Subtotal del primer lote + resultado recursivo del resto de la lista |
| `contar_cubetas_por_tipo(lista_lotes, tipo_objetivo)` | Lista vacia -> retorna 0 | Suma la cantidad del primer lote si coincide el tipo (o 0 si no) + resultado recursivo del resto |
| `filtrar_refrigerados(lista_lotes)` | Lista vacia -> retorna lista vacia | Filtra el resto de la lista y antepone el primer lote solo si requiere refrigeracion |

Ademas se incluye `contar_lotes(lista_lotes)` como funcion auxiliar recursiva
para contar el total de lotes registrados.

No se utiliza ningun ciclo `for`/`while` dentro de `GUI.py`. Incluso el
llenado y limpieza de la tabla (Treeview) en `gui.py` se hace con funciones
auxiliares recursivas (`_poblar_treeview`, `_limpiar_treeview`).
