from gestores.base_datos import BaseDatos
from modelos.registro import RegistroAcceso

class SmartGate:
    def __init__(self):
        self.bd = BaseDatos()
    def procesar_acceso(self, matricula):
        vehiculo = self.bd.buscar_matricula(matricula)
        if vehiculo is None:
            nuevo_registro=RegistroAcceso(
                matricula=matricula,
                autorizado=False,
                motivo="Vehículo no registrado en el sistema"
            )
        elif not vehiculo.activo:
            nuevo_registro=RegistroAcceso(
                matricula=matricula,
                autorizado=False,
                motivo=f"Rechazado - Vehiculo INACTIVO (Propietario: {vehiculo.propietario})"
            )
        else:
            nuevo_registro=RegistroAcceso(
                matricula=matricula,
                autorizado=True,
                motivo=f"Acesso concedido - {vehiculo.tipo} (Propietario: {vehiculo.propietario})"
            )
        self.bd.guardar_nuevo_registro(nuevo_registro)
        return nuevo_registro