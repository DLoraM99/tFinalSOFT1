# -*- coding: utf-8 -*-

"""
    El módulo ordena las listas de medallas según la categoría
    (oro, plata o bronce) que se desee, de mayor a menor.
"""


#metadata
__author__="Diego Lora"
__copyrihgt__="DLM"
__version__="v. 1.2"
__mail__="diego.lora@usil.pe"
__status__="Estudiante"



#funciones
def bubbleOro(paises, particip, listaOro, listaPlt, listaBrz, totalMed) :
    """ funcion que realiza BubleSort y ordena las listas según la mayor cantidad de medallas de oro """
    cantDat = len(listaOro)
    for i in range(cantDat) :
        for j in range(cantDat) :
            if (listaOro[i]>listaOro[j]) :
                auxPais = paises[i]
                paises[i] = paises[j]
                paises[j] = auxPais
                
                auxParticip = particip[i]
                particip[i] = particip[j]
                particip[j] = auxParticip

                auxOro = listaOro[i]
                listaOro[i] = listaOro[j]
                listaOro[j] = auxOro

                auxPlt = listaPlt[i]
                listaPlt[i] = listaPlt[j]
                listaPlt[j] = auxPlt

                auxBrz = listaBrz[i]
                listaBrz[i] = listaBrz[j]
                listaBrz[j] = auxBrz

                auxMed = totalMed[i]
                totalMed[i] = totalMed[j]
                totalMed[j] = auxMed



def bubblePlt(paises, particip, listaOro, listaPlt, listaBrz, totalMed) :
    """ funcion que realiza BubleSort y ordena las listas según la mayor cantidad de medallas de plata """
    cantDat = len(listaPlt)
    for i in range(cantDat) :
        for j in range(cantDat) :
            if (listaPlt[i]>listaPlt[j]) :
                auxPais = paises[i]
                paises[i] = paises[j]
                paises[j] = auxPais
                
                auxParticip = particip[i]
                particip[i] = particip[j]
                particip[j] = auxParticip

                auxOro = listaOro[i]
                listaOro[i] = listaOro[j]
                listaOro[j] = auxOro

                auxPlt = listaPlt[i]
                listaPlt[i] = listaPlt[j]
                listaPlt[j] = auxPlt

                auxBrz = listaBrz[i]
                listaBrz[i] = listaBrz[j]
                listaBrz[j] = auxBrz

                auxMed = totalMed[i]
                totalMed[i] = totalMed[j]
                totalMed[j] = auxMed



def bubbleBrz(paises, particip, listaOro, listaPlt, listaBrz, totalMed) :
    """ funcion que realiza BubleSort y ordena las listas según la mayor cantidad de medallas de bronce """
    cantDat = len(listaBrz)
    for i in range(cantDat) :
        for j in range(cantDat) :
            if (listaBrz[i]>listaBrz[j]) :
                auxPais = paises[i]
                paises[i] = paises[j]
                paises[j] = auxPais
                
                auxParticip = particip[i]
                particip[i] = particip[j]
                particip[j] = auxParticip

                auxOro = listaOro[i]
                listaOro[i] = listaOro[j]
                listaOro[j] = auxOro

                auxPlt = listaPlt[i]
                listaPlt[i] = listaPlt[j]
                listaPlt[j] = auxPlt

                auxBrz = listaBrz[i]
                listaBrz[i] = listaBrz[j]
                listaBrz[j] = auxBrz

                auxMed = totalMed[i]
                totalMed[i] = totalMed[j]
                totalMed[j] = auxMed




 #CODIGO PASCAL <3
 #begin
  #{ORDENAMIENTO POR INTERCAMBIO}
  #for i:=1 to numDat-1 do begin
    #for j:=i+1 to numDat do begin
      #if algo[i]>algo[j] then begin
        #auxAlgo := algo[i];
        #algo[i] := algo[j];
        #algo[j] := auxAlgo;
      #end;
    #end;
  #end;
 #end;
