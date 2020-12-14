"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config as cf
from App import model
import csv
from time import process_time
import datetime
"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def init():
    """
    Llama la funcion de inicializacion del modelo.
    """
    analyzer = model.newAnalyzer()
    return analyzer


def loadData(analyzer, taxisfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    t1 = process_time()
    taxisfile = cf.data_dir + taxisfile
    input_file = csv.DictReader(open(taxisfile, encoding="utf-8"), delimiter=",")
    for taxi in input_file:
        model.addTaxi(analyzer, taxi)
    t2  = process_time()
    print("El tiempo de procesamiento es de: ", t2 - t1)
    return analyzer
# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def getCantidadTaxis(citiTaxi, N):
    return model.getCantidadTaxis(citiTaxi, N)


def getPointsbydate(analyzer, initialDate, cant):
    """
    Retorna el total de crimenes en un rango de fechas
    """
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    return model.getPointsbydate(analyzer, initialDate.date(), cant)

def getPointsbyrange(citiTaxi, initialDate, finalDate, N):
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d').date()
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d').date()
    return model.getPointsbyRange(citiTaxi, initialDate, finalDate, N)


def Shortway(citiTaxi, origin, destination, HoI, HoF):
    horai = datetime.datetime.strptime(HoI, '%H:%M').time()
    horaf = datetime.datetime.strptime(HoF, '%H:%M').time()
    return model.Shortestway(citiTaxi, origin, destination, horai, horaf)



"""funciones consultas de Arboles"""

def crimesSize(analyzer):
    return model.crimesSize(analyzer)


def indexHeight(analyzer):
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    return model.indexSize(analyzer)


def minKey(analyzer):
    return model.minKey(analyzer)


def maxKey(analyzer):
    return model.maxKey(analyzer)

