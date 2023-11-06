from library.LeerArchivo import LecturaArchivoSimulacion
import csv
from typing import List
from datetime import datetime
from library.cPaciente import Paciente
from library.cEnfermero import Enfermero
from library.cMedico import Medico
from library.fDC import CalculoTiempoRestante
from library.fDC import Binary_InsertionSort

def main():
  print("Hello World")
  '''
  Enfermero1 = Enfermero("57531189", "Silvio", "Mendex")
    
  Julio = Paciente("12564938", "Julio", "Doe", ["Resfrio"], "Azul", datetime(2023,11,3,16,40,1))
  Maria = Paciente("34784920", "Maria", "Smith", ["Vertigo Con Afectacion Vegetativa","Sincope"], "Amarillo",datetime(2023,11,3,18,40,1))
  Sofia = Paciente("54782464","Sofia Ana","Fleishman",["Esguinces"], "Verde", datetime(2023,11,3,18,15,1))
  Raul = Paciente("36421479","Raul","Perez",["No Respira"], "Rojo", datetime(2023,11,3,18,20,1))
  Pedro = Paciente("48902533","Pedro","Pascal",["Esguinces"], "Verde",datetime(2023,11,3,20,21,1))
  Malena = Paciente("46789915","Malena","Krupnik",["Sincope"],"Amarillo", datetime(2023,11,3,20,23,1))
  Jose = Paciente("46789915","Jose","Swaig",["Coma"],"Naranja", datetime(2023,11,3,20,23,5))

  ListaNoAtentidos = []
  
  ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Julio,ListaNoAtentidos) #se agrega julio a la lista. Esp hasta: 20:40
  ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Maria,ListaNoAtentidos)
  ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Sofia,ListaNoAtentidos)
  ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Raul,ListaNoAtentidos)
  ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Pedro,ListaNoAtentidos)
  ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Malena,ListaNoAtentidos)
  ListaNoAtentidos = Enfermero1.Asignar_Lugar_FilaDC(Jose,ListaNoAtentidos)

  
  print(CalculoTiempoRestante(ListaNoAtentidos[0]))
  print(ListaNoAtentidos[0].Nombre)
  print(CalculoTiempoRestante(ListaNoAtentidos[1]))
  print(ListaNoAtentidos[1].Nombre)
  print(CalculoTiempoRestante(ListaNoAtentidos[2]))
  print(ListaNoAtentidos[2].Nombre)
  print(CalculoTiempoRestante(ListaNoAtentidos[3]))
  print(ListaNoAtentidos[3].Nombre)
  print(CalculoTiempoRestante(ListaNoAtentidos[4]))
  print(ListaNoAtentidos[4].Nombre)
  print(CalculoTiempoRestante(ListaNoAtentidos[5]))
  print(ListaNoAtentidos[5].Nombre)
  print(CalculoTiempoRestante(ListaNoAtentidos[6]))
  print(ListaNoAtentidos[6].Nombre)
  '''
  
  '''hola = []
  hola = LecturaArchivoSimulacion()
  for paciente in hola:
    print(paciente.Nombre)
    print(paciente.Apellido)
    print(paciente.DNI)
  '''
    

if __name__== "__main__":
  main()