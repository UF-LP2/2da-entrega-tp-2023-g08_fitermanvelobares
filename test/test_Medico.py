
from library.Paciente import Paciente
from library.Medico import Medico
from typing import List
import pytest


def test_Atender_Paciente():
    NoAtendidos : List[Paciente] = []
    Medico1 = Medico("35876690", "Marcelo", "Cohen")

    #no me importa el orden de la fila en este test, solo me importa que lo atienda
    Raul = Paciente("36421479","Raul","Perez",["Otalgias"])
    Jose = Paciente("46789915","Jose","Swaig",["Odontalgias", "Traumatismos"])
    Sofia = Paciente("54782464","Sofia Ana","Fleishman",["Esguinces"])
    
    NoAtendidos.append(Raul)
    NoAtendidos.append(Jose)
    NoAtendidos.append(Sofia)
    
    Medico1.Atender_Paciente(NoAtendidos)
    
    assert NoAtendidos[0].DNI == Jose.DNI
    assert NoAtendidos[0].DNI != Raul.DNI
    
    Medico1.Atender_Paciente(NoAtendidos)
    
    assert NoAtendidos[0].DNI == Sofia.DNI
    assert NoAtendidos[0].DNI != Jose.DNI
    
    
    
