# app/controllers/proyecto.py
from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from app.models.proyecto import Proyecto
from app.models.actividades import Actividad
from app.models.colaborador import Colaborador
from app.models.roles import Rol
from app.models.colaborador_proyectos_roles import ColaboradorProyectosRoles  # Importar relación
from app.controllers.colaborador import validar_sesion
from app import db
from sqlalchemy.orm import joinedload

# Crear el blueprint para el controlador de proyectos
proyecto_bp = Blueprint('proyecto', __name__)

# Ruta para ver y crear proyectos
@proyecto_bp.route('/proyectos', methods=['GET', 'POST'])
def proyectos():
    usuario_id = session.get('usuario_id')
    rol = session.get('rol')

    # Validar sesión
    if not validar_sesion():
        flash("Sesión no válida. Por favor, inicia sesión nuevamente.", "warning")
        return redirect(url_for('colaborador.login'))

    if not usuario_id or not rol:
        flash("Por favor, inicia sesión primero.", "warning")
        return redirect(url_for('colaborador.login'))

    if request.method == 'POST':
        # Crear un nuevo proyecto
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        id_lider = request.form.get('id_lider') or usuario_id
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')

        nuevo_proyecto = Proyecto(
            nombre=nombre,
            descripcion=descripcion,
            id_lider=id_lider,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        db.session.add(nuevo_proyecto)
        db.session.commit()

        # Asignar automáticamente a Fernando (Admin) como Admin del proyecto
        admin_rol = Rol.query.filter_by(nombre_rol='Admin').first()
        if admin_rol:
            admin_relacion = ColaboradorProyectosRoles(
                id_colaborador=2,  # Fernando siempre es id_colaborador=2
                id_proyecto=nuevo_proyecto.id_proyecto,
                id_rol=admin_rol.id_rol
            )
            db.session.add(admin_relacion)

        # Asegurar que el usuario actual sea Líder de Proyecto
        lider_rol = Rol.query.filter_by(nombre_rol='Líder de Proyecto').first()
        colaborador = Colaborador.query.get(usuario_id)
        if colaborador and lider_rol and colaborador.id_rol != lider_rol.id_rol:
            colaborador.id_rol = lider_rol.id_rol
            session['rol'] = 'Líder de Proyecto'  # Actualizar en la sesión
            db.session.commit()

        flash('Proyecto creado exitosamente. Ahora eres Líder de Proyecto.', 'success')

    # Filtrar proyectos según el rol
    if rol == 'Admin':
        proyectos = Proyecto.query.all()
    else:
        proyectos = Proyecto.query.filter(
            (Proyecto.id_lider == usuario_id) |
            (Proyecto.colaboradores_roles.any(id_colaborador=usuario_id))
        ).all()

    print("DEBUG - Proyectos cargados:", proyectos)
    colaboradores = Colaborador.query.all()  # Listado de colaboradores
    return render_template('proyectos.html', proyectos=proyectos, colaboradores=colaboradores)


# Ruta para gestionar actividades dentro de un proyecto
@proyecto_bp.route('/proyectos/<int:proyecto_id>/actividades', methods=['GET', 'POST'])
def actividades(proyecto_id):
    usuario_id = session.get('usuario_id')
    rol = session.get('rol')

    if not validar_sesion():
        flash("Sesión no válida. Por favor, inicia sesión nuevamente.", "warning")
        return redirect(url_for('colaborador.login'))

    proyecto = Proyecto.query.get(proyecto_id)
    if not proyecto:
        flash('El proyecto no existe.', 'danger')
        return redirect(url_for('proyecto.proyectos'))

    # Verificar acceso al proyecto
    if rol != 'Admin' and proyecto.id_lider != usuario_id and not ColaboradorProyectosRoles.query.filter_by(id_colaborador=usuario_id, id_proyecto=proyecto_id).first():
        flash('No tienes permiso para acceder a este proyecto.', 'danger')
        return redirect(url_for('proyecto.proyectos'))

    if request.method == 'POST':
        # Crear una nueva actividad
        nombre = request.form.get('nombre')
        descripcion = request.form.get('descripcion')
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        visibilidad = request.form.get('visibilidad')
        id_colaborador = request.form.get('id_colaborador')

        nueva_actividad = Actividad(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            visibilidad=visibilidad,
            id_proyecto=proyecto_id,
            id_colaborador=id_colaborador
        )
        db.session.add(nueva_actividad)
        db.session.commit()
        flash('Actividad agregada exitosamente.', 'success')

    # Filtrar actividades visibles según el rol
    if rol == 'Admin' or proyecto.id_lider == usuario_id:
        actividades = Actividad.query.options(joinedload(Actividad.colaborador)).filter_by(id_proyecto=proyecto_id).all()
    else:
        actividades = Actividad.query.filter_by(id_proyecto=proyecto_id).filter(
            (Actividad.id_colaborador == usuario_id) |
            (Actividad.visibilidad == 'Publica')
        ).options(joinedload(Actividad.colaborador)).all()

    colaboradores = Colaborador.query.all()  # Listado de colaboradores
    return render_template('actividad.html', proyecto=proyecto, actividades=actividades, colaboradores=colaboradores)
