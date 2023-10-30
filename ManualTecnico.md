# Manual Técnico: Aplicación de Análisis Léxico y Operaciones Matemáticas

### Universidad San Carlos de Guatemala
Escuela de Ciencias y Sistemas 

Segundo Semestre 2023

Lenguajes Formales y de Programación

## Descripción del Proyecto
Este proyecto consiste en una aplicación que realiza análisis léxico de un lenguaje de programación personalizado y ejecuta operaciones matemáticas. 


## Objetivos
* Objetivo General
    * Desarrollar un sistema de análisis léxico y sintactico para reconocer un lenguaje dado, gestionar archivos y generar informes de análisis sintactico y lexico.

* Objetivos Específicos
    * Analizador Léxico y Sintactico: Implementar un analizador léxico y sintactico basado en estados para reconocer tokens y palabras reservadas en el código fuente.
    * Gestión de Archivos: Crear funciones para abrir, guardar y guardar como archivos con formato JSON.
    * Generación de Informes: Generar informes de análisis léxico que incluyan detalles sobre tokens y errores, y guardarlos en un archivo JSON.
    * Interfaz Gráfica: Diseñar una interfaz gráfica de usuario utilizando la biblioteca Tkinter para cargar y analizar código fuente.
    * Graficación de Árboles: Utilizar la biblioteca Graphviz para generar y mostrar diagramas de árbol de las operaciones analizadas.
   


---
## Implementación
### Función analizador(secuencia):

- Analiza una secuencia de caracteres que representa código fuente.
- Identifica y clasifica palabras, números, símbolos y errores léxicos en el código.
- Almacena los resultados en listas globales.
### Función crear_cadena_triple_comillas(secuencia):

- Busca y crea una cadena que está entre comillas triples '''.
### Función crear_palabra(secuencia):

- Crea una palabra a partir de caracteres en la secuencia.
- Identifica errores léxicos si encuentra caracteres no válidos.
### Función crear_palabra_reservada(secuencia):

- Crea palabras reservadas a partir de caracteres en la secuencia.
### Función crear_numero(secuencia):

- Crea números a partir de caracteres en la secuencia.
- Identifica números enteros y flotantes.
- Identifica errores léxicos si encuentra caracteres no válidos.
### Función generar_tabla_html(lista_palabras):

- Genera una tabla HTML que muestra los tokens analizados, incluyendo su tipo, lexema, fila y columna.
- Abre un archivo HTML en modo escritura, escribe el contenido HTML en el archivo y lo abre en el navegador web.
### Función generar_tabla_html2(lista_error):

- Similar a generar_tabla_html, pero genera una tabla para mostrar los errores léxicos y sintácticos en lugar de los tokens analizados.
### Función cargar_archivo():

- Abre un cuadro de diálogo para que el usuario seleccione un archivo con extensión ".bizdata".
- Lee el contenido del archivo seleccionado y lo muestra en un área de texto en la interfaz.
### Función analizador_sintactico():

- Realiza un análisis sintáctico adicional para identificar comandos específicos del lenguaje.
- Puede identificar y ejecutar comandos como "conteo", "datos", "imprimir", "imprimirln", etc.
- Muestra los resultados de estos comandos en la consola derecha.
### Función verificarcontarsi(token):
- Realiza un análisis sintáctico para identificar y ejecutar el comando "contarsi".
- Calcula y muestra el número de veces que un valor dado se repite en un campo especificado.
###  Metodo de árbol
![Vista Principal](https://github.com/Serrano18/LFP_S2_2023_Proyecto2_202201989/blob/main/Imagenes/Interfaz.png)
###  AFD
![Vista Principal](https://github.com/Serrano18/LFP_S2_2023_Proyecto2_202201989/blob/main/Imagenes/Interfaz.png)
### Gramática
![Vista Principal](https://github.com/Serrano18/LFP_S2_2023_Proyecto2_202201989/blob/main/Imagenes/Interfaz.png)