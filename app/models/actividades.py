# app/models/actividad.py
from app import db
from app.models.colaborador import Colaborador  # Importamos el modelo Colaborador

class Actividad(db.Model):
    __tablename__ = 'Actividades'
    
    id_actividad = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text)
    fecha_inicio = db.Column(db.Date)
    fecha_fin = db.Column(db.Date)
    visibilidad = db.Column(db.Enum('Publica', 'Privada', 'Limitada'), nullable=False)
    id_proyecto = db.Column(db.Integer, db.ForeignKey('Proyectos.id_proyecto', ondelete="CASCADE"))
    id_colaborador = db.Column(db.Integer, db.ForeignKey('Colaborador.id_colaborador', ondelete="SET NULL"))  # Añade esta columna

    # Relaciones
    colaborador = db.relationship('Colaborador', backref=db.backref('actividades', lazy=True))

    proyecto = db.relationship('Proyecto', backref=db.backref('actividades', cascade="all, delete-orphan"))
    def __repr__(self):
        return f'<Actividad {self.nombre}>'

