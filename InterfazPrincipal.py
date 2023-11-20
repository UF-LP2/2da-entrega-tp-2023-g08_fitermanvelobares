import tkinter as tk
from library.Paciente import Paciente
from library.Enfermero import Enfermero
from library.Medico import Medico
from LeerArchivo import LecturaArchivoSimulacion
from PIL import Image, ImageTk
import random
import time

# Defino colores
colores_mapping = {
    "Rojo": "#FD3B3B",
    "Naranja": "#FE7B07",
    "Amarillo": "#FFBA49",
    "Verde": "#41DB72",
    "Azul": "#3066BE"
}

# Tamaño de los cuadrados de los pacientes en píxeles
tamano_cuadrado = 60

# Espacio entre pacientes en píxeles
espacio_entre_pacientes = 5

# Listas de pacientes
pacientes = []
PacientesOrdenados = []

# Número de columnas
num_columnas = 10

# Tamaño fijo del canvas
canvas_width = 700
canvas_height = 500

#posicion en la lista del archivo
posicion_actual = 0

canvas = None

def limpiar_canvas():
    global canvas
    if canvas:
        canvas.delete("all")

# Asigno colores a pacientes y los muestro en interfaz
def Interfaz():
    limpiar_canvas()
    global pacientes, PacientesOrdenados, posicion_actual, canvas
    PacientesOrdenados = []

    AuxPacientes = LecturaArchivoSimulacion()
    auxCantidadPacSimulacion = random.randint(1, 50) 
    pacientes = AuxPacientes[posicion_actual:posicion_actual+auxCantidadPacSimulacion]
    
    for idx, paciente in enumerate(pacientes):
        enfermero = Enfermero()
        enfermero.Asignar_Color_Paciente(paciente)
        enfermero.Asignar_Lugar_FilaDC(paciente, PacientesOrdenados)
    
    for idx, paciente in enumerate(PacientesOrdenados):
        color_pac = colores_mapping.get(paciente.ColorP.Color, "white") # Color del cuadrado = color del paciente

        #Calculo de fila y columna en la cuadrícula
        fila = idx // num_columnas
        columna = idx % num_columnas

        # Calculo coordenadas cuadrado del paciente
        x1 = columna * (tamano_cuadrado + espacio_entre_pacientes)+3
        y1 = fila * (tamano_cuadrado + espacio_entre_pacientes)
        x2 = x1 + tamano_cuadrado
        y2 = y1 + tamano_cuadrado

        # Creo cuadrado del paciente con su color asignado
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_pac)

        #Nombre pac
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"{paciente.Nombre}", fill="black")
        
    for paciente in PacientesOrdenados:
        medico = Medico()
        medico.Atender_Paciente([paciente])
        
        color_pac = colores_mapping.get(paciente.ColorP.Color, "white")

        #Fila y la columna en la cuadrícula
        fila = PacientesOrdenados.index(paciente) // num_columnas
        columna = PacientesOrdenados.index(paciente) % num_columnas

        # Coordenadas para el cuadrado del paciente
        x1 = columna * (tamano_cuadrado + espacio_entre_pacientes)
        y1 = fila * (tamano_cuadrado + espacio_entre_pacientes)
        x2 = x1 + tamano_cuadrado
        y2 = y1 + tamano_cuadrado
        
        # Estado del paciente (Vivo o Muerto) dentro del cuadrado
        estado_paciente = "Vivo" if paciente.Vivo else "Muerto"
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2 + 15, text=estado_paciente, fill="black")
    
    PacientesOrdenados = []
    posicion_actual += auxCantidadPacSimulacion


#ventana principal
window = tk.Tk()
window.title("Hospital FitBares")
window.geometry("700x500")

#imagen en la parte inferior
imagen = Image.open("logo2.gif")

#Cambio el tamaño de la imagen
nuevo_ancho = imagen.width // 2
nuevo_alto = imagen.height // 2
imagen.thumbnail((nuevo_ancho, nuevo_alto))
imagen = ImageTk.PhotoImage(imagen)
imagen_frame = tk.Frame(window)
imagen_frame.pack(side="bottom")


imagen_label = tk.Label(imagen_frame, image=imagen)
imagen_label.pack()


#botones, orientación: uno al lado del otro
button_frame = tk.Frame(window)
button_frame.pack(side="top")


asignar_button = tk.Button(button_frame, text="Simular", command=Interfaz)
asignar_button.pack(side="left")

limpiar_button = tk.Button(button_frame, text="Borrar Graficos", command=limpiar_canvas)
limpiar_button.pack(side="left")

# Canvas para mostrar a los pacientes
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()


window.mainloop()


