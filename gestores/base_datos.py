import json
from config import VEHICULOS_JSON, REGISTROS_JSON
from modelos.vehiculo import Vehiculo
from modelos.registro import RegistroAcceso

class BaseDatos:
    def cargar_vehiculos(self):
        try:
            with open(VEHICULOS_JSON, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except (FileExistsError, json.JSONDecodeError):
            return []
        
        vehiculos = []
        for dato in datos:
            vehiculo = Vehiculo(
                dato["matricula"],
                dato["propietario"],
                dato["tipo"],
                dato["modelo"],
                dato["color"],
                dato["activo"],
            )
            vehiculos.append(vehiculo)
        return vehiculos
    def buscar_matricula(self, matricula):
        lista_vehiculos=self.cargar_vehiculos()
        for vehiculo in lista_vehiculos:
            if vehiculo.matricula.upper() == matricula.upper():
                return vehiculo
        return None
    
    def guardar_nuevo_registro(self, registro):
        try:
            with open(REGISTROS_JSON, "r", encoding="utf-8") as archivo:
                historial_datos = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            historial_datos = []
        historial_datos.append(registro.to_dict())

        with open(REGISTROS_JSON, "w", encoding="utf-8") as archivo:
            json.dump(historial_datos, archivo, ensure_ascii=False, indent=4)
