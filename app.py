
import html
import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
from Palabra import *
import webbrowser

PALABRAS_RESERVADAS = ["Claves", "Registros", "imprimir", "conteo", "promedio", "contarsi", "datos", "max", "min", "exportarReporte","sumar","imprimirln"]
SIGNOS = ['=', '[', ']', '{', '}', '(', ')', ',', ';']
SIGNOSRECHAZADOS = ['@','!','|','$','%','&' ,'?' ,'¿' ,'+' ,'-' ,'/','*' ,'¡','-','^','ª','º' ,'€' ,'½','~','°','©','·'] 

# tipos de tokens
TIPOS_TOKENS = {
    'PALABRA_RESERVADA': 'Palabra Reservada',
    'SIGNO': 'Signo',
    'CADENA': 'Cadena',
    'NUMERO': 'Numero',
}
listado_claves=[]
listado_registrtos=[]
global numero_fila
global numero_columna

global lista_palabras
global lista_errores

numero_fila=1
numero_columna=1
lista_palabras=[]
lista_errores=[]

def analizador(secuencia):
    global numero_fila
    global numero_columna
    global lista_palabras
    global lista_errores
    global palabras

    numero_fila=1
    lista_errores=[]
    operaciones_resultantes=[]
    lista_palabras=[]
    palabras_graficos=[]
    palabra=''
    posicion=0
    comentario=False

    while secuencia:
        num=secuencia[posicion]
        posicion +=1
        if num == '\"':
            palabra,secuencia= crear_palabra(secuencia[posicion:])
            if palabra and secuencia:
                p= Palabra("Cadena",palabra,numero_fila,numero_columna)    
                lista_palabras.append(p)
                numero_columna+=len(palabra)+2
                posicion=0
        elif num.isdigit():#alamcenar digitos
            token,secuencia = crear_numero(secuencia)
            if token and secuencia:
                #numero_columna+=1
                p=Palabra("Numero",token,numero_fila,numero_columna)
                lista_palabras.append(p)
                numero_columna+=len(str(token))+1
                posicion=0
        elif num in SIGNOS:
            p=Palabra("Signo",num,numero_fila,numero_columna)
            lista_palabras.append(p)
            numero_columna+=1
            secuencia = secuencia[1:]
            posicion = 0
        elif num in SIGNOSRECHAZADOS:
            p=Palabra("Error Lexico",num,numero_fila,numero_columna)
            lista_errores.append(p)
            numero_columna+=len(str(num))+1
            secuencia=secuencia[1:]
            posicion=0
        elif num.isalpha():
            palabra, secuencia = crear_palabra_reservada(secuencia[posicion - 1:])
            if palabra and secuencia:
                if palabra in PALABRAS_RESERVADAS:
                    p = Palabra("Palabra Reservada", palabra, numero_fila, numero_columna)
                    lista_palabras.append(p)
                else:
                    p = Palabra("Palabra ", palabra, numero_fila, numero_columna)
                    lista_errores.append(p)
                
                numero_columna += len(palabra) + 1
                posicion = 0
        elif num == '#':
            # Almacenar la línea completa en la lista de comentarios
            comentario = ''
            while secuencia and secuencia[0] != '\n':
                comentario += secuencia[0]
                secuencia = secuencia[1:]
            p = Palabra("Cadena", comentario, numero_fila, numero_columna)
            lista_palabras.append(p)
            # Actualizar el número de fila
            numero_columna += len(palabra)+1
            posicion=0
        elif num == '\'':
            if secuencia.startswith("'''"):
                cadena_triple_comillas = True
                palabra, secuencia = crear_cadena_triple_comillas(secuencia)
                if palabra:
                    p = Palabra("Cadena", palabra, numero_fila, numero_columna)
                    lista_palabras.append(p)
                    print(palabra)
                    numero_columna+= len(palabra)+1
                    comentario_multilinea = True
                else:
                    e = Palabra("Error Lexico", "Comillas simples no cerradas", numero_fila, numero_columna)
                    lista_errores.append(e)
                    secuencia = secuencia[1:]
                posicion = 0
        #por si el texto trae saltos de lineas tabulaciones para que no falle la aplicacion
        elif num == '\n':                       #saltos de linea
            secuencia = secuencia[1:]
            posicion=0
            numero_columna =1
            numero_fila+=1
        elif num == '\t': #tabulaciones
            numero_columna+=4
            secuencia=secuencia[4:]
            posicion=0
        else: #espacios
            secuencia=secuencia[1:]
            posicion = 0
            numero_columna+=1

def crear_cadena_triple_comillas(secuencia):
    global numero_fila
    global numero_columna
    global lista_palabras
    palabra = "''"
    posicion = 3

    while secuencia:
        num = secuencia[0]
        palabra += num
        secuencia = secuencia[1:]

        if palabra.endswith("''"):
            return palabra, secuencia

    return None, None

def crear_palabra(secuencia):
    global numero_fila
    global numero_columna
    global lista_palabras
    global lista_errores
    palabra=''
    posicion=''
    for num in secuencia:
        posicion+=num
        if num == '\"':
            return palabra, secuencia[len(posicion):]
        else:
            if num=='@' or num=='!' or num=='|' or num == '$' or num == '%' or num == '&' or num == '(' or num == ')' or num == '=' or num == '?' or num == '¿' or num=='+' or num=='-' or num=='/'or num=='*'or num=='¡'or num=='-' or num==';' or num=='^' or num== 'ª' or num=='º' or num=='€' or num=='½'or num=='~' or num=='°' or num=='©'or num=='·':  
                        e=Palabra("Error Lexico",num,numero_fila,numero_columna+len(palabra)+1)
                        lista_errores.append(e)
                        
            palabra+=num
    return None,None

def crear_palabra_reservada(secuencia):
    palabra = ''
    posicion = ''
    
    for num in secuencia:
        if num.isalpha():
            posicion += num
            palabra += num
        else:
            return palabra, secuencia[len(posicion):]
    return None,None

def crear_numero(secuencia):

    valornume=''
    posicion=''
    global numero_columna
    ncol=numero_columna
    decimal=False
    for num in secuencia:
        posicion+=num
        if num == '.':
            decimal=True
        if num == "," or num=='"' or num == ' ' or num=='\n' or num== '\t' or num=='}'or num==']':
            if decimal:
                return float(valornume),secuencia[len(posicion)-1:]#Python usa índices basados en cero, entonces necesito el último carácter procesado.
            else:
                return int(valornume),secuencia[len(posicion)-1:]
        else:
            if num=='@' or num=='!' or num=='|' or num=='#' or num == '$' or num == '%' or num == '&' or num == '(' or num == ')' or num == '=' or num == '?' or num == '¿' or num=='+' or num=='-' or num=='/'or num=='*'or num =='_' or num=='¡'or num=='-' or num==';' or num=='^' or num== 'ª' or num=='º' or num=='€' or num=='½'or num=='~' or num=='°' or num=='©'or num=='·':
                    e=Palabra(num,numero_fila,numero_columna+len(valornume)+1)
                    lista_errores.append(e)
            valornume+=num
            ncol+=1
    return None,None
def analizar_archivo():
    texto = area_texto_izquierda.get("1.0", "end-1c")  
    analizador(texto)
    analizador_sintactico(lista_palabras)
    almacenaryverificarRegistros()
    print("  ---------------------------- ")
    for registro in listado_registrtos:
        print(registro)

    print("  ---------------------------- ")
    print("  ---------------------------- ")
    for palabra in lista_palabras:
        print(palabra.palabra)
    print("  ---------------------------- ")
def generar_reporte(tipo_reporte):
    
    if tipo_reporte == "Tokens":
        generar_tabla_html(lista_palabras)
    if tipo_reporte == "Errores":
        generar_tabla_html2(lista_errores)

def generar_tabla_html(lista_palabras):
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Tabla de Tokens Analizados</title>
      <style>
        table {
            border-collapse: collapse; /* Para colapsar los bordes de las celdas */
            width: 50%; /* Establecer el ancho de la tabla al 50% del contenedor padre */
            margin: 0 auto; /* Centrar la tabla horizontalmente */
            border: 2px solid black; /* Establecer un borde de 2 píxeles de ancho y sólido */
        }

        th, td {
            border: 1px solid black; /* Establecer un borde de 1 píxel de ancho y sólido para celdas */
            padding: 8px; /* Añadir relleno a celdas para dar espacio al contenido */
            text-align: center; /* Centrar el contenido de las celdas horizontalmente */
        }
    </style>
</head>
<body>
    <h1>Tabla de Tokens Analizados</h1>
    <table>
        <tr>
            <th>Tipo de Token</th>
            <th>Lexema</th>
            <th>Fila</th>
            <th>Columna</th>
        </tr>
    """
    for palabra in lista_palabras:
        html += f"<tr><td>{palabra.tipo}</td><td>{palabra.palabra}</td><td>{palabra.fila}</td><td>{palabra.columna}</td></tr>\n"

    html += """
    </table>
</body>
</html>
    """

    with open("tabla_tokens.html", "w") as archivo_html:
        archivo_html.write(html)
    webbrowser.open("tabla_tokens.html")



def generar_tabla_html2(lista_error):
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Tabla de Tokens Analizados</title>
      <style>
        table {
            border-collapse: collapse; /* Para colapsar los bordes de las celdas */
            width: 50%; /* Establecer el ancho de la tabla al 50% del contenedor padre */
            margin: 0 auto; /* Centrar la tabla horizontalmente */
            border: 2px solid black; /* Establecer un borde de 2 píxeles de ancho y sólido */
        }

        th, td {
            border: 1px solid black; /* Establecer un borde de 1 píxel de ancho y sólido para celdas */
            padding: 8px; /* Añadir relleno a celdas para dar espacio al contenido */
            text-align: center; /* Centrar el contenido de las celdas horizontalmente */
        }
    </style>
</head>
<body>
    <h1>Tabla de Errores</h1>
    <table>
        <tr>
            <th>Tipo de Error</th>
            <th>Error</th>
            <th>Fila</th>
            <th>Columna</th>
        </tr>
    """
    for palabra in lista_error:
        if palabra.tipo == "Error Lexico" or palabra.tipo == "Error Sintactico":
            html += f"<tr><td>{palabra.tipo}</td><td>{palabra.palabra}</td><td>{palabra.fila}</td><td>{palabra.columna}</td></tr>\n"
    html += """
    </table>
</body>
</html>
    """

    with open("tabla_errores.html", "w") as archivo_html:
        archivo_html.write(html)
    webbrowser.open("tabla_errores.html")
    
def cargar_archivo():
    file_path = filedialog.askopenfilename(filetypes=[("Archivo bizdata", "*.bizdata")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            area_texto_izquierda.delete(1.0, tk.END)  
            area_texto_izquierda.insert(tk.END, content)  




#ANALIZADOR SINTACTICO
def analizador_sintactico(tokens):
    pass
def almacenaryverificarRegistros():
    i = 0
    while i < len(lista_palabras):
        palabra = lista_palabras[i]

        if palabra.palabra == "Registros":
            if i + 1 < len(lista_palabras):
                siguiente = lista_palabras[i + 1]
                if siguiente.palabra == "=":
                    i += 2  # Saltar "Registros" y "="

                    if i < len(lista_palabras):
                        if lista_palabras[i].palabra == "[":
                            i += 1  # Saltar "["

                            while i < len(lista_palabras):
                                if lista_palabras[i].palabra == "{":
                                    i += 1  # Saltar "{"
                                    registro = []
                                    continuar = True
                                    while i < len(lista_palabras) and continuar:
                                        if lista_palabras[i].palabra == "}":
                                            if lista_palabras[i+1].palabra == "]":
                                                i += 1  # Saltar "]"
                                                print("salio")
                                                break
                                            continuar=False
                                            i += 1
                                        elif lista_palabras[i].palabra == ",":
                                            i += 1  # Saltar ","
                                        else:
                                            # Verificar si el elemento es un número o cadena
                                            if lista_palabras[i].tipo in ["Numero", "Cadena"]:
                                                listado_registrtos.append(lista_palabras[i].palabra)
                                                i += 1
                                       
                                            else:
                                                p = Palabra("Error Sintactico",lista_palabras[i].palabra,lista_palabras[i].fila,lista_palabras[i].columna)
                                                lista_errores.append(p)
                                                i += 1
                                elif lista_palabras[i].palabra == "]":
                                    i += 1  # Saltar "]"
                                    #print("salio")
                                    break
                                else:
                                    p = Palabra("Error Sintactico",lista_palabras[i].palabra,lista_palabras[i].fila,lista_palabras[i].columna)
                                    lista_errores.append(p)
                                    i += 1
                        else:
                            p = Palabra("Error Sintactico",lista_palabras[i].palabra,lista_palabras[i].fila,lista_palabras[i].columna)
                            lista_errores.append(p)
                    else:
                        p = Palabra("Error Sintactico",lista_palabras[i].palabra,lista_palabras[i].fila,lista_palabras[i].columna)
                        lista_errores.append(p)

                else:
                    p = Palabra("Error Sintactico",siguiente.palabra,siguiente.fila,siguiente.columna)
                    lista_errores.append(p)

            else:
                p = Palabra("Error Sintactico",lista_palabras[i].palabra,lista_palabras[i].fila,lista_palabras[i].columna)
                lista_errores.append(p)
        i += 1
                    

root = tk.Tk()
root.title("Proyecto 2 - BIZDATA - 202201989")
fuente=tkFont.Font(family='Helvetica', size=14)
fuente1=tkFont.Font(family='Helvetica', size=12)
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
area_texto_izquierda = tk.Text(columna_izquierda,font=fuente1)
area_texto_izquierda.pack(expand=True, fill="both")
consola_derecha = tk.Text(columna_derecha, state=tk.DISABLED,font=fuente1)
consola_derecha.pack(expand=True, fill="both")
root.mainloop()



