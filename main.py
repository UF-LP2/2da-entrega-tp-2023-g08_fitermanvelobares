from library.LeerArchivo import LecturaArchivoSimulacion
import csv
from typing import List
from datetime import datetime
from library.Paciente import Paciente
from library.Enfermero import Enfermero
from library.Medico import Medico

def main() -> None:
  print("Hello World")
  Probando123 = []
  LecturaArchivoSimulacion(Probando123)
  
  for paciente in Probando123:
    print(f"Nombre: {paciente.Nombre}, Apellido: {paciente.Apellido}")
    print("Síntomas:", paciente.Sintomas)


if __name__== "_main_":
  main()