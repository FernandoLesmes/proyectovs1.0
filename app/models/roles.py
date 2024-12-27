# app/models/roles.py
from app import db

class Rol(db.Model):
    __tablename__ = 'Roles'

    id_rol = db.Column(db.Integer, primary_key=True)
    nombre_rol = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f'<Rol {self.nombre_rol}>'
