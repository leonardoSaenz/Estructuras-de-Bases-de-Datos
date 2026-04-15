En este trabajo se busca crear un KD-tree y comparar su eficiencia con la de algoritmos mas rudimentarios a los cuales vamos a denominar de "fuerza bruta"
Lenguaje utilizado Python
Librerias utilizadas (random, math, matplotlib.pyplot as plt, time)

Uso de cada archivo:
Lab2_leonardo_saenz.py: Implementacion del KD-tree, con sus funciones, las cuales son:

generar_direcciones: Busca generar puntos aleatorios en un plano  y agregarlos a una lista simulando direcciones de entrega.
construirArbol: Crear el KD-tree de manera recursiva. organiza los datos segun su valor en la coordenada x o y, tambien toma el punto medio como raiz del arbol.
calcularDistancia: Calcula la distancia entre dos puntos
dentroDelRadio: Verifica si la dos puntos estan a una distancia menor o igual al radio
rangeSearch: Busca todos los puntos del KD-tree que se encuentran dentro de un radio alrededor de puntoComparar. Evita explorar ramas completas del árbol cuando la distancia al plano de división ya supera el radio
puntoMascercano: Encuentra el punto mas cercano del KD-tree a un punto "X". Descarta segun cual sea la rama que mas se ajuste a la busqueda, luego descarta las otras comparando la distancia al plano de division con la mejor distancia encontrada hasta el momento.
puntoMasCercanoFuerzaBruta: Encuentra el punto mas cercano recorriendo todos los puntos de una lista.
visualizar_todo: genera dos graficas usando matplotlib, la primera mostrando el resultado del rangesearch y la segunda el vecino mas cercano

siguiendo la lista de archivos:
pruebas_tiempo_y_Analisis.py:
En este a traves de la funcion rangeSearchFuerzaBruta hace una comparacion de rendimiento de un el algoritmo de fuerza bruta y el de el KD-TREE tanto en la busqueda de el punto mas cercano y el range search.

Luego se busca hacer un analisis de los datos comparando sus eficiencias y como ultimo se da una conclusion breve.
