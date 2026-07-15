import os
from dotenv import load_dotenv

# Carga las variables del archivo .env al entorno
load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME")
    ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

    UPLOAD_FOLDER = os.path.join("app", "static", "uploads")

    # Validación temprana: si falta una variable, el proyecto no arranca
    @staticmethod
    def validate():
        required = ["SECRET_KEY", "DATABASE_URL", "ADMIN_USERNAME", "ADMIN_PASSWORD"]
        faltantes = [var for var in required if not os.environ.get(var)]
        if faltantes:
            raise RuntimeError(
                f"Faltan variables de entorno en .env: {', '.join(faltantes)}"
            )