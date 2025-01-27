from app import db
from app.models.colaborador import Colaborador
from app.models.proyecto import Proyecto
from app.models.roles import Rol

class ColaboradorProyectosRoles(db.Model):
    __tablename__ = 'Colaborador_Proyectos_Roles'

    id_colaborador = db.Column(db.Integer, db.ForeignKey('Colaborador.id_colaborador'), primary_key=True)
    id_proyecto = db.Column(db.Integer, db.ForeignKey('Proyectos.id_proyecto'), primary_key=True)
    id_rol = db.Column(db.Integer, db.ForeignKey('Roles.id_rol'), primary_key=True)

    # Relaciones
    colaborador = db.relationship('Colaborador', backref=db.backref('proyectos_roles', lazy=True))
    proyecto = db.relationship('Proyecto', backref=db.backref('colaboradores_roles', lazy=True))
    rol = db.relationship('Rol', backref=db.backref('colaboradores_roles', lazy=True))
