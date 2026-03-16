from faker import Faker
import random
import time                   

fake = Faker("es_ES")


archivo = open("base_datos.txt", "w")
archivo.write("ID | NOMBRE | PROMEDIO\n")
archivo.write("----------------------\n")


ids = list(range(1, 10001))
random.shuffle(ids)

for id in ids:
    nombre = fake.first_name()
    promedio = round(random.uniform(1.0, 10.0), 1)
    archivo.write(str(id) + " | " + nombre + " | " + str(promedio) + "\n")

archivo.close()


archivo = open("base_datos.txt", "a")
archivo.write("10001 | Carlos | 8.5\n")
archivo.write("10002 | Maria | 9.0\n")
archivo.write("10003 | Pedro | 7.5\n")
archivo.write("10004 | Pedro | 7.5\n")
archivo.write("10005 | Pedro | 7.5\n")
archivo.close()


lista_estudiantes = []

archivo = open("base_datos.txt", "r")
for linea in archivo:
    if "|" in linea:  
        lista_estudiantes.append(linea.strip())
archivo.close()

print(str(len(lista_estudiantes)) + " estudiantes cargados!")
print("----------------------")


id_buscar = input("Ingresa el ID que quieres buscar (1-" + str(len(lista_estudiantes)) + "): ")


inicio = time.perf_counter()

encontrado = False
for estudiante in lista_estudiantes:
    if estudiante.startswith(id_buscar + " |"):
        partes = estudiante.split(" | ")
        print("ID       →", partes[0])
        print("Nombre   →", partes[1])
        print("Promedio →", partes[2])
        encontrado = True


fin = time.perf_counter()

if not encontrado:
    print("ID no encontrado!")

print("----------------------")
print("Tiempo de búsqueda:", fin - inicio, "segundos")