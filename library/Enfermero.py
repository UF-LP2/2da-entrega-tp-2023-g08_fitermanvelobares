from library.Paciente import Paciente

class Enfermero:
    def __init__(self, DNI: str, Nombre: str, Apellido: str):
        self.DNI = DNI
        self.Nombre = Nombre
        self.Apellido = Apellido
        
                
    def Asignar_Color_Paciente(self, Pac: Paciente) -> None:
            for sintoma in Pac.Sintomas:
                if sintoma in ["No Respira", "Politraumatismo Grave"]:
                    Pac.Color = "Rojo"
                    break
                elif sintoma in ["Coma", "Convulsiones", "Hemorragia Digestiva", "Isquemia"]:
                    Pac.Color = "Naranja"
                    break
                elif sintoma in ["Cefalea Brusca", "Paresia", "Hipertension Arterial", "Vertigo Con Afectacion Vegetativa", "Sincope", "Urgencias Psiquiatricas"]:
                    Pac.Color = "Amarillo"
                elif sintoma in ["Otalgias", "Odontalgias", "Dolores Inespecíficos Leves", "Traumatismos", "Esguinces"]:
                    Pac.Color = "Verde"
                else:
                    Pac.Color = "Azul"
   
# break en rojo y naranja pq ya con un sintoma de ese color me basta para clasificarlos
# con los otros sigo escuchando sus sintomas por si me los dijeron en desorden de prioridad