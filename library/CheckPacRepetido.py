from library.PacRepetidoException import PacRepetidoException
from library.Paciente import Paciente
from typing import List

def CheckPacRepetido (ListaPac:List[Paciente], Pac:Paciente):
    for i in range(len(ListaPac)):
        if Pac.DNI == ListaPac[i].DNI:
            raise PacRepetidoException (f"{ListaPac[i]} esta repetido en la lista.") #faltaria parte main...