from faker import Faker
import random
import time                     

fake = Faker("es_ES")

class Nodo:
    def __init__(self, es_hoja=False):
        self.claves = []
        self.hijos = []
        self.es_hoja = es_hoja
        self.siguiente = None

class ArbolBMas:
    def __init__(self, orden=3):
        self.raiz = Nodo(es_hoja=True)
        self.orden = orden

    def insertar(self, id, nombre, promedio):
        raiz = self.raiz
        if len(raiz.claves) == (2 * self.orden) - 1:
            nueva_raiz = Nodo(es_hoja=False)
            nueva_raiz.hijos.append(self.raiz)
            self._dividir(nueva_raiz, 0)
            self.raiz = nueva_raiz
        self._insertar_no_lleno(self.raiz, id, nombre, promedio)

    def _dividir(self, padre, indice):
        orden = self.orden
        nodo = padre.hijos[indice]
        nuevo_nodo = Nodo(es_hoja=nodo.es_hoja)
        clave_media = nodo.claves[orden - 1]

        if nodo.es_hoja:
            padre.claves.insert(indice, clave_media[0])
        else:
            padre.claves.insert(indice, clave_media)

        padre.hijos.insert(indice + 1, nuevo_nodo)
        nuevo_nodo.claves = nodo.claves[orden:]
        nodo.claves = nodo.claves[:orden - 1]
        if nodo.es_hoja:
            nuevo_nodo.siguiente = nodo.siguiente
            nodo.siguiente = nuevo_nodo
        if not nodo.es_hoja:
            nuevo_nodo.hijos = nodo.hijos[orden:]
            nodo.hijos = nodo.hijos[:orden]

    def _insertar_no_lleno(self, nodo, id, nombre, promedio):
        if nodo.es_hoja:
            nodo.claves.append((id, nombre, promedio))
            nodo.claves.sort(key=lambda x: x[0])
            return
        i = len(nodo.claves) - 1
        while i >= 0 and id < nodo.claves[i]:
            i -= 1
        i += 1
        if len(nodo.hijos[i].claves) == (2 * self.orden) - 1:
            self._dividir(nodo, i)
            if id > nodo.claves[i]:
                i += 1
        self._insertar_no_lleno(nodo.hijos[i], id, nombre, promedio)

    def buscar(self, id):
        return self._buscar(self.raiz, id)

    def _buscar(self, nodo, id):
        if nodo.es_hoja:
            for clave in nodo.claves:
                if clave[0] == id:
                    return clave
            return None
        i = 0
        while i < len(nodo.claves) and id >= nodo.claves[i]:
            i += 1
        return self._buscar(nodo.hijos[i], id)


archivo = open("base_datos.txt", "w")
archivo.write("ID | NOMBRE | PROMEDIO\n")
archivo.write("----------------------\n")

arbol = ArbolBMas(orden=3)

for id in range(1, 10001):
    nombre = fake.first_name()
    promedio = round(random.uniform(1.0, 10.0), 1)
    archivo.write(str(id) + " | " + nombre + " | " + str(promedio) + "\n")
    arbol.insertar(id, nombre, promedio)

archivo.close()
print("10000 estudiantes creados!")
print("----------------------")


id_buscar = int(input("Ingresa el ID que quieres buscar (1-10000): "))


inicio = time.perf_counter()

resultado = arbol.buscar(id_buscar)


fin = time.perf_counter()

if resultado:
    print("ID       →", resultado[0])
    print("Nombre   →", resultado[1])
    print("Promedio →", resultado[2])
else:
    print("ID no encontrado!")

print("----------------------")
print("Tiempo de búsqueda:", fin - inicio, "segundos")