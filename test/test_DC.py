from library.Paciente import Paciente
from library.Enfermero import Enfermero
from library.DC import CalculoTiempoRestante
import pytest
from typing import List
from datetime import datetime

def test_FilaDivideConquer():
    Enfermero1 = Enfermero(True,"57531189", "Silvio", "Mendex")
    
    Julio = Paciente("12564938", "Julio", "Doe", ["Resfrio"], "Azul", datetime(2023,11,3,16,40,1))
    Maria = Paciente("34784920", "Maria", "Smith", ["Vertigo Con Afectacion Vegetativa","Sincope"], "Amarillo",datetime(2023,11,3,18,40,1))
    Sofia = Paciente("54782464","Sofia Ana","Fleishman",["Esguinces"], "Verde", datetime(2023,11,3,18,15,1))
    Raul = Paciente("36421479","Raul","Perez",["No Respira"], "Rojo", datetime(2023,11,3,18,20,1))
    Pedro = Paciente("48902533","Pedro","Pascal",["Esguinces"], "Verde",datetime(2023,11,3,20,21,1))
    Malena = Paciente("46789915","Malena","Krupnik",["Sincope"],"Amarillo", datetime(2023,11,3,20,23,1))
    Jose = Paciente("46789915","Jose","Swaig",["Coma"],"Naranja", datetime(2023,11,3,20,23,5))

    ListaNoAtentidos = []
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Julio,ListaNoAtentidos) #se agrega julio a la lista. Esp hasta: 20:40
    
    assert ListaNoAtentidos[0].DNI == Julio.DNI
    assert ListaNoAtentidos[0].DNI != Sofia.DNI
    #Lista = Julio
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Maria,ListaNoAtentidos) #se aregega a maria a la lista. Esp hasta: 19:40
    assert ListaNoAtentidos[0].DNI == Maria.DNI
    assert ListaNoAtentidos[0].DNI != Julio.DNI
    assert ListaNoAtentidos[1].DNI == Julio.DNI
    #Lista = Maria - Julio
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Sofia,ListaNoAtentidos) #se aregega a Sofia a la lista. Esp hasta: 20:15
    assert ListaNoAtentidos[0].DNI == Maria.DNI
    assert ListaNoAtentidos[1].DNI == Sofia.DNI
    assert ListaNoAtentidos[2].DNI == Julio.DNI
    assert ListaNoAtentidos[1].DNI != Julio.DNI
    #Lista = Maria - Sofia - Julio
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Raul,ListaNoAtentidos) #se aregega a Raul a la lista. NO ESPERA
    assert ListaNoAtentidos[0].DNI == Raul.DNI
    assert ListaNoAtentidos[1].DNI == Maria.DNI
    assert ListaNoAtentidos[2].DNI == Sofia.DNI
    assert ListaNoAtentidos[3].DNI == Julio.DNI
    
    assert ListaNoAtentidos[0].DNI != Maria.DNI
    assert ListaNoAtentidos[1].DNI != Sofia.DNI
    assert ListaNoAtentidos[2].DNI != Julio.DNI
    #Lista = Raul - Maria - Sofia - Julio
     
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Pedro,ListaNoAtentidos) #se aregega a Pedro a la lista. Esp hasta:  22:21     
    assert ListaNoAtentidos[0].DNI == Raul.DNI
    assert ListaNoAtentidos[1].DNI == Maria.DNI
    assert ListaNoAtentidos[2].DNI == Sofia.DNI
    assert ListaNoAtentidos[3].DNI == Julio.DNI 
    assert ListaNoAtentidos[4].DNI == Pedro.DNI
    #Lista = Raul - Maria - Sofia - Julio - Pedro

    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Malena,ListaNoAtentidos) #se aregega a Malena a la lista. Esp hasta: 21:23
    assert ListaNoAtentidos[0].DNI == Raul.DNI
    assert ListaNoAtentidos[1].DNI == Maria.DNI
    assert ListaNoAtentidos[2].DNI == Sofia.DNI
    assert ListaNoAtentidos[3].DNI == Julio.DNI 
    assert ListaNoAtentidos[4].DNI == Malena.DNI
    assert ListaNoAtentidos[5].DNI == Pedro.DNI
    
    assert ListaNoAtentidos[4].DNI != Pedro.DNI
    #Lista = Raul - Maria - Sofia - Julio - Malena - Pedro
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Jose,ListaNoAtentidos) #se aregega a Jose a la lista. Esp hasta: 20:33
    assert ListaNoAtentidos[0].DNI == Raul.DNI
    assert ListaNoAtentidos[1].DNI == Maria.DNI
    assert ListaNoAtentidos[2].DNI == Sofia.DNI
    assert ListaNoAtentidos[3].DNI == Jose.DNI
    assert ListaNoAtentidos[4].DNI == Julio.DNI 
    assert ListaNoAtentidos[5].DNI == Malena.DNI
    assert ListaNoAtentidos[6].DNI == Pedro.DNI
    
    #Lista = Raul - Jose - Maria - Sofia - Julio - Malena - Pedro    
    