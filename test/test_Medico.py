
from library.Paciente import Paciente
from library.Medico import Medico
from typing import List
import pytest


def test_Atender_Paciente():
    NoAtendidos : List[Paciente] = []
    Medico1 = Medico("35876690", "Marcelo", "Cohen")
    #creo Medico y la lista
    
    Raul = Paciente("36421479","Raul","Perez",["Otalgias"])
    Jose = Paciente("46789915","Jose","Swaig",["Odontalgias", "Traumatismos"])
    Sofia = Paciente("54782464","Sofia Ana","Fleishman",["Esguinces"])
    #creo pacientes
    
    NoAtendidos.append(Raul)
    NoAtendidos.append(Jose)
    NoAtendidos.append(Sofia)
    #inserto los pacientes a la lista "NoAtendidos", sin tener en cuenta prioridades
    #no nos importa el orden de la fila (prioridades) en este test, solo  importa que los atienda desde el principio de la fila (pos[0])

    
    Medico1.Atender_Paciente(NoAtendidos)
    #atiende a Raul
    
    assert NoAtendidos[0].DNI == Jose.DNI
    assert NoAtendidos[0].DNI != Raul.DNI
    #Raul ya no se encuentra en la fila, ahora el primero es Jose
    
    Medico1.Atender_Paciente(NoAtendidos)
    #atiende a Jose 
        
    assert NoAtendidos[0].DNI == Sofia.DNI
    assert NoAtendidos[0].DNI != Jose.DNI
    #Jose ya no se encuentra en la fila, ahora la primera es Sofia
    
    
