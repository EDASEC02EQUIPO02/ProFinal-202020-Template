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


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
from DISClib.ADT.graph import gr
from time import process_time
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("\n")
    print("**")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de taxis")
    print("3- Datos cargados ")
    print("4- Requerimento A")
    print("5- Requerimento B")
    print("6- Requerimento C")
    print("0- Salir")
    print("**")


large = "Taxi_Trips-2020-subset-large.csv"
medium = "Taxi_Trips-2020-subset-medium.csv"
small = "Taxi_Trips-2020-subset-small.csv"



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()
    elif int(inputs[0]) == 2:
        pregunta = input("Que archivo desea cargar? (small, medium, large): ")
        if pregunta == "small":
            controller.loadData(cont, small)
        if pregunta == "medium":
            controller.loadData(cont, medium)
        if pregunta == "large":
            controller.loadData(cont, large)
    elif int(inputs[0]) == 3:
        pregunta = int(input("Qué información le gustaria saber?(1-algo, 2-Arbol, 3-Grafo): "))
        if pregunta == 2:
            print("\nCargando información de las fechas ....")
            print('\nInformación sobre el arbol de fechas: \n')        
            print('Altura del arbol: ' + str(controller.indexHeight(cont)))
            print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
            print('Menor Llave: ' + str(controller.minKey(cont)))
            print('Mayor Llave: ' + str(controller.maxKey(cont)))
    elif int(inputs[0]) == 5:
        respuesta = input("Desea ver la info para una fecha específica o rango? ")
        if respuesta == "especifica":
            initialDate = input("Ingrese la fecha que desea usar (YYYY-MM-DD): ")
            cant = int(input("Ingrese la cantidad de taxis que desea ver: "))
            lst = controller.getPointsbydate(cont, initialDate, cant)
        else:
            initialDate = input("Ingrese la fecha que desea usar de inicio (YYYY-MM-DD): ")
            finalDate = input("Ingrese la fecha que desea usar al final (YYYY-MM-DD): ")
            cant = int(input("Ingrese la cantidad de taxis que desea ver: "))
            controller.getPointsbyrange(cont, initialDate, finalDate, cant)
    elif int(inputs[0]) == 6:
        t1 = process_time()
        origin = input("Ingrese la estación inicial: ")
        destination = input("Ingrese la estación Final: ")
        horai = input("Ingrese el rango de hora inicial con formato (HH:MM): ")
        horaf = input("Ingrese el rango de hora final con formato (HH:MM): ")
        controller.Shortway(cont, origin, destination, horai, horaf)
        t2 = process_time()
        print("El tiempo de procesamiento es de: ", t2 - t1)
    else:
        sys.exit(0)
sys.exit(0)
