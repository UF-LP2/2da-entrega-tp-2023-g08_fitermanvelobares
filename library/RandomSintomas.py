from library.Paciente import Paciente
from library.Enfermero import Enfermero
from typing import List
import random


def EnvejecerPacientes(ListaPacientes:List[Paciente]):
    SintomasPosibles = ["No Respira", "Politraumatismo Grave", "Coma", "Convulsiones", "Hemorragia Digestiva", 
                        "Isquemia", "Cefalea Brusca", "Paresia", "Hipertension Arterial", 
                        "Vertigo Con Afectacion Vegetativa","Sincope", "Urgencias Psiquiatricas", "Otalgias",
                        "Odontalgias", "Dolores Inespecíficos Leves", "Traumatismos", "Esguinces"]
    #^todos los sinotmas que puede tener el paciente
    
    enfermeroAux = Enfermero() #creo un enfermero
    
    CantidadRdn =  random.randint(0, len(ListaPacientes)-1) #decido cuantos pacientes experimentaron nuevos sintomas
    print("Pacientes envecejidos: " +str(CantidadRdn))
    
    for k in range(0,CantidadRdn):
        PosRandLista = random.sample(range(len(ListaPacientes)), 1)[0] #elijo al paciente en lista que le voy a cambiar los sintomas
        if (ListaPacientes[PosRandLista].ColorP.Color == "Naranja" or ListaPacientes[PosRandLista].ColorP.Color == "Rojo"):    
            AuxNuevoSintoma = random.randint(0,1) #Los sintomas rojos
        elif(ListaPacientes[PosRandLista].ColorP.Color == "Amarillo"):
            AuxNuevoSintoma = random.randint(0,5) #Los sintomas rojos y naranjas
        elif(ListaPacientes[PosRandLista].ColorP.Color == "Verde"): 
            AuxNuevoSintoma = random.randint(0,11) #Los sintomas rojos, naranjas y amarillos
        else: #es azul
            AuxNuevoSintoma = random.randint(0, len(SintomasPosibles)-1) #decido que sintoma nuevo tiene
            
        ListaPacientes[PosRandLista].Sintomas.insert(0,SintomasPosibles[AuxNuevoSintoma]) #le asigno el nuevo sintoma
        ListaPacientes[PosRandLista].Envejecido = True #lo marco como envejecido, asi mantiene el horario de triage anterior
        enfermeroAux.Asignar_Color_Paciente(ListaPacientes[PosRandLista]) #le vuelvo a asignar el color y tiempo de espera maximo
        
        print("El paciente: " + str(ListaPacientes[PosRandLista].Nombre) + " DNI: " +str(ListaPacientes[PosRandLista].DNI)+ " Cambio de sintomas")
        print("Color Nuevo del Paciente: "+ListaPacientes[PosRandLista].ColorP.Color)
    
        enfermeroAux.Asignar_Lugar_FilaDC(ListaPacientes[PosRandLista], ListaPacientes) #asigno nuevo lugar en la lista