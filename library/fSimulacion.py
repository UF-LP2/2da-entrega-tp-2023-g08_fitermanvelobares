from library.cEnfermero import Enfermero
from library.cPaciente import Paciente
from library.cMedico import Medico
import random
from typing import List
from library.fDC import CalculoTiempoRestante
from datetime import datetime


def Simulacion(arr:list[Paciente], CantidadPacientes, ListaSimulacion: list[Paciente]):        
    Horario = datetime.now().hour #me importa solo la hora pasa saber cuantos enfermeros tengo
    print("Son las: " + str(Horario) + " hs")
    print("Atiendo a: " + str(CantidadPacientes) + " pacientes")
        
    Med1 = Medico()
    #creo los medicos que van a atender los pacientes. La cantidad es simbolica ya que no se esta ejecutando en paralelo
    #por eso creamos uno solo y lo llamamos en un bucle
    
    Enfermero1 = Enfermero() #siempre hay un enfermero atendiendo
    Enfermero2 = Enfermero(False) 
    Enfermero3 = Enfermero(False) 
    Enfermero4 = Enfermero(False) 
    Enfermero5 = Enfermero(False) 
    if 6 < Horario <= 10:
        Enfermero2.Disponible = True 
        print("2 enfermeros disponibles")
    elif 10 < Horario <= 16:
        Enfermero2.Disponible = True 
        Enfermero3.Disponible = True 
        Enfermero4.Disponible = True 
        Enfermero5.Disponible = True 
        print("5 enfermeros disponibles")
    elif 16 < Horario <= 23:   
        Enfermero2.Disponible = True 
        Enfermero3.Disponible = True 
        print("3 enfermeros disponibles")
    else:
        print("1 enfermero disponible")
    #^Cantidad de enfermeros disponibles segun el horario
    
    i = 0
    while i < CantidadPacientes: #asigno colores y lugar fila
        Enfermero1.Asignar_Color_Paciente(arr[i])
        Enfermero1.Asignar_Lugar_FilaDC(arr[i],ListaSimulacion)
        print("Triage x Enf1 a: " + str(arr[i].Nombre) + " DNI: " +str(arr[i].DNI))
        print("Color: "+arr[i].ColorP.Color)
        i= i+1
        
        if Enfermero2.Disponible == True and i < CantidadPacientes: 
            Enfermero2.Asignar_Color_Paciente(arr[i])
            Enfermero2.Asignar_Lugar_FilaDC(arr[i],ListaSimulacion)
            print("Triage x Enf2 a: " + str(arr[i].Nombre) + " DNI: " +str(arr[i].DNI))
            print("Color: "+arr[i].ColorP.Color)
            i = i+1

        #Si se asigno el color y lugar a un paciente, paso a la siguiente poscicion en la lista
        
        if Enfermero3.Disponible == True and i < CantidadPacientes: 
            Enfermero3.Asignar_Color_Paciente(arr[i])
            Enfermero3.Asignar_Lugar_FilaDC(arr[i],ListaSimulacion)
            print("Triage x Enf3 a: " + str(arr[i].Nombre) + " DNI: " +str(arr[i].DNI))
            print("Color: "+arr[i].ColorP.Color)
            i = i+1
        
        if Enfermero4.Disponible == True and i < CantidadPacientes: 
            Enfermero4.Asignar_Color_Paciente(arr[i])
            Enfermero4.Asignar_Lugar_FilaDC(arr[i],ListaSimulacion)
            print("Triage x Enf4 a: " + str(arr[i].Nombre) + " DNI: " +str(arr[i].DNI))
            print("Color: "+arr[i].ColorP.Color)
            i = i+1
    
            
        if Enfermero5.Disponible == True and i < CantidadPacientes: 
            Enfermero5.Asignar_Color_Paciente(arr[i])
            Enfermero5.Asignar_Lugar_FilaDC(arr[i],ListaSimulacion)
            print("Triage x Enf5 a: " + str(arr[i].Nombre) + " DNI: " +str(arr[i].DNI))
            print("Color: "+arr[i].ColorP.Color)
            i = i+1   

    #imprimo lista 
    print("Lista de pacientes: ")
    for paciente in ListaSimulacion:
        print(paciente.Nombre)
        print(paciente.Apellido)
        print(paciente.DNI)
        print(paciente.ColorP.Color)
        print("tiempo maximo de espera restante para el paciente en minutoss: "+ str(CalculoTiempoRestante(paciente)))
        print("\n")

    auxLista = len(ListaSimulacion)
    auxLista2=auxLista
    i = 0  # Inicializa el índice en 0

    ContVivos = 0
    ContMuertos = 0
    while i < auxLista:
        paciente_actual = ListaSimulacion[i]  # Obtiene el paciente actual
        print("Atendiendo a: " + str(paciente_actual.Nombre) + " DNI: " + str(paciente_actual.DNI))
        Med1.Atender_Paciente(ListaSimulacion)
        print("Esta Vivo o muerto?: ", end=" ") # el end= para que vivo o muerto se imprima en el mismo renglon
        if paciente_actual.Vivo:
            print("Vivo")
            ContVivos = ContVivos +1
        else:
            print("Muerto")
            ContMuertos = ContMuertos +1
        auxLista = len(ListaSimulacion)  # Actualiza la longitud de la lista
    
    print("Pacientes que fallecieron: "+str(ContMuertos)) 
    print("Pacientes que siguen vivos: "+str(ContVivos)) 
    print("Lista de pacientes post atender:\n")
    
    
    if len(ListaSimulacion)>0:
        for j in range(0,auxLista2):
            print(ListaSimulacion[j].Nombre)
            print(ListaSimulacion[j].Apellido)
            print(ListaSimulacion[j].DNI)
            print("\n")
    else:
        print("ya se atendieron todos los pacientes!")
