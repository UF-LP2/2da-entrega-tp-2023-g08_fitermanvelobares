from library.PacRepetidoException import PacRepetidoException
from typing import List

def CheckPacRepetido (ListaPac, DNI):
    repetido = False
    for i in range(len(ListaPac)):
        if DNI == ListaPac[i].DNI:
            repetido = True
            raise PacRepetidoException (f"{ListaPac[i]} esta repetido en la lista.") #faltaria parte main...
            break
            
    return repetido