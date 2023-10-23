from library.Paciente import Paciente
from library.Enfermero import Enfermero
import pytest

def test_PacienteRojo():
   
    Raul = Paciente("36421479","Raul","Perez",["No Respira"])
    Jose = Paciente("46789915","Jose","Swaig",["Otalgias", "Politraumatismo Grave"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
    
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes
    
    assert Raul.Color == "Rojo"
    assert not Raul.Color == "Azul"
    
    assert Jose.Color == "Rojo"
    assert not Jose.Color == "Verde"
    #chequeo colores
    

def test_PacienteNaranja():
   
    Raul = Paciente("36421479","Raul","Perez",["Coma"])
    Jose = Paciente("46789915","Jose","Swaig",["Otalgias", "Convulsiones"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
     
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes

    assert Raul.Color == "Naranja"
    assert not Raul.Color == "Azul"
    
    assert Jose.Color == "Naranja"
    assert not Jose.Color == "Verde"
    #chequeo colores

def test_PacienteAmarillo() -> None:
   
    Raul = Paciente("36421479","Raul","Perez",["Cefalea Brusca"])
    Jose = Paciente("46789915","Jose","Swaig",["Otalgias", "Hipertension Arterial"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
     
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes
    
    assert Raul.Color == "Amarillo"
    assert not Raul.Color == "Naranja"
    
    assert Jose.Color == "Amarillo"
    assert not Jose.Color == "Verde"
    #chequeo colores
    
def test_PacienteVerde():
   
    Raul = Paciente("36421479","Raul","Perez",["Otalgias"])
    Jose = Paciente("46789915","Jose","Swaig",["Odontalgias", "Traumatismos"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
     
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes
    
    assert Raul.Color == "Verde"
    assert not Raul.Color == "Azul"
    
    assert Jose.Color == "Verde"
    assert not Jose.Color == "Rojo"
    #chequeo colores
    
def test_PacienteAzul():
   
    Raul = Paciente("36421479","Raul","Perez",["Nada"])
    Jose = Paciente("46789915","Jose","Swaig",["Resfrio", "Comezon en el brazo"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
     
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes
  
    assert Raul.Color == "Azul"
    assert not Raul.Color == "Verde"
    
    assert Jose.Color == "Azul"
    assert not Jose.Color == "Rojo"
    #chequeo colores