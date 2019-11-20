# -*- coding: utf-8 -*-

"""
    El módulo genera aleatoriamente una lista de N países a partir de
    los 41 países que participaron, establecidos previamente.
"""


#metadata
__author__="Diego Lora"
__copyrihgt__="DLM"
__version__="v. 1.0"
__mail__="diego.lora@usil.pe"
__status__="Estudiante"


#funciones
def generarPaises(cant) :
    """ funcion que retorna una cantidad N de paises aleatoriamente de entre 41 """
    import random
    elegidos = []
    paises = ['Antigua y Barbuda', 'Argentina', 'Aruba', 'Bahamas', 'Barbados', 'Belize', 'Bermuda', 'Bolivia',
              'Brasil', 'Canadá', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominica', 'Ecuador', 'El Salvador',
              'Estados Unidos', 'Granada', 'Guatemala', 'Guyana', 'Haití', 'Honduras', 'Islas Caimán',
              'Islas Virgenes Británicas', 'Islas Vírgenes', 'Jamaica', 'México', 'Nicaragua', 'Panamá', 'Paraguay',
              'Perú', 'Puerto Rico', 'República Dominicana', 'San Cristobal y Nieves', 'San Vicente y las Granaditas',
              'Santa Lucía', 'Suriname', 'Trinidad y Tobago', 'Uruguay', 'Venezuela']

    while (len(elegidos) != cant) :
        indice = random.randint(0, 40)

        if not(paises[indice] in elegidos) :
            elegidos.append(paises[indice])

    elegidos.sort()

    return elegidos



def generarCantParticip(paisesComp) :
    """ funcion que retorna la cantidad de participantes de los paises elegidos """
    cantPart = []
    paises = ['Antigua y Barbuda','Argentina','Aruba','Bahamas','Barbados','Belize','Bermuda','Bolivia','Brasil','Islas Virgenes Británicas','Canadá', 'Islas Caimán','Chile','Colombia',
              'Costa Rica','Cuba','Dominica','República Dominicana','Ecuador','El Salvador','Granada','Guatemala','Guyana','Haití','Honduras','Jamaica','México', 'Nicaragua',
              'Panamá', 'Paraguay','Perú', 'Puerto Rico','Santa Lucía','San Cristobal y Nieves','San Vicente y las Granaditas','Suriname','Trinidad y Tobago','Estados Unidos','Uruguay', 'Venezuela','Islas Vírgenes']
    participantes = [9, 529, 21, 33, 31, 6, 17, 49, 487, 5, 477, 6, 317, 349,
                     84, 420, 2, 209, 201, 56, 11, 144, 26, 8, 44, 131, 543, 61,
                     83, 71, 592, 244, 7, 4, 4, 6, 98, 643, 147, 282, 30]

    cantPaises = len(paisesComp)

    for i in range(cantPaises) :
        pais = paisesComp[i]
        indice = paises.index(pais)
        part = participantes[indice]
        cantPart.append(part)
            
    return cantPart