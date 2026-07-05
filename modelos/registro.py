from datetime import datetime

class RegistroAcceso:
    def __init__(self, matricula, autorizado, motivo, fecha_hora=None):
        self.matricula = matricula.upper()
        self.autorizado = autorizado
        self.motivo = motivo

        if fecha_hora is None:
            self.fecha_hora= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.fecha_hora= fecha_hora
    
    def __str__(self):
        estado = "AUTORIZADO" if self.autorizado else "RECHAZADO"
        return f'[{self.fecha_hora}] {self.matricula} - {estado}({self.motivo})'
    
    def to_dict(self):
        return {
            "fecha_hora": self.fecha_hora,
            "matricula": self.matricula,
            "autorizado": self.autorizado,
            "motivo": self.motivo
        }
    @classmethod
    def from_dict(cls, datos):
        return cls(
            matricula=datos["matricula"],
            autorizado=datos["autorizado"],
            motivo=datos["motivo"],
            fecha_hora=datos["fecha_hora"]
        )