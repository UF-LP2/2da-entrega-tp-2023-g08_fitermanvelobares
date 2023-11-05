from library.cPaciente import Paciente
from library.cEnfermero import Enfermero
import pytest
from typing import List
from datetime import datetime
from library.fDC import InsercionBinaria

def test_FilaDivideConquer():
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    
    Julio = Paciente("12564938", "Julio", "Doe", ["Resfrio"], "Azul", datetime(2023,11,3,16,40,1))
    Maria = Paciente("34784920", "Maria", "Smith", ["Vertigo Con Afectacion Vegetativa","Sincope"], "Amarillo",datetime(2023,11,3,17,40,1))
    Sofia = Paciente("54782464","Sofia Ana","Fleishman",["Esguinces"], "Verde", datetime(2023,11,3,18,15,1))
    Raul = Paciente("36421479","Raul","Perez",["No Respira"], "Rojo", datetime(2023,11,3,18,20,1))
    Pedro = Paciente("48902533","Pedro","Pascal",["Esguinces"], "Verde",datetime(2023,11,3,20,21,1))
    Malena = Paciente("46789915","Malena","Krupnik",["Sincope"],"Amarillo", datetime(2023,11,3,20,23,1))
    Jose = Paciente("46789915","Jose","Swaig",["Coma"],"Naranja", datetime(2023,11,3,20,23,5))

    ListaNoAtentidos = []
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Julio,ListaNoAtentidos) #se agrega julio a la lista. Esp hasta: 20:40
    
    assert ListaNoAtentidos[0].Nombre == Julio.Nombre
    assert ListaNoAtentidos[0].Nombre != Sofia.Nombre
    #Lista = Julio
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Maria,ListaNoAtentidos) #se aregega a maria a la lista. Esp hasta: 16:40
    assert ListaNoAtentidos[0].Nombre == Maria.Nombre
    assert ListaNoAtentidos[0].Nombre != Julio.Nombre
    assert ListaNoAtentidos[1].Nombre == Julio.Nombre
    #Lista = Maria - Julio
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Sofia,ListaNoAtentidos) #se aregega a Sofia a la lista. Esp hasta: 20:15
    assert ListaNoAtentidos[0].Nombre == Maria.Nombre
    assert ListaNoAtentidos[1].Nombre == Sofia.Nombre
    assert ListaNoAtentidos[2].Nombre == Julio.Nombre
    assert ListaNoAtentidos[1].Nombre != Julio.Nombre
    #Lista = Maria - Sofia - Julio
    
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Raul,ListaNoAtentidos) #se aregega a Raul a la lista. NO ESPERA
    assert ListaNoAtentidos[0].Nombre == Raul.Nombre
    assert ListaNoAtentidos[1].Nombre == Maria.Nombre
    assert ListaNoAtentidos[2].Nombre == Sofia.Nombre
    assert ListaNoAtentidos[3].Nombre == Julio.Nombre
    
    assert ListaNoAtentidos[0].Nombre != Maria.Nombre
    assert ListaNoAtentidos[1].Nombre != Sofia.Nombre
    assert ListaNoAtentidos[2].Nombre != Julio.Nombre
    #Lista = Raul - Maria - Sofia - Julio
     
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Pedro,ListaNoAtentidos) #se aregega a Pedro a la lista. Esp hasta:  22:21 
    assert ListaNoAtentidos[0].Nombre == Raul.Nombre
    assert ListaNoAtentidos[1].Nombre == Maria.Nombre
    assert ListaNoAtentidos[2].Nombre == Sofia.Nombre
    assert ListaNoAtentidos[3].Nombre == Julio.Nombre 
    assert ListaNoAtentidos[4].Nombre == Pedro.Nombre
    #Lista = Raul - Maria - Sofia - Julio - Pedro
      
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Malena,ListaNoAtentidos) #se aregega a Malena a la lista. Esp hasta: 21:23
    ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Jose,ListaNoAtentidos) #se aregega a Jose a la lista. Esp hasta: 20:33
    
    
    