import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
dotenv_path = r"C:\Users\Fernando\Documents\proyecto\.env"
load_dotenv(dotenv_path=dotenv_path)


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(24))  # Usa un valor por defecto si no está en .env

print("DEBUG - SQLALCHEMY_DATABASE_URI:", Config.SQLALCHEMY_DATABASE_URI)
print("DEBUG - SECRET_KEY:", Config.SECRET_KEY)

