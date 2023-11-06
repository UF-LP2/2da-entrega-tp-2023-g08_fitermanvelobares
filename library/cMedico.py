from library.cPaciente import Paciente
from typing import List

class Medico:
    def __init__(self, DNI = "99999999", Nombre = "John", Apellido = "Doe"):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
    
    def Atender_Paciente(self, ListaPac: List[Paciente]):
        ListaPac.pop(0)