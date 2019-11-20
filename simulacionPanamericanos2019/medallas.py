# -*- coding: utf-8 -*-

"""
    El módulo genera aleatoriamente las medallas para la cantidad de paises
    generados.
"""


#metadata
__author__="Diego Lora"
__copyrihgt__="DLM"
__version__="v. 1.0"
__mail__="diego.lora@usil.pe"
__status__="Estudiante"


#funciones
def generarMedallas(paises, participantes) :
    """ funcion que retorna el total de medallas de los N países participantes """
    import random
    medallas = []
    oro = []
    plata = []
    bronce = []
    totalMed = []

    cantPaises = len(paises)

    for i in range(cantPaises) :
        cantOro = 0
        cantPlata = 0
        cantBronce = 0
        total = 0

        for j in range(participantes[i]) :
            result = random.randint(0, 1)

            if (result==1) :
                result = random.randint(0, 3)

                if (result==1) :
                    cantOro = cantOro + 1

                elif (result==2) :
                    cantPlata = cantPlata + 1

                elif (result==3) :
                    cantBronce = cantBronce + 1

        total = cantOro + cantPlata + cantBronce

        oro.append(cantOro)
        plata.append(cantPlata)
        bronce.append(cantBronce)
        totalMed.append(total)

    
    medallas.append(oro)
    medallas.append(plata)
    medallas.append(bronce)
    medallas.append(totalMed)

    return medallas