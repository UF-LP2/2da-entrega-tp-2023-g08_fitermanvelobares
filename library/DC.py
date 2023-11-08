from library.Paciente import Paciente
from datetime import datetime
from library.Colores import Colores

def CalculoTiempoRestante(pac:Paciente):
    tEsperaPaciente = datetime.now() - pac.HorarioTriage

    minutos_transcurridos = tEsperaPaciente.total_seconds() / 60 #paso el tiempo de espera a minutos
    
    tiempo_maximo_espera = pac.ColorP.TEspera  # tiempo máximo de espera del paciente
    tEsperaRestante = tiempo_maximo_espera - minutos_transcurridos  # diferencia en minutos
    
    #actualizo los colores si lo que le queda de espera es igual o menor o lo de otro color
    if(pac.ColorP.Color == "Naranja" and tEsperaRestante<=5):
        pac.ColorP = Colores("Rojo")
    if(pac.ColorP.Color == "Amarillo" and tEsperaRestante<=10):
        pac.ColorP = Colores("Naranja")
    if(pac.ColorP.Color == "Verde" and tEsperaRestante<=60):
        pac.ColorP = Colores("Amarillo")
    if(pac.ColorP.Color == "Azul" and tEsperaRestante<=120):
        pac.ColorP = Colores("Verde")
        
        
    return tEsperaRestante
        

def Binary_Search(arr: list[Paciente], val, inicioLista, finLista): #funcion recursiva
    tEsperaIniLista = CalculoTiempoRestante(arr[inicioLista])
        
    if ((finLista-inicioLista) <= 1):
        if (val < tEsperaIniLista):
                return inicioLista - 1
        else:
            return inicioLista
    #Caso base
    #Si la lista tiene un solo elemento, me fijo si val es mayor o menor y ahi lo agrego
        
    #compara tiempos de espera y devuelve posicion en la que se debe insertar el paciente
    medio = (inicioLista + finLista)//2
    tEsperaMedio = CalculoTiempoRestante(arr[medio])
        
    if tEsperaMedio < val:
        return Binary_Search(arr,val,medio,finLista)
    elif tEsperaMedio > val:
        return Binary_Search(arr,val,inicioLista,medio)
    else:
        return medio

def Binary_InsertionSort(arr: list[Paciente]):
    for i in range(1,len(arr)):
        tempTiempo = CalculoTiempoRestante(arr[i])
        temp = arr[i]
        pos = Binary_Search(arr,tempTiempo,0,i) + 1

        for k in range(i,pos,-1):
            arr[k]=arr[k-1]
        
        arr[pos] = temp
            
