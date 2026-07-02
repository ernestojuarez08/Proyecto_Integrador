class Vehiculo:

    def __init__(self, matricula, propietario, tipo, modelo, color, activo):
        self.matricula = matricula
        self.propietario = propietario
        self.tipo = tipo
        self.modelo = modelo
        self.color = color
        self.activo = activo

    def __str__(self):
        return f"{self.matricula} | {self.propietario} | {self.tipo}"
