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
def rand(cant) :
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
        indice = random.randint(0, 41)

        if not(paises[indice] in elegidos) :
            elegidos.append(paises[indice])

    elegidos.sort()

    return elegidos
