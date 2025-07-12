import tkinter as tk 
from views.resources import BACKGROUND

def show_table(w:tk.Tk,column, row,columspan=0,padx=0,pady=0):
    contenedor =tk.Frame(w)
    contenedor.grid (column= column,row=row, columnspan=columspan, padx=padx,pady=pady,sticky="news")

    canvas=tk.Canvas(contenedor)
    scrollbar=tk.Scrollbar(contenedor,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left",fill="both",expand=True)
    scrollbar.pack(side="right",fill="y")

    frame_scrollable = tk.Frame(canvas)
    canvas.create_window((0,0),window=frame_scrollable, anchor="nw")

    def on_configure():
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scrollable.bind("<Configure>", on_configure)
    canvas.configure(bg=BACKGROUND)
    return frame_scrollable