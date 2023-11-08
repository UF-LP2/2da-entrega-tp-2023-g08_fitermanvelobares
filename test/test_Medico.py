
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
    Mario = Paciente("386903394","Mario","Perez",["No Respira"])
    Pedro = Paciente("48902533","Pedro","Pascal",["Esguinces"])
    Malena = Paciente("45678325","Malena","Krupnik",["Sincope"])
    Ivan = Paciente("25853573","Jose","Swaig",["Coma"],"Naranja")

    #creo pacientes
    
    NoAtendidos.append(Raul)
    NoAtendidos.append(Jose)
    NoAtendidos.append(Sofia)
    NoAtendidos.append(Mario)
    NoAtendidos.append(Pedro)
    NoAtendidos.append(Malena)
    NoAtendidos.append(Ivan)
    #inserto los pacientes a la lista "NoAtendidos", sin tener en cuenta prioridades
    #no nos importa el orden de la fila (prioridades) en este test, solo  importa que los atienda desde el principio de la fila (pos[0])

    
    Medico1.Atender_Paciente(NoAtendidos)
    #atiende a Raul
    assert len(NoAtendidos) == 6
    assert NoAtendidos[0].DNI == Jose.DNI
    assert NoAtendidos[0].DNI != Raul.DNI
    #Raul ya no se encuentra en la fila, ahora el primero es Jose
    
    Medico1.Atender_Paciente(NoAtendidos)
    #atiende a Jose 
    assert len(NoAtendidos) == 5    
    assert NoAtendidos[0].DNI == Sofia.DNI
    assert NoAtendidos[0].DNI != Jose.DNI
    
    
    Medico1.Atender_Paciente(NoAtendidos)
    Medico1.Atender_Paciente(NoAtendidos)
    assert len(NoAtendidos) == 3   
    assert NoAtendidos[0].DNI == Pedro.DNI
    #Jose ya no se encuentra en la fila, ahora la primera es Sofia
    
    
