# Proyecto: Gestor de Notas de Estudiantes
estudiantes = {
    "Ana": 16,
    "Luis": 10,
    "Carlos": 18
}
def agregar_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota (0-20): "))
    estudiantes[nombre] = nota
    print(f"Estudiante {nombre} agregado correctamente.\n")

def mostrar_notas():
    print("--- Lista de Notas ---")
    for nombre, nota in estudiantes.items():
        print(f"{nombre}: {nota}")

def calcular_promedio():
    promedio = sum(estudiantes.values()) / len(estudiantes)
    print(f"Promedio general: {promedio:.2f}")

def eliminar_estudiante():
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    if nombre in estudiantes:
        del estudiantes[nombre]
        print(f"Estudiante {nombre} eliminado correctamente.\n")
    else:
        print("Error: Estudiante no encontrado.\n")

while True:
    print("\n1. Agregar | 2. Ver notas | 3. Estadisticas | 4. Eliminar | 5. Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_notas()
    elif opcion == "3":
        calcular_promedio()
    elif opcion == "4":
        eliminar_estudiante()
    elif opcion == "5":
        break
    else:
        print("Opcion no valida.")

