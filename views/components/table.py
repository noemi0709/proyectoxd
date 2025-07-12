import tkinter as tk
from views.resources import BACKGROUND

def show_table(w: tk.Tk, column, row, columnspan=0, padx=0, pady=0):
    contenedor = tk.Frame(w, bg=BACKGROUND)
    contenedor.grid(column=column, row=row, columnspan=columnspan, padx=padx, pady=pady, sticky="news")

    canvas = tk.Canvas(contenedor, bg=BACKGROUND, highlightthickness=0)
    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    frame_scrollable = tk.Frame(canvas, bg=BACKGROUND)
    canvas.create_window((0, 0), window=frame_scrollable, anchor="nw")

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scrollable.bind("<Configure>", on_configure)

    return frame_scrollable
