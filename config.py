from pathlib import Path

# Carpeta principal del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Archivos JSON
DATA_DIR = BASE_DIR / "datos"

VEHICULOS_JSON = DATA_DIR / "vehiculos.json"
REGISTROS_JSON = DATA_DIR / "registros.json"

# Informacion del sistema
NOMBRE_SISTEMA = "SmartGate IA"
VERSION = "1.0"
