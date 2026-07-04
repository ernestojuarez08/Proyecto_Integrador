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
    
    def to_dict(self):
        return {
            "matricula": self.matricula,
            "propietario": self.propietario,
            "tipo": self.tipo,
            "modelo": self.modelo,
            "color": self.color,
            "activo": self.activo
    }

@classmethod
def from_dict(cls, datos):
        return cls(
            matricula=datos["matricula"],
            propietario=datos["propietario"],
            tipo=datos["tipo"],
            modelo=datos["modelo"],
            color=datos["color"],
            activo=datos["activo"]
        )