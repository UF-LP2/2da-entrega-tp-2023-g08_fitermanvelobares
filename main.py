import csv
from typing import List
import random
from datetime import datetime
from library.Paciente import Paciente
from library.Enfermero import Enfermero
from library.Medico import Medico
from library.Simulacion import Simulacion
from InterfazPrincipal import Interfaz
from LeerArchivo import LecturaArchivoSimulacion


def main():
  PacientesSimulacion = []
  PacientesSimulacion = LecturaArchivoSimulacion()
  ListaPacientesSinAtender = []
 
  '''PacientesSimulacion = PacientesSimulacion[:80]''' #para que no se trabe la compu, chequeamos solo con 80 pacientes en vez de 1000
  while(len(PacientesSimulacion)>0): #se simula hasta que ya no haya pacientes
    auxCantidadPacSimulacion = random.randint(1, len(PacientesSimulacion)) 
    
    Simulacion(PacientesSimulacion[:auxCantidadPacSimulacion],auxCantidadPacSimulacion,ListaPacientesSinAtender)
    PacientesSimulacion = PacientesSimulacion[auxCantidadPacSimulacion:]
  #Simulacion con horario elegido como random en vez del actual para que se vean los casos de diferente cantidad de enfermeros
  
  '''Simulacion(PacientesSimulacion[:8],8,ListaSimulacion)''' #si se quiere chequear una cant exacta de pacientes 

  #Simulacion 1000 pacientes^^
    
  #Interfaz:
  Interfaz()
  
  
if __name__== "__main__":
  main()
  