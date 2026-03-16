from faker import Faker
import random
import time                     

fake = Faker("es_ES")

class Nodo:
    def __init__(self, id, nombre, promedio):
        self.id = id
        self.nombre = nombre
        self.promedio = promedio
        self.izquierda = None
        self.derecha = None

class ArbolABB:
    def __init__(self):
        self.raiz = None
        self.total = 0

    def insertar(self, id, nombre, promedio):
        nodo_nuevo = Nodo(id, nombre, promedio)
        self.total += 1
        
        if self.raiz is None:
            self.raiz = nodo_nuevo
            return

        nodo_actual = self.raiz
        while True:
            if id < nodo_actual.id:
                if nodo_actual.izquierda is None:
                    nodo_actual.izquierda = nodo_nuevo
                    break
                nodo_actual = nodo_actual.izquierda
            else:
                if nodo_actual.derecha is None:
                    nodo_actual.derecha = nodo_nuevo
                    break
                nodo_actual = nodo_actual.derecha

    def buscar(self, id):
        nodo_actual = self.raiz
        while nodo_actual is not None:
            if id == nodo_actual.id:
                return nodo_actual
            elif id < nodo_actual.id:
                nodo_actual = nodo_actual.izquierda
            else:
                nodo_actual = nodo_actual.derecha
        return None

archivo = open("base_datos.txt", "w")
archivo.write("ID | NOMBRE | PROMEDIO\n")
archivo.write("----------------------\n")

arbol = ArbolABB()


ids = list(range(1, 10001))
random.shuffle(ids)

for id in ids:
    nombre = fake.first_name()
    promedio = round(random.uniform(1.0, 10.0), 1)
    archivo.write(str(id) + " | " + nombre + " | " + str(promedio) + "\n")
    arbol.insertar(id, nombre, promedio)

archivo.close()


nuevos = [
    (10001, "Carlos", 8.5),
    (10002, "Maria",  9.0),
    (10003, "Pedro",  7.5),
]

archivo = open("base_datos.txt", "a")
for id, nombre, promedio in nuevos:
    archivo.write(str(id) + " | " + nombre + " | " + str(promedio) + "\n")
    arbol.insertar(id, nombre, promedio)
archivo.close()

print(str(arbol.total) + " estudiantes cargados!")
print("----------------------")


id_buscar = int(input("Ingresa el ID que quieres buscar (1-" + str(arbol.total) + "): "))


inicio = time.perf_counter()

resultado = arbol.buscar(id_buscar)


fin = time.perf_counter()

if resultado:
    print("ID       →", resultado.id)
    print("Nombre   →", resultado.nombre)
    print("Promedio →", resultado.promedio)
else:
    print("ID no encontrado!")

print("----------------------")
print("Tiempo de búsqueda:", fin - inicio, "segundos")