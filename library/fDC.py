from library.cPaciente import Paciente
from datetime import datetime

def CalculoTiempoRestante(pac:Paciente):
    tEsperaPaciente = pac.HorarioTriage - datetime.now()

    minutos = tEsperaPaciente.total_seconds() / 60 #paso el tiempo de espera a minutos
    
    if(pac.ColorP.TEspera == 0):
        tEsperaRestante = 0    
    else:
        tEsperaRestante = pac.ColorP.TEspera - minutos
    #cuenta que da cantidad de minutos restante de espera maxima que tiene el paciente
    return tEsperaRestante
        

def Binary_Search(arr: list[Paciente], val, inicioLista, finLista): #funcion recursiva
        tEsperaIniLista = CalculoTiempoRestante(arr[inicioLista])
        
        #Si la lista tiene un solo elemento, me fijo si val es mayor o menor y ahi lo agrego
        if inicioLista == finLista:
            if tEsperaIniLista > val:
                return inicioLista
            else:
                return inicioLista+1
        #Caso base
            
        #Si el inicio es mas grande que el final --> se recorrio todo arr y no se encontro ningun valor menor a val
        if inicioLista > finLista:
            return inicioLista
        #Caso base
        
        #compara tiempos de espera y devuelve posicion en la que se debe insertar el paciente
        medio = (inicioLista+finLista)//2
        tEsperaMedio = CalculoTiempoRestante(arr[medio])
        
        if tEsperaMedio < val:
            return Binary_Search(arr,val,medio+1,finLista)
        elif tEsperaMedio > val:
            return Binary_Search(arr,val,inicioLista,medio-1)
        else:
            return medio
        

def InsercionBinaria(arr, pac: Paciente):
    tEsperaRestante = CalculoTiempoRestante(pac)
    i =  len(arr)
    j = Binary_Search(arr,tEsperaRestante,0,i-1)
    arr.insert(j,pac)  
    return arr

