from config import NOMBRE_SISTEMA, VERSION

print("=" * 40)
print(f"{NOMBRE_SISTEMA} v{VERSION}")
print("Proyecto iniciado correctamente.")
print("=" * 40)


from gestores.base_datos import BaseDatos

bd = BaseDatos()

vehiculos = bd.cargar_vehiculos()

print("Vehículos cargados:")

for v in vehiculos:
    print(v)
