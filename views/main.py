import tkinter as tk 
from  views.resources import BACKGROUND,ICON 

ventana = tk.Tk()
ventana.configure(background=BACKGROUND)
ventana.state("zoomed")


ventana.iconbitmap(ICON)
ventana.title("Classroom xd")


