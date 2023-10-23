from typing import List
from datetime import datetime
class Paciente:
    def __init__(self, DNI: str, Nombre: str, Apellido: str, Sintomas: List[str], Color="Blanco", HorarioTriage = datetime(1, 1, 1, 0, 0, 0)):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Sintomas = Sintomas
        self.Color = Color  
        self.HorarioTriage = HorarioTriage
