from app import db
from app.models.roles import Rol
from werkzeug.security import generate_password_hash, check_password_hash

class Colaborador(db.Model):  # El nombre debe ser 'Colaborador'
    __tablename__ = 'Colaborador'  # Asegúrate de que coincida con el nombre de tu tabla en la base de datos

    id_colaborador = db.Column(db.Integer, primary_key=True)  # 
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    area = db.Column(db.String(100))
    cargo = db.Column(db.String(100))
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    codigo_sap = db.Column(db.String(50), unique=True, nullable=False)
    #rol = db.Column(db.String(20), nullable=False)
    contraseña = db.Column(db.String(255), nullable=False)  # Ajusta para la contraseña encriptada
    session_token = db.Column(db.String(255), nullable=True) 
     # Nueva columna: id_rol como clave foránea
    id_rol = db.Column(db.Integer, db.ForeignKey('Roles.id_rol'), nullable=True)  
    
    # Relación con el modelo Rol
    rol = db.relationship('Rol', backref=db.backref('colaboradores', lazy=True)) # se relizo cambio de l 19 a l22

    # Método para establecer el hash de la contraseña
    def set_password(self, password):
        self.contraseña = generate_password_hash(password)

    # Método para verificar la contraseña proporcionada
    def check_password(self, password):
        return check_password_hash(self.contraseña, password)

