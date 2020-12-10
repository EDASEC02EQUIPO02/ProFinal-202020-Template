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
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""
def newAnalyzer():
    citiTaxi = {
                    'graph': None,
                    'taxisId': None,
                    'companias': None,
                    'fecha': None}

    citiTaxi['graph'] = gr.newGraph(datastructure='ADJ_LIST',
                                  directed=True,
                                  size=1000,
                                  comparefunction=compareStations)
    #citiTaxi['taxisId'] = lt.newList('SINGLE_LINKED')
    citiTaxi['taxisId'] = []
    citiTaxi['companias'] = m.newMap(numelements=17, prime=109345121, maptype="CHAINING", loadfactor=1, comparefunction=None)
    citiTaxi['fecha'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    return citiTaxi





# -----------------------------------------------------
#                       API
# -----------------------------------------------------

# Funciones para agregar informacion al grafo

def addTaxi(citiTaxi, taxi):
    """
    """
    compania=taxi["company"]
    taxiid=str(taxi["taxi_id"])
    if taxiid not in citiTaxi['taxisId']:
        citiTaxi['taxisId'].append(taxiid)
    #print(lt.size(citiTaxi['taxisId']))
    #if lt.isPresent(citiTaxi["taxisId"], taxiid)==0:
        #lt.addLast(citiTaxi["taxisId"], taxiid)
    #añadir_compañia(citiTaxi, taxi, compania)
    updateDateIndex(citiTaxi['fecha'], taxi)
    return citiTaxi


def añadir_compañia(citiTaxi, taxi, compania):
    """
    Añade el nombre de una compañia a la tabla de Hash para compañias en el catalogo
    """
    print(compania)
    if m.contains(citiTaxi["companias"], compania) == True:
        n = m.get(citiTaxi["companias"], compania)
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
        m.put(citiTaxi["companias"], compania, dic)


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
    occurreddate = taxi['trip_start_timestamp']
    crimedate = datetime.datetime.strptime(occurreddate, '%Y-%m-%dT%H:%M:%S.%f')
    entry = om.get(map, crimedate.date())
    if entry is None:
        dicc = {}
        datentry = newDataEntry(taxi)
        dicc[taxi['taxi_id']] = datentry
        om.put(map, crimedate.date(), dicc)
    else:
        diccio = me.getValue(entry)
        if taxi['taxi_id'] not in diccio:
            datentry = newDataEntry(taxi)
            diccio[taxi['taxi_id']] = datentry
        else:
            dic = diccio[taxi['taxi_id']]
            a = taxi['trip_miles']
            if a == '':
                a = 0
            dic['millas'] += float(a)
            c = taxi['trip_total']
            if c == '':
                c = 0
            dic['dinero'] = float(c)
            dic['servicios'] += 1
    return map

def newDataEntry(taxi):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'millas': None, 'dinero': None, 'servicios': None}
    entry['millas'] = float(taxi['trip_miles'])
    c = taxi['trip_total']
    if c == '':
        c = 0
    entry['dinero'] = float(c)
    entry['servicios'] = 1

    return entry


# Funciones para agregar informacion al grafo

# ==============================
# Funciones de consulta
# ==============================



"""Consultas para Arboles"""
def crimesSize(analyzer):
    return lt.size(analyzer['accidents'])


def indexHeight(analyzer):
    return om.height(analyzer['fecha'])


def indexSize(analyzer):
    return om.size(analyzer['fecha'])


def minKey(analyzer):
    return om.minKey(analyzer['fecha'])


def maxKey(analyzer):
    return om.maxKey(analyzer['fecha'])




# ==============================
# Funciones Ejercicios
# ==============================


"""REQ B"""
def getPointsbydate(analyzer, initialDate, N):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    dicc = {}
    llave = om.get(analyzer['fecha'], initialDate)
    entry = me.getValue(llave)
    for i in entry:
        dinero = entry[i]['dinero']
        if dinero != 0.0:
            milla = entry[i]['millas']
            servicio = entry[i]['servicios']
            formula = (milla/dinero)*servicio
            dicc[i] = formula
    mayores(dicc, N)

    

def mayores(dicc, N):
    lista = []
    lista2 = []
    for i in dicc:
        lista.append(dicc[i])
    new = sorted(lista, reverse=True)
    for i in range(0, N):
        dato = new[i]
        lista2.append(dato)
    for i in range(0,N):
        print("Para el taxi: " + str(lista2[i])+ " sus puntos son: " + str(lista[i]))
        print("\n")




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

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 != id2:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1