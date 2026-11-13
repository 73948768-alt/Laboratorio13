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

agregar_estudiante()
mostrar_notas()
calcular_promedio()