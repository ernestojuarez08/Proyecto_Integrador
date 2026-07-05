import random
from datetime import datetime, timedelta
from gestores.base_datos import BaseDatos
from modelos.smartgate import SmartGate

class SimuladorFlujo:

    def __init__(self):
        self.bd = BaseDatos()
        self.gate = SmartGate()

    def generar_registro_simulado(self, matricula, fecha_hora_simulada):
        
        vehiculo = self.bd.buscar_matricula(matricula)
        if vehiculo is None:
            from modelos.registro import RegistroAcceso
            nuevo_registro = RegistroAcceso(matricula, False, "Vehiculo no registrado en el sistema", fecha_hora_simulada)
        elif not vehiculo.activo:
            from modelos.registro import RegistroAcceso
            nuevo_registro = RegistroAcceso(matricula, False, f"Rechazado - Vehiculo INACTIVO (Propietario: {vehiculo.propietario})", fecha_hora_simulada)
        else:
            from modelos.registro import RegistroAcceso
            nuevo_registro = RegistroAcceso(matricula, True, f"Acceso concedido - {vehiculo.tipo} (Propietario: {vehiculo.propietario})", fecha_hora_simulada)

        self.bd.guardar_nuevo_registro(nuevo_registro)
        return nuevo_registro

    def ejecutar_simulacion(self, dias_a_simular=1, cantidad_vehiculos_dia=50):
        vehiculos_registrados = self.bd.cargar_vehiculos()
        
        if not vehiculos_registrados:
            print(" No hay vehículos en vehiculos.json para simular, registra algunos primero")
            return

        lista_matriculas = [v.matricula for v in vehiculos_registrados]
        lista_matriculas.extend(["XYZ999X", "UNK0000", "BAD1234", "ERR8888"])
        fecha_inicio = datetime.now() - timedelta(days=dias_a_simular)
        
        print(f"\n Iniciando simulación masiva de trafico por {dias_a_simular} días")
        registros_creados = 0

        for dia in range(dias_a_simular):
            fecha_actual_simulada = fecha_inicio + timedelta(days=dia)
            
            for _ in range(cantidad_vehiculos_dia):
                hora_actual = random.randint(0, 23)
                
                if hora_actual in [7, 8, 9, 14, 15, 18, 19]:
                    minutos_extra = random.randint(1, 5)
                elif hora_actual in [0, 1, 2, 3, 4, 5]:
                    minutos_extra = random.randint(30, 60)
                else:
                    minutos_extra = random.randint(10, 25)

                minuto_actual = random.randint(0, 59)
                segundo_actual = random.randint(0, 59)
                
                momento_evento = datetime(
                    year=fecha_actual_simulada.year,
                    month=fecha_actual_simulada.month,
                    day=fecha_actual_simulada.day,
                    hour=hora_actual,
                    minute=minuto_actual,
                    second=segundo_actual
                )

                mat_elegida = random.choice(lista_matriculas)
                self.generar_registro_simulado(mat_elegida, momento_evento.strftime("%Y-%m-%d %H:%M:%S"))
                registros_creados += 1

        print(f" Simulación finalizada exitosamente, se generaron {registros_creados} registros historicos.")