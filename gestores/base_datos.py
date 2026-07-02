import json
from config import VEHICULOS_JSON
from modelos.vehiculo import Vehiculo


class BaseDatos:

    def cargar_vehiculos(self):

        with open(VEHICULOS_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

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
