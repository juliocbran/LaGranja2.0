import tkinter as tk
from tkinter import ttk  ,messagebox

from PIL import Image, ImageTk


lotes_registrados = []
#================================================================   
#================================================================   
#================================================================   
#================================================================   
#================================================================   
def calcular_total_inventario(lista_lotes):
    if not lista_lotes:
        return 0.0
    # Caso recursivo: subtotal del primer lote + total del resto
    costo_actual = lista_lotes[0]["cantidad"] * lista_lotes[0]["precio"]
    return costo_actual + calcular_total_inventario(lista_lotes[1:])


def contar_cubetas_por_tipo(lista_lotes, tipo_objetivo):
    if not lista_lotes:
        return 0
    # Caso recursivo: suma la cantidad si coincide el tipo
    coincidencia = lista_lotes[0]["cantidad"] if lista_lotes[0]["tipo"] == tipo_objetivo else 0
    return coincidencia + contar_cubetas_por_tipo(lista_lotes[1:], tipo_objetivo)

def filtrar_refrigerados(lista_lotes):
    if not lista_lotes:
        return []
    # Caso recursivo: construye lista nueva solo con refrigerados
    if lista_lotes[0]["refrigeracion"]:
        return [lista_lotes[0]] + filtrar_refrigerados(lista_lotes[1:])
    else:
        return filtrar_refrigerados(lista_lotes[1:])

#================================================================   
#================================================================   
#================================================================   
#================================================================   
#================================================================   
def actualizar_tabla(lista):
    # Limpiar filas existentes con un ciclo for común
    for item in tabla.get_children():
        tabla.delete(item)
    
    # Insertar los lotes en la tabla
    for lote in lista:
        subtotal = lote["cantidad"] * lote["precio"]
        refri_txt = "Sí" if lote["refrigeracion"] else "No"
        tabla.insert("", "end", values=(lote["tipo"], lote["cantidad"], f"${lote['precio']:.2f}", f"${subtotal:.2f}", refri_txt))


def limpiar_campos():
    C_P.delete(0, tk.END)          # Borra el texto de Cantidad
    PU.delete(0, tk.END)           # Borra el texto de Precio Unitario
    combo.current(0)              # Regresa el menú desplegable a la primera opción
    Refri.set(False)              # Desmarca la casilla de refrigeración
    cambiar_color_refri()


   

def registrar_lote():
    tipo = opcion_seleccionada.get()
    cant_txt = C_P.get().strip()
    precio_txt = PU.get().strip()
    refri = Refri.get()

    # Validaciones básicas
    if not cant_txt or not precio_txt:
        messagebox.showerror("Error de Datos", "Por favor ingresa la cantidad y el precio.")
        return

    try:
        cant = int(cant_txt)
        precio = float(precio_txt)
        if cant <= 0 or precio <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error de Datos", "La cantidad y el precio deben ser números mayores a 0.")
        return

    # Guardar en la estructura de datos
    nuevo_lote = {
        "tipo": tipo,
        "cantidad": cant,
        "precio": precio,
        "refrigeracion": refri
    }
    lotes_registrados.append(nuevo_lote)

    # Actualizar la tabla visual
    actualizar_tabla(lotes_registrados)

    # Limpiar campos de entrada
    C_P.delete(0, tk.END)
    PU.delete(0, tk.END)
    Refri.set(False)
    cambiar_color_refri()

def ejecutar_calculo_totales():
    # Llama a la función recursiva requerida en la guía

    global lotes_registrados
    total = calcular_total_inventario(lotes_registrados)
    messagebox.showinfo("Consolidado Inventario", f"El valor total del inventario acumulado es:${total}")

def ejecutar_conteo_por_tipo():
    global lotes_registrados
    tipo_seleccionado = opcion_seleccionada.get()
    total_cubetas = contar_cubetas_por_tipo(lotes_registrados, tipo_seleccionado)
    messagebox.showinfo("Conteo por Tipo", f"Total de cubetas acumuladas para '{tipo_seleccionado}':{total_cubetas} unidades")

def filtrar_tabla_refrigerados():
    # Llama a la función recursiva requerida en la guía
    global lotes_registrados
    lotes_filtrados = filtrar_refrigerados(lotes_registrados)
    actualizar_tabla(lotes_filtrados)

def mostrar_todos_los_lotes():
    actualizar_tabla(lotes_registrados)




#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

window=tk.Tk()
window.title("La Granja-Recepcion e Inventario")
window.attributes(fullscreen=False)
ancho_pantalla = window.winfo_screenwidth()
alto_pantalla = window.winfo_screenheight()
#"{ancho_pantalla}x{alto_pantalla}"

minancho=int(ancho_pantalla*0.7)
minalto=int(alto_pantalla*0.8)
window.resizable(True, True)

window.minsize(minancho, minalto)
window.geometry(f"{minancho}x{minalto}")
window.configure(bg="#F5F5DC")
color_fondo="#F5F5DC"
color_texto="black"

estilo_texto= {
    "bg": "#A16D3F",             # Color de fondo del botón
    "fg": "#F5F5DC",               # Color de las letras
    "font": ("Impact ", 15),
    "bd": 3,                     # Borde
    "relief": "raised",           # Estilo 3D suave
}
estilo_boton = {
    "bg": "#8B340B",             # Color de fondo del botón
    "fg": "#F5F5DC",               # Color de las letras
    "activebackground": "#e2bf74",# Color al hacer clic
    "activeforeground": "white", # Color de letras al hacer clic
    "font": ("Impact ", 15, "bold"),
    "bd": 3,                     # Borde
    "relief": "raised",           # Estilo 3D suave
}
estilo_input= {
    "bg": "#A16D3F",             # Color de fondo del botón
    "fg": "#F5F5DC",              # Color de las letras al hacer clic
    "font": ("Impact ", 15, "bold"),
    "bd": 3,                     # Borde
    "relief": "raised",           # Estilo 3D suave
}




##=======================================
#ESTE ES EL CUADRO EN EL QUE ESTAN LOS INPUTS Y BOTONES PARA INGRESAR LA INFO
frame_Par = tk.LabelFrame(
    window,bg=color_fondo
,fg=color_texto,text="LA GRANJA",
    font=("Impact ", 15, "bold"),  #negrilla y letra
    bd=2, #grosor del contorno
    relief="solid" # TIPO DE CONTORNO
)

frame_Par.pack(fill="x", padx=10, pady=6)

frame_Formulario = tk.Frame(frame_Par, bg=color_fondo)
frame_Formulario.pack(side="left", fill="both", expand=True, padx=10)

frame_Logo = tk.Frame(frame_Par, bg=color_fondo)
frame_Logo.pack(side="right",fill="both", padx=10, pady=5)
#===============================================================
#===============================================================
imagen = Image.open("logo.png")
anchoLogo = 300

imagen_pequena = imagen.resize((anchoLogo, 200))
logo = ImageTk.PhotoImage(imagen_pequena)
etiqueta_logo = tk.Label(frame_Logo, image=logo,bg=color_fondo, bd=1)
etiqueta_logo.image = logo  # Referencia para que no se borre

etiqueta_logo.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="e")
#===============================================================
##=======================================
#ESTE ES EL MENSAJE DEL "TIPO"
tk.Label(
    frame_Formulario,
    text="Tipo / Producto:",
    **estilo_texto,
    
).grid(row=0, column=0, sticky="w", padx=10, pady=25)

##=======================================
#ESTE ES EL MENSAJE DE LA CANTIDAD
tk.Label(
    frame_Formulario,
    text="Cantidad (P/C):",
    **estilo_texto,
    
).grid(row=3, column=0, sticky="w", padx=10, pady=25)


#=======================================
#ESTE ES COMO EL INGRESO PERO DE CANTIDAD
C_P=tk.Entry(
    frame_Formulario,
    **estilo_input,
)
C_P.grid(row=3, column=1, sticky="w", padx=10, pady=25)

tk.Label(
    frame_Formulario,
    text="Precio Unitario:",
    **estilo_texto,
    
).grid(row=2, column=0, sticky="w", padx=10, pady=25)
#PRECIO UNITARIO
PU=tk.Entry(
    frame_Formulario,
    **estilo_input,
)
PU.grid(row=2, column=1, sticky="w", padx=10, pady=25)
#=======================================
tk.Label(
    frame_Formulario,
    text="Refrigeración Especial:",
    **estilo_texto,
    
).grid(row=0, column=3, sticky="w", padx=20, pady=25)

#===================================================================
opciones = ["A", "AA", "AAA","Yema Doble","Leche fresca"]
#NO SE PUEDE USAR BG O BF PARA ESTE DESPLEGABLE ENTONCES HACEMOS LO SIGUIENTE
style = ttk.Style()
style.theme_use('clam')
style.configure("Custom.TCombobox",
    fieldbackground=("#A16D3F"
),  # Fondo del campo de texto cerrado
    background=("#A16D3F"
),       # Fondo del botón de la flecha
    foreground= "#F5F5DC" ,     # Color del texto
    selectbackground=("#A16D3F"
), # Fondo al seleccionar el texto
    selectforeground=("black"
), # Color del texto al seleccionar
    bordercolor=("black"),      # Color del borde
    arrowcolor=color_texto        # Color de la flechita
)

style.map("Custom.TCombobox",
    fieldbackground=[('readonly',"#A16D3F"
)],
    selectbackground=[('readonly', "#A16D3F"
)],  # Quita el fondo azul de la selección
    selectforeground=[('readonly',"#F5F5DC")],  # Mantiene las letras claras
    background=[('readonly', "#A16D3F"
)],
    foreground=[('readonly', "#F5F5DC")]
)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++
opcion_seleccionada = tk.StringVar()
combo = ttk.Combobox(
    frame_Formulario,
    
    textvariable=opcion_seleccionada,
    values=opciones,
    font=("Impact ", 15, "bold"),
    style="Custom.TCombobox",
    state="readonly"
)
combo.current(0)
combo.grid(row=0,column=1,padx=10, pady=10)




#=======================================
#ESTO TAMBIEN ES DEL CHECK
Refri = tk.BooleanVar(value=False)
def cambiar_color_refri():
    if Refri.get():
        cb_Refri.config(bg="#44be96", selectcolor="#44be96")
    else:
        cb_Refri.config(bg="#A16D3F", selectcolor="#A16D3F")


#ESTE ES EL DE EL CHECK
cb_Refri = tk.Checkbutton(
    frame_Formulario,
    text="Check",
    variable=Refri,
    bg="#A16D3F",
    fg=color_texto,
    selectcolor="#CC874B",
    activebackground="grey",
    activeforeground=color_texto,
    command=cambiar_color_refri,
    bd=3,
    relief="raised",
    
    font=("Impact ", 11, "bold"),
)

cb_Refri.grid(row=0,column=4,sticky="w",padx=1,pady=25)

#BOTON DENTRO DE LOS INPUT , command=registrar_lote
tk.Button(frame_Formulario, text="Registrar Lote",command=registrar_lote,**estilo_boton).grid(column=3,row=2,sticky="w",padx=20,pady=25)
tk.Button(frame_Formulario, text="Limpiar Campos", command=limpiar_campos,**estilo_boton).grid(column=3, row=3, padx=20, pady=25,sticky="w")

#==============================================================0
frame_Botones= tk.Frame(
    window,                    
    bg=color_fondo
,


)
#BOTONES DE OPCIONES ABAJO ORGANIZAR CON LOGICA
frame_Botones.pack(fill="x",padx=10,pady=6)
#command=ejecutar_calculo_totales
tk.Button(frame_Botones, text="Calcular Totales",command=ejecutar_calculo_totales,**estilo_boton).pack(side="left", padx=15)
#command=filtrar_tabla_refrigerados
tk.Button(frame_Botones, text="Ver Solo Refrigerados",command=filtrar_tabla_refrigerados,**estilo_boton).pack(side="left", padx=15)
#command=mostrar_todos_los_lotes
tk.Button(frame_Botones, text="Ver Todos",command=mostrar_todos_los_lotes,**estilo_boton).pack(side="left", padx=15)

tk.Button(frame_Botones, text="Contar por Tipo", command=ejecutar_conteo_por_tipo, **estilo_boton).pack(side="left", padx=5)


#TABLAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//JULIO, LEER Y COMPLETAR O PERSONALIZAR SI PUEDES
frame_Tabla = tk.Frame(window, bg=color_fondo)

frame_Tabla.pack(fill="both", expand=True, padx=25, pady=10)

columnas = ("tipo", "cantidad", "precio", "subtotal", "refrigeracion")

COLOR_FONDO_TABLA = "#F5F5DC"     # Fondo de las filas (blanco)
COLOR_TEXTO_TABLA = "#A16D3F"       # Texto de las filas (negro)
COLOR_ENCABEZADO_BG = "#A16D3F"     # Fondo del encabezado (igual al botón)
COLOR_ENCABEZADO_FG = "#F5F5DC"    # Texto del encabezado (blanco)
COLOR_SELECCION_BG = "#ccb583"
style.configure("Custom.Treeview",
    background=COLOR_FONDO_TABLA,
    foreground=COLOR_TEXTO_TABLA,
    fieldbackground=COLOR_FONDO_TABLA,
    rowheight=20,
    font=("Impact ", 16)
)

style.map("Custom.Treeview",
    background=[('selected', COLOR_SELECCION_BG)],
    foreground=[('selected', 'white')]
)

# Estilo para los Encabezados (Títulos de las columnas)
style.configure("Custom.Treeview.Heading",
    background=COLOR_ENCABEZADO_BG,
    foreground=COLOR_ENCABEZADO_FG,
    font=("Impact ", 16, "bold"),
    relief="flat"
)

style.map("Custom.Treeview.Heading",
    background=[('active', COLOR_ENCABEZADO_BG)]
)

tabla = ttk.Treeview(frame_Tabla, columns=columnas, show="headings",style="Custom.Treeview")

tabla.heading("tipo", text="Tipo / Producto")
tabla.heading("cantidad", text="Cantidad")
tabla.heading("precio", text="Precio Unitario ($)")
tabla.heading("subtotal", text="Subtotal ($)")
tabla.heading("refrigeracion", text="Refrigeración Especial")

tabla.column("tipo", anchor="center",width=100)
tabla.column("cantidad", anchor="center", width=100)
tabla.column("precio", anchor="center", width=120)
tabla.column("subtotal", anchor="center", width=120)
tabla.column("refrigeracion", anchor="center", width=140)

tabla.pack(fill="both", expand=True)
#hay que hace rla cuestion de actualizar lista y eso

def actualizar_tabla(lista):
    # PASO 1: Obtener todas las filas viejas que están dibujadas en la tabla
    filas_actuales = tabla.get_children()
    
    # PASO 2: Borrar fila por fila usando un ciclo imperativo tradicional
    i = 0
    while i < len(filas_actuales):
        fila_id = filas_actuales[i]
        tabla.delete(fila_id)  # Borra la fila de la pantalla
        i = i + 1

    # PASO 3: Insertar los datos nuevos uno por uno
    for lote in lista:
        # Extraemos los datos de nuestro diccionario de forma directa
        tipo_prod = lote["tipo"]
        cant_prod = lote["cantidad"]
        prec_prod = lote["precio"]
        
        # Calculamos el subtotal
        subtotal_prod = cant_prod * prec_prod
        
        # Convertimos el True/False a un texto sencillo con un 'if' clásico
        if lote["refrigeracion"] == True:
            texto_refri = "Sí"
        else:
            texto_refri = "No"

        # Preparamos la tupla de datos
        datos_fila = (tipo_prod, cant_prod, f"${prec_prod:.2f}", f"${subtotal_prod:.2f}", texto_refri)

        # Insertamos la fila en la tabla
        tabla.insert("", "end", values=datos_fila)

window.mainloop()