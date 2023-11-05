import csv
from library.cPaciente import Paciente
from typing import List

def LecturaArchivoSimulacion():
    ListasinAtender = []
    with open(r"SimulacionPacientes.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            DNI = row[0]
            Nombre = row[1]
            Apellido = row[2]
            Sintomas = [str(Sintoma) for Sintoma in row[3:]]
            paciente = Paciente(DNI,Nombre,Apellido,Sintomas)
            
            ListasinAtender.append(paciente)
    
    return ListasinAtender



