# -*- coding: utf-8 -*-

"""
    El módulo genera aleatoriamente una lista de 10 países a partir de
    otros 41 predefinidos.
"""


#metadata
__author__="Diego Lora"
__copyrihgt__="Open source"
__version__="v. 1.0"
__mail__="diego.lora@usil.pe"
__status__="Estudiante"


#funciones
def randomPaises(cant) :
    """ funcion que retorna una cantidad N de paises aleatoriamente de entre 41 """
    import random
    elegidos = []
    participantes = ["Antigua y Barbuda", "Argentina", "Aruba", "Bahamas", "Barbados", "Belize", "Bermuda", "Bolivia", 
                     "Brasil", "Islas Virgenes Británicas", "Canadá", "Islas Caimán", "Chile", "Colombia", "Costa Rica",
                     "Cuba", "Dominica", "República Dominicana", "Ecuador", "El Salvador", "Granada", "Guatemala", "Guyana",
                     "Haití", "Honduras", "Jamaica", "México", "Nicaragua", "Panamá", "Paraguay", "Perú", "Puerto Rico",
                     "Santa Lucía", "San Cristobal y Nieves", "San Vicente y las Granaditas", "Suriname", "Trinidad y Tobago",
                     "Estados Unidos", "Uruguay", "Venezuela", "Islas Vírgenes"]

    while (len(elegidos) != cant) :
        indice = random.randint(0, 41)

        if not(partipantes[indice] in elegidos) :
            elegidos.append(participantes[index])

    return elegidos