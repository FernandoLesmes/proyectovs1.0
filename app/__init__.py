from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session  # Importar Flask-Session para manejar sesiones
from flask_migrate import Migrate
from config import Config  # Importa la configuración

# Inicializa la base de datos
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Configuración de la aplicación

    print("DEBUG - SECRET_KEY desde __init__.py:", app.config["SECRET_KEY"])

    # Inicializar la base de datos
    db.init_app(app)
    migrate.init_app(app, db)

    
    # Configuración para Flask-Session
    app.config['SESSION_TYPE'] = 'filesystem'  # Almacenar sesiones en el sistema de archivos (puedes usar 'redis' para más escalabilidad)
    app.config['SESSION_PERMANENT'] = False    # La sesión no es permanente
    app.config['SESSION_USE_SIGNER'] = True    # Firmar cookies para mayor seguridad
    app.config['PERMANENT_SESSION_LIFETIME'] = 0 #05/12/2024
    Session(app)  # Inicializa Flask-Session
    

    # Importar y registrar el blueprint de colaboradores
    from app.controllers.colaborador import colaborador_bp
    app.register_blueprint(colaborador_bp)
    
    # Importar y registrar el blueprint de proyectos
    from app.controllers.proyecto import proyecto_bp
    app.register_blueprint(proyecto_bp)

    return app



