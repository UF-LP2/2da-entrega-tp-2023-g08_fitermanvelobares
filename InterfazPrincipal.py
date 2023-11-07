import tkinter as tk
from library.cPaciente import Paciente
from library.cEnfermero import Enfermero
from library.cMedico import Medico
from library.LeerArchivo import LecturaArchivoSimulacion
from library.fDC import CalculoTiempoRestante

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
num_columnas = 15

# Tamaño fijo del canvas
canvas_width = 1100
canvas_height = 700

# Asigno colores a pacientes y los muestro en interfaz
def asignar_colores_pacientes():
    global pacientes
    # Crear una lista de pacientes
    pacientes = LecturaArchivoSimulacion()
    pacientes = pacientes[:120]

    for idx, paciente in enumerate(pacientes):
        enfermero = Enfermero()
        enfermero.Asignar_Color_Paciente(paciente)
        enfermero.Asignar_Lugar_FilaDC(paciente, PacientesOrdenados)

    for idx, paciente in enumerate(PacientesOrdenados):
        # Color del cuadrado
        color_pac = colores_mapping.get(paciente.ColorP.Color, "white")

        # Calcular la fila y la columna en la cuadrícula
        fila = idx // num_columnas
        columna = idx % num_columnas

        # Calcular las coordenadas para el cuadrado del paciente
        x1 = columna * (tamano_cuadrado + espacio_entre_pacientes)
        y1 = fila * (tamano_cuadrado + espacio_entre_pacientes)
        x2 = x1 + tamano_cuadrado
        y2 = y1 + tamano_cuadrado

        # Crear un cuadrado con el color de fondo del paciente en el canvas
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_pac)

        # Etiqueta con el nombre del paciente
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=f"{paciente.Nombre}", fill="black")

# Atender a los pacientes
def atender_pacientes():
    global pacientes
    for paciente in PacientesOrdenados:
        medico = Medico()
        medico.Atender_Paciente([paciente])

        # Color del cuadrado del paciente
        color_pac = colores_mapping.get(paciente.ColorP.Color, "white")

        # Calcular la fila y la columna en la cuadrícula
        fila = PacientesOrdenados.index(paciente) // num_columnas
        columna = PacientesOrdenados.index(paciente) % num_columnas

        # Calcular las coordenadas para el cuadrado del paciente
        x1 = columna * (tamano_cuadrado + espacio_entre_pacientes)
        y1 = fila * (tamano_cuadrado + espacio_entre_pacientes)
        x2 = x1 + tamano_cuadrado
        y2 = y1 + tamano_cuadrado

        # Mostrar el estado del paciente (Vivo o Muerto) dentro del cuadrado del paciente
        estado_paciente = "Vivo" if paciente.Vivo else "Muerto"
        canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2 + 15, text=estado_paciente, fill="black")

# Crear la ventana principal
window = tk.Tk()
window.title("Interfaz de Pacientes")
window.geometry("1000x800")

# Crear un marco para los botones y configurar la orientación para que estén uno al lado del otro
button_frame = tk.Frame(window)
button_frame.pack(side="top")

# Crear un botón para asignar colores a los pacientes
asignar_button = tk.Button(button_frame, text="Asignar Colores", command=asignar_colores_pacientes)
asignar_button.pack(side="left")

# Crear un botón para atender a los pacientes
atender_button = tk.Button(button_frame, text="Atender Pacientes", command=atender_pacientes)
atender_button.pack(side="left")

# Crear un canvas para mostrar a los pacientes
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="lightblue")
canvas.pack()

# Iniciar el bucle principal de la interfaz
window.mainloop()
