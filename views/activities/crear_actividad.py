import tkinter as tk
from tkinter import messagebox as mb
from db.operations import crear_actividad
from views.resources import BACKGROUND, SECONDARY, TEXT, TITLES, PRIMARY

def mostrar_crear_actividad(w: tk.Tk):
    from views.activities.home import mostrar_home_actividades  # Asegúrate que esta vista exista

    for widget in w.winfo_children():
        widget.destroy()

    w.configure(bg=BACKGROUND)
    w.columnconfigure(0, weight=1)
    w.columnconfigure(1)
    w.columnconfigure(2, weight=1)

    for i in range(7):
        w.rowconfigure(i, pad=20)

    tk.Label(
        w,
        text="Formulario para registrar Actividades",fg=PRIMARY,font=TITLES,bg=BACKGROUND
    ).grid(column=0, row=0, columnspan=3, sticky="n")

    tk.Label(w, text="Título", fg=SECONDARY, font=TEXT, bg=BACKGROUND).grid(column=0, row=1, sticky="e")
    tk.Label(w, text="Descripción", fg=SECONDARY, font=TEXT, bg=BACKGROUND).grid(column=0, row=2, sticky="e")
    tk.Label(w, text="Fecha (dd/mm/yy)", fg=SECONDARY, font=TEXT, bg=BACKGROUND).grid(column=0, row=3, sticky="e")

    entry_titulo = tk.Entry(w, font=TEXT, relief="flat")
    entry_descripcion = tk.Entry(w, font=TEXT, relief="flat")
    entry_fecha = tk.Entry(w, font=TEXT, relief="flat")

    entry_titulo.grid(column=1, row=1, padx=20)
    entry_descripcion.grid(column=1, row=2, padx=20)
    entry_fecha.grid(column=1, row=3, padx=20)

    def enviar():
        data = {
            "titulo": entry_titulo.get(),
            "descripcion": entry_descripcion.get(),
            "fecha": entry_fecha.get()
        }
        import datetime
        try:
            datetime.datetime.strptime(data["fecha"], "%d/%m/%y")
        except ValueError:
            mb.showerror("Error", "Fecha inválida. Usa formato dd/mm/yy")
            return
        status, msg = crear_actividad(data)
        if not status:
            mb.showerror("Error", msg)
            return
        mb.showinfo("Éxito", "Actividad almacenada con éxito")

    tk.Button(w, command=enviar, text="Guardar", relief="flat", font=TEXT).grid(column=0, row=4, columnspan=3, sticky="n")
    tk.Button(w, command=lambda: mostrar_home_actividades(w), text="Regresar al inicio", relief="flat", font=TEXT).grid(column=0, row=5, columnspan=3, sticky="n", pady=20)

    w.mainloop()