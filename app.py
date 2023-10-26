import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
palabras_reservadas=["Claves", "Registros","=","[","]",]
def cargar_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archivo bizdata", "*.bizdata")])
    

def analizar_archivo():
    
    pass

def generar_reporte(tipo_reporte):
    
    pass

root = tk.Tk()
root.title("Proyecto 2 - BIZDATA")
fuente=tkFont.Font(family='Helvetica', size=14)
contenedor_superior = tk.Frame(root, padx=15,pady=15,bg='#283747')
contenedor_superior.pack(side=tk.TOP, fill=tk.X)
nombre_proyecto = tk.Label(contenedor_superior, text="Proyecto 2 - BIZDATA",font=fuente,bg='#283747', fg="white")
nombre_proyecto.pack(side=tk.LEFT)
btn_abrir = tk.Button(contenedor_superior, text="Cargar archivo", command=cargar_archivo,width=20,font=fuente,bg='#F1C40F', fg="white")
btn_abrir.pack(side=tk.RIGHT,padx=5)
btn_analizar = tk.Button(contenedor_superior, text="Analizar archivo", command=analizar_archivo,width=20,font=fuente,bg='#F1C40F', fg="white")
btn_analizar.pack(side=tk.RIGHT,padx=5)
menu_reportes = tk.Menu(contenedor_superior,font=fuente)
contenedor_superior.master.config(menu=menu_reportes)  
menu_reportes.add_command(label="Reporte de Tokens", command=lambda: generar_reporte("Tokens"),font=fuente)
menu_reportes.add_command(label="Reporte de Errores", command=lambda: generar_reporte("Errores"),font=fuente)
menu_reportes.add_command(label="Árbol de Derivación", command=lambda: generar_reporte("Árbol de Derivación"),font=fuente)
columna_izquierda = tk.Frame(root, padx=10,pady=10,bg='#283747')
columna_izquierda.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
columna_derecha = tk.Frame(root,padx=10,pady=10,bg='#283747')
columna_derecha.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
area_texto_izquierda = tk.Text(columna_izquierda,font=fuente)
area_texto_izquierda.pack(expand=True, fill="both")
consola_derecha = tk.Text(columna_derecha, state=tk.DISABLED,font=fuente)
consola_derecha.pack(expand=True, fill="both")
root.mainloop()
