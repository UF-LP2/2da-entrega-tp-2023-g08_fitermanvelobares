from typing import List

class Paciente:
    def __init__(self, DNI: str, Nombre: str, Apellido: str, Sintomas: List[str], Color="Blanco"):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Sintomas = Sintomas
        self.Color = Color  # Puedes asignar un color predeterminado si lo deseas
