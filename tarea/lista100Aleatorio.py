from faker import Faker
import random
import time    

fake = Faker("es_ES")


archivo = open("base_datos.txt", "w")
archivo.write("ID | NOMBRE | PROMEDIO\n")
archivo.write("----------------------\n")

for id in range(1, 10001):         
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


ids_aleatorios = random.sample(range(1, 10006), 100)


inicio = time.perf_counter()

for id_buscar in ids_aleatorios:
    encontrado = False
    for estudiante in lista_estudiantes:
        if estudiante.startswith(str(id_buscar) + " |"):
            partes = estudiante.split(" | ")
            print("ID       →", partes[0])
            print("Nombre   →", partes[1])
            print("Promedio →", partes[2])
            print("----------------------")
            encontrado = True

    if not encontrado:
        print("ID", id_buscar, "→ no encontrado!")


fin = time.perf_counter()

print("----------------------")
print("100 búsquedas realizadas!")
print("Tiempo total:", fin - inicio, "segundos")
print("Tiempo promedio por búsqueda:", (fin - inicio) / 100, "segundos")