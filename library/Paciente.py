from typing import List
from datetime import datetime
from library.Colores import Colores
class Paciente:
    def __init__(self, DNI: str, Nombre: str, Apellido: str, Sintomas: List[str], Color = "Blanco", HorarioTriage = None, Vivo = True, Envejecido = False):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Sintomas = Sintomas
        self.ColorP = Colores(Color)  
        if HorarioTriage is None:
            HorarioTriage = datetime(2023, 11, 6, 0, 0, 0)
        self.HorarioTriage = HorarioTriage
        self.Vivo = Vivo #vivo o muerto
        self.Envejecido = Envejecido

