from library.Paciente import Paciente
from library.Enfermero import Enfermero
import pytest
from typing import List
from datetime import datetime

def test_FilaVoraz():
    Raul = Paciente("36421479","Raul","Perez",["No Respira"], "Rojo")
    Jose = Paciente("46789915","Jose","Swaig",["Otalgias", "Politraumatismo Grave"],"Amarillo")
    Maria = Paciente("34784920", "Maria", "Smith", ["Vertigo Con Afectacion Vegetativa","Sincope"], "Amarillo")
    Julio = Paciente("12564938", "Julio", "Doe", ["Resfrio"], "Azul")
    Sofia = Paciente("54782464","Sofia Ana","Fleishman",["Esguinces"], "Naranja")
    Pedro = Paciente("48902533","Pedro","Pascal",["Esguinces"], "Naranja")
    Malena = Paciente("46789915","Malena","Krupnik",["Otalgias", "Politraumatismo Grave"],"Amarillo")
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    
    #creo pacientes y enfermero
    
    ListaPac : List[Paciente] = []
    #creo lista de pacientes
    
    Enfermero1.Asignar_Lugar_FilaV(Raul, ListaPac) #enfermero asigna lugar en la fila a los pacientes
    assert ListaPac[0].DNI == Raul.DNI
    assert ListaPac[0].DNI != Jose.DNI #jose ni esta en la fila
    
    Enfermero1.Asignar_Lugar_FilaV(Jose, ListaPac) #agregamos a jose a la fila, deberia quedar segundo en la fila
    assert ListaPac[0].DNI == Raul.DNI 
    assert ListaPac[1].DNI == Jose.DNI
    assert ListaPac[0].DNI != Jose.DNI 
    assert ListaPac[1].DNI != Raul.DNI
     
    Enfermero1.Asignar_Lugar_FilaV(Maria, ListaPac) # Maria es amarillo, iria despues que Jose
    assert ListaPac[0].DNI == Raul.DNI
    assert ListaPac[1].DNI == Jose.DNI
    assert ListaPac[2].DNI == Maria.DNI
    
    assert ListaPac[1].DNI != Raul.DNI
    assert ListaPac[0].DNI != Maria.DNI

    Enfermero1.Asignar_Lugar_FilaV(Julio, ListaPac) #Es azul, va ultimo
    assert ListaPac[0].DNI == Raul.DNI
    assert ListaPac[1].DNI == Jose.DNI
    assert ListaPac[2].DNI == Maria.DNI
    assert ListaPac[3].DNI == Julio.DNI
    
    Enfermero1.Asignar_Lugar_FilaV(Sofia, ListaPac) #agregamos a sofia, deberia quedar segunda en la fila
    assert ListaPac[0].DNI == Raul.DNI
    assert ListaPac[1].DNI == Sofia.DNI
    assert ListaPac[2].DNI == Jose.DNI
    assert ListaPac[3].DNI == Maria.DNI
    assert ListaPac[4].DNI == Julio.DNI

    Enfermero1.Asignar_Lugar_FilaV(Pedro, ListaPac) #agregamos a Pedro, deberia quedar desp de sofia
    assert ListaPac[0].DNI == Raul.DNI
    assert ListaPac[1].DNI == Sofia.DNI
    assert ListaPac[2].DNI == Pedro.DNI
    assert ListaPac[3].DNI == Jose.DNI
    assert ListaPac[4].DNI == Maria.DNI
    assert ListaPac[5].DNI == Julio.DNI

    Enfermero1.Asignar_Lugar_FilaV(Malena, ListaPac) #agregamos a malena, deberia quedar desp de maria
    assert ListaPac[0].DNI == Raul.DNI
    assert ListaPac[1].DNI == Sofia.DNI
    assert ListaPac[2].DNI == Pedro.DNI
    assert ListaPac[3].DNI == Jose.DNI
    assert ListaPac[4].DNI == Maria.DNI
    assert ListaPac[5].DNI == Malena.DNI
    assert ListaPac[6].DNI == Julio.DNI
    
    
    