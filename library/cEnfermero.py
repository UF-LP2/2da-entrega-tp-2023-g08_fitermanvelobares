from library.cPaciente import Paciente
from typing import List
from datetime import datetime
from library.cColores import Colores
from library.fDC import Binary_InsertionSort
class Enfermero:
    def __init__(self, Disponible = True, DNI = "00000000", Nombre= "John", Apellido = "Doe"):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Disponible = Disponible
                
    def Asignar_Color_Paciente(self, Pac: Paciente) -> None:
            if(self.Disponible == True):
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
        if(self.Disponible == True):
            NoAtendidos.append(Pac) #inserto Pac en la fila
            if(Pac.ColorP.Color != "Azul"):
                Binary_InsertionSort(NoAtendidos) #ordeno la fila si Pac no es azul (si es azul esta ok al final de la fila)
            return NoAtendidos            