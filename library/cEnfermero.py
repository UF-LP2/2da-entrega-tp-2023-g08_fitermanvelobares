from library.cPaciente import Paciente
from typing import List
from datetime import datetime
from library.cColores import Colores
from library.fDC import Binary_Search
from library.fDC import InsercionBinaria
class Enfermero:
    def __init__(self, DNI: str, Nombre: str, Apellido: str):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        
                
    def Asignar_Color_Paciente(self, Pac: Paciente) -> None:
            for sintoma in Pac.Sintomas:
                if sintoma in ["No Respira", "Politraumatismo Grave"]:
                    Pac.ColorP = Colores("Rojo")  
                    Pac.HorarioAtendido = datetime.now()
                    break
                elif sintoma in ["Coma", "Convulsiones", "Hemorragia Digestiva", "Isquemia"]:
                    Pac.ColorP = Colores("Naranja")  
                    Pac.HorarioAtendido = datetime.now()
                    break
                elif sintoma in ["Cefalea Brusca", "Paresia", "Hipertension Arterial", "Vertigo Con Afectacion Vegetativa", "Sincope", "Urgencias Psiquiatricas"]:
                    Pac.ColorP = Colores("Amarillo")  
                elif sintoma in ["Otalgias", "Odontalgias", "Dolores Inespecíficos Leves", "Traumatismos", "Esguinces"] and Pac.ColorP.Color!= "Amarillo":
                    Pac.ColorP = Colores("Verde")  
                    Pac.HorarioAtendido = datetime.now()
                elif (Pac.ColorP.Color == "Blanco"):
                    Pac.ColorP = Colores("Azul") 
                    Pac.HorarioAtendido = datetime.now()
            
    # break en rojo y naranja pq ya con un sintoma de ese color me basta para clasificarlos
    # con los otros sigo escuchando sus sintomas por si me los dijeron en desorden de prioridad
    
    def Asignar_Lugar_FilaDC(self, Pac: Paciente, NoAtendidos: List[Paciente]) -> None:
        i = 0
        if(Pac.ColorP.Color == "Rojo"):
            while(i < len(NoAtendidos) and NoAtendidos[i].ColorP.Color == "Rojo"):
                i += 1 #busco el ultimo paciente rojo en la fila
            NoAtendidos.insert(i,Pac) #inserto el pac desp del ultimo rojo
            
        elif(Pac.ColorP.Color == "Naranja"):
            while(i < len(NoAtendidos) and (NoAtendidos[i].ColorP.Color == "Rojo" or NoAtendidos[i].ColorP.Color == "Naranja")):
                i += 1 #busco el ultimo paciente naranja en la fila
            NoAtendidos.insert(i,Pac) #inserto el pac desp del ultimo naranja
            
        elif(Pac.ColorP.Color == "Amarillo" or Pac.ColorP.Color == "Verde"):
            #Divide and conquer
            NoAtendidos = InsercionBinaria(NoAtendidos, Pac)

        else: #es azul
            NoAtendidos.append(Pac) #si es azul, lo agrego al final de la lista
        return NoAtendidos

    def Asignar_Lugar_FilaV(self, Pac: Paciente, NoAtendidos: List[Paciente]) -> None:
        i:int = 0
        aux:int = 0  
    
        if(Pac.ColorP.Color == "Azul"):
            aux=len(NoAtendidos) #si es azul va al final de la lista
        else:
            while(i< len(NoAtendidos)): #si el paciente que quiero insertar no es azul recorro la lista
                if(Pac.ColorP.Color == NoAtendidos[i].ColorP.Color): #si el que quiero insertar es del mismo color que el de la lista
                    aux = i
                i+=1        
        NoAtendidos.insert(aux+1,Pac)   
 
 #No chequea ningun otro color que no sea el mismo del paciente por que es voraz y no le importa
 #No respeta prioridad. Si por ej, no hay ningun naranja ya en la fila se inserta en la posicion [i]
