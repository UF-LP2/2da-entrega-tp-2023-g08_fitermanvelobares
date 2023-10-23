from library.Paciente import Paciente
from typing import List
from datetime import datetime
class Enfermero:
    def __init__(self, DNI: str, Nombre: str, Apellido: str):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        
                
    def Asignar_Color_Paciente(self, Pac: Paciente) -> None:
            for sintoma in Pac.Sintomas:
                if sintoma in ["No Respira", "Politraumatismo Grave"]:
                    Pac.Color = "Rojo"
                    Pac.HorarioAtendido = datetime.now()
                    break
                elif sintoma in ["Coma", "Convulsiones", "Hemorragia Digestiva", "Isquemia"]:
                    Pac.Color = "Naranja"
                    Pac.HorarioAtendido = datetime.now()
                    break
                elif sintoma in ["Cefalea Brusca", "Paresia", "Hipertension Arterial", "Vertigo Con Afectacion Vegetativa", "Sincope", "Urgencias Psiquiatricas"]:
                    Pac.Color = "Amarillo"
                elif sintoma in ["Otalgias", "Odontalgias", "Dolores Inespecíficos Leves", "Traumatismos", "Esguinces"]:
                    Pac.Color = "Verde"
                    Pac.HorarioAtendido = datetime.now()
                else:
                    Pac.Color = "Azul"
                    Pac.HorarioAtendido = datetime.now()
    
            
    # break en rojo y naranja pq ya con un sintoma de ese color me basta para clasificarlos
    # con los otros sigo escuchando sus sintomas por si me los dijeron en desorden de prioridad
    
    def Asignar_Lugar_FilaDC(self, Pac: Paciente, NoAtendidos: List[Paciente]) -> None:
        i = 0
        if(Pac.Color == "Rojo"):
            while(i < len(NoAtendidos) and NoAtendidos[i].Color == "Rojo"):
                i += 1 #busco el ultimo paciente rojo en la fila
            NoAtendidos.insert(i,Pac) #inserto el pac desp del ultimo rojo
            
        elif(Pac.Color == "Naranja"):
            while(i < len(NoAtendidos) and (NoAtendidos[i].Color == "Rojo" or NoAtendidos[i].Color == "Naranja")):
                i += 1 #busco el ultimo paciente naranja en la fila
            NoAtendidos.insert(i,Pac) #inserto el pac desp del ultimo naranja
            
        elif(Pac.Color == "Amarillo"):
            #Divide and conquer
            hola=3
            
        elif(Pac.Color == "Verde"):
            #Divide and conquer
            hola=3
            
        else: #es azul
            NoAtendidos.append(Pac) #si es azul, lo agrego al final de la lista
        

    def Asignar_Lugar_FilaV(self, Pac: Paciente, NoAtendidos: List[Paciente]) -> None:
        i:int = 0
        aux:int = 0  
    
        if(Pac.Color == "Azul"):
            aux=len(NoAtendidos)
        else:
            while(i< len(NoAtendidos)): #si el paciente que quiero insertar no es azul recorro la lista
                if(Pac.Color == NoAtendidos[i].Color): #si el que quiero insertar es del mismo color que el de la lista
                    aux = i
                i+=1        
        NoAtendidos.insert(aux+1,Pac)   
 
 #No chequea ningun otro color que no sea el mismo del paciente por que es voraz y no le importa
 #No respeta prioridad. Si por ej, no hay ningun naranja ya en la fila, pero si rojos, el naranja se inserta antes que los rojos (pasa con todos los colores)
