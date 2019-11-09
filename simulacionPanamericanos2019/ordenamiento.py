# -*- coding: utf-8 -*-

"""
    El módulo ordena las listas según la categoría que se desee.
"""


#metadata
__author__="Diego Lora"
__copyrihgt__="Open source"
__version__="v. 1.0"
__mail__="diego.lora@usil.pe"
__status__="Estudiante"



#funciones
def bubbleOro(listaOro, listaPlt, listaBrz) :
    """ funcion que realiza Buble Sort y ordena las listas según la mayor cantidad de medallas de oro """
    cantDat = len(listaOro)
    for i in range(cantDat) :
        for j in range(cantDat) :
            if (listaOro[i]>listaOro[j]) :
                auxOro = listaOro[i]
                listaOro[i] = listaOro[j]
                listaOro[j] = auxOro

                auxPlt = listaPlt[i]
                listaPlt[i] = listaPlt[j]
                listaPlt[j] = auxPlt

                auxBrz = listaBrz[i]
                listaBrz[i] = listaBrz[j]
                listaBrz[j] = auxBrz



def bubblePlt(listaOro, listaPlt, listaBrz) :
    """ funcion que realiza Buble Sort y ordena las listas según la mayor cantidad de medallas de plata """
    cantDat = len(listaPlt)
    for i in range(cantDat) :
        for j in range(cantDat) :
            if (listaPlt[i]>listaPlt[j]) :
                auxOro = listaOro[i]
                listaOro[i] = listaOro[j]
                listaOro[j] = auxOro

                auxPlt = listaPlt[i]
                listaPlt[i] = listaPlt[j]
                listaPlt[j] = auxPlt

                auxBrz = listaBrz[i]
                listaBrz[i] = listaBrz[j]
                listaBrz[j] = auxBrz



def bubbleBrz(listaOro, listaPlt, listaBrz) :
    """ funcion que realiza Buble Sort y ordena las listas según la mayor cantidad de medallas de bronce """
    cantDat = len(listaBrz)
    for i in range(cantDat) :
        for j in range(cantDat) :
            if (listaBrz[i]>listaBrz[j]) :
                auxOro = listaOro[i]
                listaOro[i] = listaOro[j]
                listaOro[j] = auxOro

                auxPlt = listaPlt[i]
                listaPlt[i] = listaPlt[j]
                listaPlt[j] = auxPlt

                auxBrz = listaBrz[i]
                listaBrz[i] = listaBrz[j]
                listaBrz[j] = auxBrz




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