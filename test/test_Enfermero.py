from library.cPaciente import Paciente
from library.cEnfermero import Enfermero
from library.cColores import Colores
import pytest

def test_PacienteRojo():
   
    Raul = Paciente("36421479","Raul","Perez",["No Respira"])
    Jose = Paciente("46789915","Jose","Swaig",["Otalgias", "Politraumatismo Grave"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
    
    Enfermero1.Asignar_Color_Paciente(Raul)
    Enfermero1.Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes
    
    assert Raul.ColorP.Color == "Rojo"
    assert not Raul.ColorP.Color == "Azul"
    assert Raul.ColorP.TEspera == 0
    
    assert Jose.ColorP.Color == "Rojo"
    assert not Jose.ColorP.Color == "Verde"
    assert Jose.ColorP.TEspera == 0
    #chequeo colores
    

def test_PacienteNaranja():
   
    Raul = Paciente("36421479","Raul","Perez",["Coma"])
    Jose = Paciente("46789915","Jose","Swaig",["Otalgias", "Convulsiones"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
     
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes

    assert Raul.ColorP.Color== "Naranja"
    assert not Raul.ColorP.Color == "Azul"
    assert Raul.ColorP.TEspera == 10
    
    assert Jose.ColorP.Color == "Naranja"
    assert not Jose.ColorP.Color == "Verde"
    assert Jose.ColorP.TEspera == 10
    #chequeo colores

def test_PacienteAmarillo() -> None:
   
    Raul = Paciente("36421479","Raul","Perez",["Cefalea Brusca"])
    Jose = Paciente("46789915","Jose","Swaig",["Otalgias", "Hipertension Arterial"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
     
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes
    
    assert Raul.ColorP.Color == "Amarillo"
    assert not Raul.ColorP.Color == "Naranja"
    assert Raul.ColorP.TEspera == 60
    
    assert Jose.ColorP.Color == "Amarillo"
    assert not Jose.ColorP.Color == "Verde"
    assert Jose.ColorP.TEspera == 60
    #chequeo colores
    
def test_PacienteVerde():
   
    Raul = Paciente("36421479","Raul","Perez",["Otalgias"])
    Jose = Paciente("46789915","Jose","Swaig",["Odontalgias", "Traumatismos"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
     
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes
    
    assert Raul.ColorP.Color == "Verde"
    assert not Raul.ColorP.Color == "Azul"
    assert Raul.ColorP.TEspera == 120
    
    assert Jose.ColorP.Color == "Verde"
    assert not Jose.ColorP.Color == "Rojo"
    assert Jose.ColorP.TEspera == 120
    #chequeo colores
    
def test_PacienteAzul():
   
    Raul = Paciente("36421479","Raul","Perez",["Nada"])
    Jose = Paciente("46789915","Jose","Swaig",["Resfrio", "Comezon en el brazo"])
    Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    #creo pacientes y enfermero
     
    Enfermero1. Asignar_Color_Paciente(Raul)
    Enfermero1. Asignar_Color_Paciente(Jose)
    #enfermero asigna colores a los pacientes
  
    assert Raul.ColorP.Color == "Azul"
    assert not Raul.ColorP.Color == "Verde"
    assert Raul.ColorP.TEspera == 240
    
    assert Jose.ColorP.Color == "Azul"
    assert not Jose.ColorP.Color == "Rojo"
    assert Jose.ColorP.TEspera == 240

    #chequeo colores