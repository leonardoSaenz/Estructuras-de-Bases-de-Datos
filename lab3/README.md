En este trabajo mi intención es construir un Quadtree a traves de datos aleatorios que seran ubicados en un plano cartesiano.
Aunque se pudo llegar un mejor trabajo se termino construyendo un Quadtree con muchos problemas mucha ineficiencia y funcionalidades a medias

librerias utilizadas:
import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

def generar_direcciones(n):   --> Esta funcion genera una lista de n numeros aleatorios, cada punto es una tupla (x,y)

Class Nodo ():

  xMin, xMax son los limites horizontales de nuestro nodo
  xMin, xMax: límites horizontales
  yMin, yMax: límites verticales
  puntos: lista de puntos que están dentro de un nodo
  hijos: lista de subcuadrantes 
  esHoja: indica si el nodo se sigue diviendo o para

def crearArbol(nodo, direcciones):
  el algoritmo busca dividir el espacio en cuatro partes, divide hasta que el nodo solo tenga 1 o 0 puntos 
def calcularDistancia(punto1, punto2):
  calcula la distancia entre dos puntos 
def buscarVecino(nodo, puntoBuscar):
  a traves de un punto busca el punto mas cercano a esto, tiene un problema, ya que busca hasta la hoja y si este se encuentra con un 
  nodo vacio hoja, para ahi y no sigue buscando, ademas de que no revisa otras posibles opciones por lo que a veces da falsos positivos

def puntoMasCercanoFuerzaBruta(direcciones, punto):
  Busca el punto mas cercano revisdando toda la lista dde puntos, comparando las distancias saca el mejor candidato
def dibujar:
  dibuja la grafica del quadtree


Aprovecho para pedir disculpas, el trabajo me agarro en parciales y la verdad pudo estar mejor hecho, no entendí muy bien el concepto del Quadtree pero esto es lo que pude hacer,
en algún momento del trabajo tuve que volver a empezar porque había hecho las particiones según los puntos y no la mitad del plano, pido perdón y resolveré mis dudas en clase.


  
