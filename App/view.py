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
    elif int(inputs[0]) == 6:




    else:
        sys.exit(0)
sys.exit(0)
