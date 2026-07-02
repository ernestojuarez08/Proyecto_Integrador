from pathlib import Path

# Carpeta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Archivos JSON
RUTA_VEHICULOS = BASE_DIR / "datos" / "vehiculos.json"
RUTA_HISTORIAL = BASE_DIR / "datos" / "historial.json"

# Informacion del sistema
NOMBRE_SISTEMA = "SmartGate IA"
VERSION = "1.0"
