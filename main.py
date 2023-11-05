from library.LeerArchivo import LecturaArchivoSimulacion
import csv
from typing import List
from datetime import datetime
from library.Paciente import Paciente
from library.Enfermero import Enfermero
from library.Medico import Medico

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