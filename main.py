from library.fLeerArchivo import LecturaArchivoSimulacion
import csv
from typing import List
from datetime import datetime
from library.cPaciente import Paciente
from library.cEnfermero import Enfermero
from library.cMedico import Medico

def main():
  print("Hello World")
  hola = []
  hola = LecturaArchivoSimulacion()
  for paciente in hola:
    print(paciente.Nombre)
    print(paciente.Apellido)
    print(paciente.DNI)
  

if __name__== "__main__":
  main()