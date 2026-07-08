import random
class Sustentabilidad:

    def __init__(self):  # <-- Corregido con doble guion bajo
        self.promedio_referencia = 2.0

    def evaluar(self):
        # Simula el tiempo en segundos que tarda la barrera en abrirse/procesar
        tiempo_promedio = round(random.uniform(1.2, 3.5), 2)

        if tiempo_promedio <= self.promedio_referencia:
            estado = "Eficiente (Menos emisiones de CO2)"
        else:
            estado = "Congestión Leve (Mayor emisión de CO2 en espera)"

        return {
            "tiempo": tiempo_promedio,
            "estado": estado
        }