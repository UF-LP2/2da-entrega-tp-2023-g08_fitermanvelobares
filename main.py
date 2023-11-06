from library.LeerArchivo import LecturaArchivoSimulacion
import csv
from typing import List
import random
from datetime import datetime
from library.cPaciente import Paciente
from library.cEnfermero import Enfermero
from library.cMedico import Medico
from library.fSimulacion import Simulacion


def main():
  
  PacientesSimulacion = []
  PacientesSimulacion = LecturaArchivoSimulacion()
  ListaSimulacion = []
 
  '''PacientesSimulacion = PacientesSimulacion[:80] #para que no se trabe la compu, chequeamos solo con 80 pacientes en vez de 1000
  while(len(PacientesSimulacion)>0): #se simula hasta que ya no haya pacientes
    auxHorario = random.randint(0, 23) 
    auxCantidadPacSimulacion = random.randint(1, len(PacientesSimulacion)) 
    
    Simulacion(PacientesSimulacion[:auxCantidadPacSimulacion],auxHorario,auxCantidadPacSimulacion,ListaSimulacion)
    PacientesSimulacion = PacientesSimulacion[auxCantidadPacSimulacion:]
  ''' #Simulacion
  
  Simulacion(PacientesSimulacion[:8],11,8,ListaSimulacion) #si se quiere chequear una cant exacta de pacientes 

if __name__== "__main__":
  main()