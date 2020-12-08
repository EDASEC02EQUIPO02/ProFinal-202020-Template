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
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""
def newAnalyzer():
    try:
        citiTaxi = {
                    'graph': None,
                    'taxisId': None,
                    'companias': None,
                    'fecha': None}

        citiTaxi['graph'] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=1000,
                                  comparefunction=compareStations)
        citiTaxi['taxisId'] = lt.newList('SINGLE_LINKED', compareStations)
        citiTaxi['companias'] = m.newMap(numelementes=17, prime=109345121, maptype="CHAINING", loadfactor=1, comparefunction=None)
        citiTaxi['fecha'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)

    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')





# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo

def addTaxi(citiTaxi, taxi):
    """
    """
    compania=taxi["company"]
    taxiid=taxi["taxi_id"]
    if lt.isPresent(citiTaxi["taxisId"], taxiid)==0:
        lt.addLast(citiTaxi["taxisId"], taxiid)
    añadir_compañia(citiTaxi, taxi, compania)
    updateDateIndex(citiTaxi['fecha'], taxi)
    return citiTaxi


def añadir_compañia(citiTaxi, taxi, compania):
    """
    Añade el nombre de una compañia a la tabla de Hash para compañias en el catalogo
    """

    if mp.contains(citiTaxi["compania"], compania) == True:
        n = mp.get(citiTaxi["compania"], compania)
        dic["cantidad"]+=1
        if lt.isPresent(citiTaxi["taxisId"], taxiid)==0:
            lt.addLast(dic["taxis"], taxi["taxi_id"])
    else:
        dic={}
        N = lt.newList("SINGLED_LINKED")
        lt.addLast(N, taxi["taxi_id"])
        dic["nombre"]=compania
        dic["taxis"]=N
        dic["cantidad"]=1
        mp.put(citiTaxi["compania"], compania, dic)


# ==============================
# Arbol de fechas
# ==============================

def updateDateIndex(map, taxi):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = taxi['Start_Time']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, crimedate.date())
    if entry is None:
        datentry = newDataEntry(taxi)
        om.put(map, crimedate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    lst = datentry['lstcrimes']
    lt.addLast(lst, taxi)
    return map


# Funciones para agregar informacion al grafo

# ==============================
# Funciones de consulta
# ==============================


# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================


def compareStations(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1