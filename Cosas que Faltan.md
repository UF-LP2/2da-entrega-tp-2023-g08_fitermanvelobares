
~Extras:
No Respira,Politraumatismo Grave,Coma,Convulsiones,Hemorragia Digestiva,Isquemia,Cefalea Brusca,Paresia,Hipertension Arterial,Vertigo Con Afectacion Vegetativa,Sincope,Urgencias Psiquiatricas,Otalgias,Odontalgias,Dolores Inespecíficos Leves,Traumatismos,Esguinces, hipo, resfrio, me duele el pie, piojos

interfaz, que se imprima a medida que se atienden los pacientes?


Funcion envejecer 
#actualizo los colores si lo que le queda de espera es igual o menor o lo de otro color
    if(pac.ColorP.Color == "Naranja" and tEsperaRestante<=5):
        pac.ColorP = Colores("Rojo")
    if(pac.ColorP.Color == "Amarillo" and tEsperaRestante<=10):
        pac.ColorP = Colores("Naranja")
    if(pac.ColorP.Color == "Verde" and tEsperaRestante<=60):
        pac.ColorP = Colores("Amarillo")
    if(pac.ColorP.Color == "Azul" and tEsperaRestante<=120):
        pac.ColorP = Colores("Verde")