from config import NOMBRE_SISTEMA, VERSION
from gestores.base_datos import BaseDatos
from modelos.smartgate import SmartGate
from analisis.simulador import SimuladorFlujo

print("=" * 40)
print(f"{NOMBRE_SISTEMA} v{VERSION}")
print("Proyecto iniciado correctamente.")
print("=" * 40)

bd = BaseDatos()
gate = SmartGate()
sim = SimuladorFlujo()

vehiculos = bd.cargar_vehiculos()
print(f"Vehículos cargados en el sistema: {len(vehiculos)}")

for v in vehiculos:
    print(f". - {v}")
print("=" * 40)

while True:
    print("Menú de control de acceso")
    print("1. Validar Matrícula (Simulación de Entrada)")
    print("2. Salir del Sistema")
    opcion = input("Seleccionar una opción (1 o 3): ").strip()

    if opcion == "1":
        matricula = input("Ingresa la matrícula del vehículo: ").strip()

        if not matricula:
            print("Error: La matricula no puede estar vacia")
            continue
        print("Buscando en el sistema y registrando")
        registro_generado = gate.procesar_acceso(matricula)
        print("Resultado en tiempo real:")
        print(registro_generado)

    elif opcion == "2":
        print("Configuración de la Simulación")
        try:
            dias = int(input("Cuantos días hacia atras deseas simular? (Ej. 3): "))
            autos = int(input("Cuantos accesos simular por cada día? (Ej. 100): "))
            sim.ejecutar_simulacion(dias_a_simular=dias, cantidad_vehiculos_dia=autos)
            print("Abre tu archivo registros.json paraver los datos masivos generados")
        except ValueError:
            print("Error, porfavor ingresar numeros enteros validos ")

    elif opcion == "3":
        print(f"Cerrcando {NOMBRE_SISTEMA}")
        break

    else:
        print("Opcion invalida")

