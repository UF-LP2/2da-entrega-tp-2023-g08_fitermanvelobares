from library.cPaciente import Paciente
from typing import List

class Medico:
    def __init__(self, DNI: str, Nombre: str, Apellido: str):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
    
    def Atender_Paciente(self, ListaPac: List[Paciente]):
        ListaPac.pop(0)