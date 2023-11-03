
class Colores:
    def __init__(self,Color="Blanco"):
        self.Color = Color
        if Color == "Rojo":
            self.TEspera = 0
        elif Color == "Naranja":
            self.TEspera = 10
        elif Color == "Amarillo":
            self.TEspera = 60
        elif Color == "Verde":
            self.TEspera = 120
        elif Color == "Azul":
            self.TEspera = 240
        else:
            self.TEspera = 300
        
        