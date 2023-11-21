from library.Paciente import Paciente
from typing import List
from datetime import datetime
from library.Colores import Colores
from library.DC import Binary_InsertionSort
import time
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
                    horario_actual = datetime.now()
                    Pac.HorarioTriage = horario_actual
                    break
                
                elif sintoma in ["Coma", "Convulsiones", "Hemorragia Digestiva", "Isquemia"]:
                    Pac.ColorP = Colores("Naranja")  
                    horario_actual = datetime.now()
                    Pac.HorarioTriage = horario_actual   
                    break
                
                elif sintoma in ["Cefalea Brusca", "Paresia", "Hipertension Arterial", "Vertigo Con Afectacion Vegetativa", "Sincope", "Urgencias Psiquiatricas"]:
                    Pac.ColorP = Colores("Amarillo")  
                    horario_actual = datetime.now()
                    Pac.HorarioTriage = horario_actual
                        
                elif sintoma in ["Otalgias", "Odontalgias", "Dolores Inespecíficos Leves", "Traumatismos", "Esguinces"] and Pac.ColorP.Color!= "Amarillo":
                    Pac.ColorP = Colores("Verde")  
                    horario_actual = datetime.now()
                    Pac.HorarioTriage = horario_actual
                        
                elif (Pac.ColorP.Color == "Blanco"):
                    Pac.ColorP = Colores("Azul") 
                    horario_actual = datetime.now()
                    Pac.HorarioTriage = horario_actual
            
        time.sleep(0.1) #simulamos que tarda en atender a los pacientes
   
    
            
    # break en rojo y naranja pq ya con un sintoma de ese color me basta para clasificarlos
    # con los otros sigo escuchando sus sintomas por si me los dijeron en desorden de prioridad

    def Asignar_Lugar_FilaDC(self, Pac: Paciente, NoAtendidos: List[Paciente]) -> None:
        if self.Disponible:
            if Pac not in NoAtendidos:  # Verificar si el paciente no está en la lista (puede que ya este y que sea uno de los pacientes que desarrollaron nuevos sintomas)
                NoAtendidos.append(Pac)  # Insertar Pac en la fila
            if Pac.ColorP.Color != "Azul":
                Binary_InsertionSort(NoAtendidos)  # Ordenar la fila si Pac no es azul
        return NoAtendidos