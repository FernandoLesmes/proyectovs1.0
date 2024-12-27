# models/proyecto.py
from app import db
from app.models.colaborador import Colaborador##este

class Proyecto(db.Model):
    __tablename__ = 'Proyectos'
    
    id_proyecto = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, default=None)
    id_lider = db.Column(db.Integer, default=None)
    fecha_inicio = db.Column(db.Date, default=None)
    fecha_fin = db.Column(db.Date, default=None)


    id_lider = db.Column(db.Integer, db.ForeignKey('Colaborador.id_colaborador'), nullable=False)  # clave foránea hacia Colaborador
    
    # Definir la relación con Colaborador# 16-19
    lider = db.relationship('Colaborador', backref=db.backref('proyectos', lazy=True), foreign_keys=[id_lider])



    def __repr__(self):
        return f'<Proyecto {self.nombre}>'
