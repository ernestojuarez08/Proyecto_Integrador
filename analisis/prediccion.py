from collections import Counter
import json
from config import REGISTROS_JSON

class SimulacionPredictiva:

    def __init__(self, archivo=REGISTROS_JSON):
        self.archivo = archivo

    def cargar_registros(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def analizar(self):
        registros = self.cargar_registros()

        if len(registros) == 0:
            return "No existen registros para realizar la predicción."
        
        horas = []
        for r in registros:
            if "fecha_hora" in r:
                hora = r["fecha_hora"][11:13]
                horas.append(hora)

        if not horas:
            return "No hay datos de horarios válidos."

        contador = Counter(horas)
        hora_pico = max(contador, key=contador.get)
        cantidad = contador[hora_pico]

        # Ajuste de umbrales para que sea realista con el simulador masivo
        if cantidad < 15:
            riesgo = "BAJO"
        elif cantidad < 40:
            riesgo = "MEDIO"
        else:
            riesgo = "ALTO"

        return {
            "hora_pico": f"{hora_pico}:00 hrs",
            "vehiculos": cantidad,
            "riesgo": riesgo
        }