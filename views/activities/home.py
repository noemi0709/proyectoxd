from tkinter import messagebox as mb, Tk, Label, Button
from views.resources import BACKGROUND, PRIMARY, SECONDARY, TITLES, TEXT, LOGO
from PIL import Image, ImageTk
from db.operations import obtener_actividades, eliminar_actividad, actualizar_actividad
from views.activities.crear_actividad import mostrar_crear_actividad
from views.components.table import show_table


def mostrar_home_actividades(w: Tk):
    def delete_actividad(act_id):
        res = mb.askyesno("¿Seguro que deseas eliminar esta actividad?")
        if res:
            eliminar_actividad(act_id)
            actividades = obtener_actividades()
            table_actividades(actividades)

    def update_actividad(act_id, actividad):
        # TODO: Implementar función para editar una actividad
        pass

    def table_actividades(actividades):
        table = show_table(w, 1, 3, columnspan=4, padx=10, pady=10)

        columnas = ["Título", "Descripción", "Fecha", "Fecha de registro", "Opciones"]
        for i, columna in enumerate(columnas):
            table.columnconfigure(i, weight=1)
            Label(table, text=columna, font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid").grid(column=i, row=0, sticky="news")

        for i, actividad in enumerate(actividades, 1):
            Label(table, text=actividad[1], font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid").grid(column=0, row=i, sticky="news")
            Label(table, text=actividad[2], font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid").grid(column=1, row=i, sticky="news")
            Label(table, text=actividad[3], font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid").grid(column=2, row=i, sticky="news")
            Label(table, text=actividad[4].strftime("%d-%m-%Y"), font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="solid").grid(column=3, row=i, sticky="news")

            # Botones de acción
            Button(table, text="Eliminar", font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="raised",
                   command=lambda id=actividad[0]: delete_actividad(id)).grid(column=4, row=i, sticky="e")
            Button(table, text="Editar", font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="raised",
                   command=lambda id=actividad[0], a=actividad: update_actividad(id, a)).grid(column=4, row=i, sticky="w")

    # Limpiar pantalla
    for widget in w.winfo_children():
        widget.destroy()

    # Configurar filas y columnas
    for i in range(6):
        w.rowconfigure(i, weight=1)
        w.columnconfigure(i, weight=1)

    # Logo
    image_pil = Image.open(LOGO)
    resized_image = image_pil.resize((100, 100))
    photo = ImageTk.PhotoImage(resized_image)
    w.photo = photo
    Label(w, image=photo, bg=BACKGROUND).grid(column=0, row=0, columnspan=6, sticky="news")

    # Navbar (fila 1)
    botones = ["Servicios", "Prendas", "Actividades", "Usuarios"]
    for index, label in enumerate(botones, start=1):
        Button(w, text=label, font=TEXT, bg=BACKGROUND, relief="raised").grid(column=index, row=1, sticky="we")

    # Título y botón de alta
    Label(w, text="Actividades", font=TITLES, bg=BACKGROUND).grid(column=0, row=2, columnspan=6, sticky="n")
    Button(w, text="Crear actividad", font=TEXT, bg=PRIMARY, fg=SECONDARY, relief="groove",
           command=lambda: mostrar_crear_actividad(w)).grid(column=4, sticky="n", row=2, padx=10)

    # Tabla
    actividades = obtener_actividades()
    table_actividades(actividades)

    w.mainloop()
