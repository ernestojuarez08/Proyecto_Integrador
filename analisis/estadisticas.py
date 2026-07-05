import json
from datetime import datetime
from config import REGISTROS_JSON

class ModuloEstadistico:

    def __init__(self):
        self.ruta_registros = REGISTROS_JSON

    def _cargar_historial(self):
        try:
            with open(self.ruta_registros, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def calcular_metricas(self):
        registros = self._cargar_historial()
        total_accesos = len(registros)

        if total_accesos == 0:
            return {
                "total": 0,
                "dias_evaluados": 0,
                "promedio_por_hora": 0,
                "hora_mayor_trafico": "N/A",
                "hora_menor_trafico": "N/A",
                "distribucion_horas": {h: 0 for h in range(24)}
            }

        conteo_por_hora = {h: 0 for h in range(24)}
        dias_unicos = set()

        for reg in registros:
            fecha_hora_str = reg["fecha_hora"]
            try:
                dt = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
                conteo_por_hora[dt.hour] += 1
                dias_unicos.add(dt.date())
            except ValueError:
                continue

        cantidad_dias = len(dias_unicos) if len(dias_unicos) > 0 else 1
        
        hora_pico = max(conteo_por_hora, key=conteo_por_hora.get)
        hora_valle = min(conteo_por_hora, key=conteo_por_hora.get)

        promedio_por_hora = total_accesos / (cantidad_dias * 24)

        return {
            "total": total_accesos,
            "dias_evaluados": cantidad_dias,
            "promedio_por_hora": round(promedio_por_hora, 2),
            "hora_mayor_trafico": f"{hora_pico}:00 hrs ({conteo_por_hora[hora_pico]} accesos totales)",
            "hora_menor_trafico": f"{hora_valle}:00 hrs ({conteo_por_hora[hora_valle]} accesos totales)",
            "distribucion_horas": conteo_por_hora
        }