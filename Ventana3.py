import tkinter as tk
from tkinter import scrolledtext
import sys
from library.LeerArchivo import LecturaArchivoSimulacion
from library.fSimulacion import Simulacion
from typing import List
import random

# Función para redirigir los prints a un widget de texto en Tkinter
def redirect_output(widget):
    class StdoutRedirect:
        def __init__(self, widget):
            self.widget = widget

        def write(self, text):
            self.widget.insert(tk.END, text)
            self.widget.see(tk.END)

    sys.stdout = StdoutRedirect(widget)

def Simul():
    PacientesSimulacion = []
    PacientesSimulacion = LecturaArchivoSimulacion()
    ListaSimulacion = []

    #Comentar o descomentar el bloque de código que se quiera ejecutar
    
    PacientesSimulacion = PacientesSimulacion[:80] # para que no se trabe la compu, chequeamos solo con 80 pacientes en vez de 1000 (Comentar para chequear todos)
    while(len(PacientesSimulacion)>0): #se simula hasta que ya no haya pacientes
         auxHorario = random.randint(0, 23)
         auxCantidadPacSimulacion = random.randint(1, len(PacientesSimulacion))
         Simulacion(PacientesSimulacion[:auxCantidadPacSimulacion],auxHorario,auxCantidadPacSimulacion,ListaSimulacion)
         PacientesSimulacion = PacientesSimulacion[auxCantidadPacSimulacion:]
    
    #Simulación con horario elegido como random en vez del actual para que se vean los casos de diferente cantidad de enfermeros
    '''Simulacion(PacientesSimulacion[:8], 11, 8, ListaSimulacion)'''  # Por si se quiere chequear una cantidad exacta de pacientes

def ejecutar_simulacion():
    Simul()  # Llama a la función Simul() para ejecutar la simulación 
    
root = tk.Tk()
root.title("Hospital")
root.geometry("550x550")
root.config(bg='lightblue')
root.resizable(width=False,height=False)


text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=45, height=35)
text_widget.pack()

# Redirigir los prints a la ventana de texto
redirect_output(text_widget)

# Crear un botón que ejecuta la función con los prints
print_button = tk.Button(root, text="Ejecutar Simulacion", command=ejecutar_simulacion)
print_button.pack()

root.mainloop()


