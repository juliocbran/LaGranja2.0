# Distribuidora de Huevos y Lacteos 'La Granja'

Sistema de gestion de recepcion, inventario y control de calidad.
Proyecto de Programacion Imperativa — Guia #01 (Python 3.9+ + Tkinter).

Integrantes:
- Harry Ospina Mazo
- Julio Cesar Vidal Bran

----------------------------------------------------------------------

DESCRIPCION:
Aplicacion de escritorio para la recepcion y control de inventario de
lotes de productos agricolas (huevos y leche). La interfaz grafica permite
registrar lotes, visualizarlos dinamicamente en una tabla con estilos
personalizados y calcular consolidados.

Todo el procesamiento de datos esta integrado en un unico script utilizando
funciones puramente recursivas, eliminando el uso de ciclos imperativos
(for / while) para las operaciones del negocio.

----------------------------------------------------------------------

ESTRUCTURA DEL PROYECTO:

LAGRANJA2.0/
├── GUI.py           -> Punto de entrada principal. Contiene la interfaz (Tkinter), captura de eventos y funciones recursivas.
├── README.md        -> Documentacion general del proyecto.
├── LICENSE          -> Licencia del proyecto.
├── logo.png         -> Logo principal mostrado en la interfaz.
├── logo (2).png     -> Recurso grafico de imagen.
├── -logo.png        -> Recurso grafico de imagen.
└── Screenshot_1.png -> Captura de pantalla del sistema.

----------------------------------------------------------------------

REQUISITOS E INSTALACION:

- Python 3.9 o superior (incluye Tkinter en la instalacion estandar).
- Pillow (PIL) para la manipulacion y renderizado de imagenes.

Comando de instalacion:
python -m pip install Pillow

----------------------------------------------------------------------

COMO EJECUTAR:

Desde la terminal en la raiz de la carpeta LAGRANJA2.0:
python GUI.py

----------------------------------------------------------------------

USO RAPIDO DE LA APLICACION:

1. Seleccionar Producto: Elige una categoria en el desplegable (A, AA, AAA, Yema Doble, Leche fresca).
2. Ingresar Datos: Completa los campos de Precio Unitario y Cantidad (P/C).
3. Refrigeracion: Marca la casilla Refrigeracion Especial si el lote lo requiere (el boton cambia dinamicamente a color verde).
4. Registrar Lote: Presiona Registrar Lote para guardar y mostrar la entrada en la tabla.
5. Consultar Totales: Usa Calcular Totales para ver el valor monetario acumulado del inventario.
6. Filtrar por Tipo: Selecciona un tipo de producto y presiona Contar por Tipo para conocer las unidades acumuladas.
7. Filtrar Tabla: Alterna entre Ver Solo Refrigerados y Ver Todos para filtrar los registros visibles.
8. Limpiar Campos: Restablece los campos de texto e interactivos para un nuevo registro.

----------------------------------------------------------------------

FUNCIONES RECURSIVAS (GUI.py):

- calcular_total_inventario(lista_lotes):
  Caso Base: Lista vacia [] -> retorna 0.0
  Caso Recursivo: Multiplica cantidad * precio del primer lote + llamada recursiva sobre lista_lotes[1:]

- contar_cubetas_por_tipo(lista_lotes, tipo_objetivo):
  Caso Base: Lista vacia [] -> retorna 0
  Caso Recursivo: Suma la cantidad del lote si coincide el tipo + llamada recursiva sobre lista_lotes[1:]

- filtrar_refrigerados(lista_lotes):
  Caso Base: Lista vacia [] -> retorna []
  Caso Recursivo: Evalua si el primer lote es refrigerado y lo concatena con el resultado de lista_lotes[1:]

----------------------------------------------------------------------

REGLAS DE NEGOCIO Y ESTILOS:

- Validacion de Entradas: Control de excepciones (try/except) para impedir el registro de campos vacios, valores no numericos o montos menores o iguales a cero.
- Dinamismo en Controles: La casilla de verificacion cambia de fondo entre #A16D3F (por defecto) y #44be96 (activo) mediante cambiar_color_refri().
- Tema Visual Rustico: Paleta de colores (#F5F5DC, #A16D3F, #8B340B), fuente Impact y personalizacion con ttk.Style para mantener la identidad visual de la marca.