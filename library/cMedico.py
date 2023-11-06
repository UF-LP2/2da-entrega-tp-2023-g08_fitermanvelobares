from library.cPaciente import Paciente
from typing import List
from library.fDC import CalculoTiempoRestante

class Medico:
    def __init__(self, DNI = "99999999", Nombre = "John", Apellido = "Doe"):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
    
    def Atender_Paciente(self, ListaPac: List[Paciente]):
        if(CalculoTiempoRestante(ListaPac[0])>0):
            ListaPac[0].Vivo = True
        else:
            ListaPac[0].Vivo = False #se murio el paciente por esperar mucho
        
        ListaPac.pop(0)