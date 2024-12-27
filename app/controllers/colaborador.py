from flask import Blueprint, request, redirect, url_for, flash, render_template, session
from app.models.colaborador import Colaborador  # Importamos el modelo Colaborador
from app.models.roles import Rol
from app import db
from werkzeug.security import generate_password_hash  # Para hashear contraseñas
import uuid  # Para generar tokens únicos
from flask_login import current_user

# Crear un blueprint para el controlador de colaboradores
colaborador_bp = Blueprint('colaborador', __name__)

def validar_sesion():
    """Valida la sesión actual comparando el token de sesión en la base de datos."""
    usuario_id = session.get('usuario_id')
    session_token = session.get('session_token')

    print("DEBUG - Validar Sesión:")
    print(f"Usuario ID: {usuario_id}")
    print(f"Session Token: {session_token}")

    if not usuario_id or not session_token:
        print("DEBUG - Falta usuario_id o session_token")
        return False

    colaborador = Colaborador.query.get(usuario_id)
    if not colaborador or colaborador.session_token != session_token:
        print("DEBUG - Colaborador no encontrado o sesión inválida.")
        return False

    return True

@colaborador_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        usuario = request.form.get('usuario')
        password = request.form.get('password')
        
        # Buscar al colaborador en la base de datos usando el nombre de usuario
        colaborador = Colaborador.query.filter_by(usuario=usuario).first()

        # Verificar si el colaborador existe y si la contraseña es correcta
        if colaborador and colaborador.check_password(password):
            session.clear()  # Limpia cualquier sesión anterior

            # Generar un token único para la sesión
            session_token = str(uuid.uuid4())

            # Iniciar la sesión del usuario
            session['usuario_id'] = colaborador.id_colaborador
            session['rol'] = colaborador.rol.nombre_rol
            session['session_token'] = session_token

            session.modified = True

            # Guardar el token único en la base de datos
            colaborador.session_token = session_token
            db.session.commit()

            print("DEBUG - Sesión después de login:", session)
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('colaborador.dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    # Si la solicitud es GET, renderiza el formulario de inicio de sesión
    return render_template('login.html')

@colaborador_bp.route('/dashboard')
def dashboard():
    if not validar_sesion():
        flash("Sesión no válida. Por favor, inicia sesión nuevamente.", "warning")
        return redirect(url_for('colaborador.login'))

    print("DEBUG - Sesión actual en dashboard:", session)
    return render_template('dashboard.html')


@colaborador_bp.route('/logout', methods=['POST'])
def logout():
    """Cierra la sesión actual y limpia el token en la base de datos."""
    usuario_id = session.get('usuario_id')

    if usuario_id:
        colaborador = Colaborador.query.get(usuario_id)
        if colaborador:
            colaborador.session_token = None
            db.session.commit()

    session.clear()
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('colaborador.login'))

@colaborador_bp.route('/users', methods=['GET', 'POST'])
def users():
    if not validar_sesion():
        flash("Sesión no válida. Por favor, inicia sesión nuevamente.", "warning")
        return redirect(url_for('colaborador.login'))

    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.form.get('nombre')
        apellidos = request.form.get('apellidos')
        area = request.form.get('area')
        cargo = request.form.get('cargo')
        usuario = request.form.get('usuario')
        correo = request.form.get('correo')
        codigo_sap = request.form.get('codigo_sap')
        id_rol = request.form.get('id_rol')  # Capturar id_rol
        password = request.form.get('password')

        if not all([nombre, apellidos, area, cargo, usuario, correo, codigo_sap, id_rol, password]):
            flash("Todos los campos son obligatorios", "warning")
            return redirect(url_for('colaborador.users'))

        # Hashear la contraseña antes de guardarla
        password_hashed = generate_password_hash(password)

        # Crear un nuevo objeto Colaborador y guardarlo en la base de datos
        nuevo_colaborador = Colaborador(
            nombre=nombre,
            apellidos=apellidos,
            area=area,
            cargo=cargo,
            usuario=usuario,
            correo=correo,
            codigo_sap=codigo_sap,
            id_rol=id_rol,
            contraseña=password_hashed
        )
        db.session.add(nuevo_colaborador)
        db.session.commit()

        flash('Usuario guardado exitosamente', 'success')

    roles = Rol.query.all()
    colaboradores = Colaborador.query.all()  # Recuperamos todos los colaboradores para mostrar en la tabla
    return render_template('users.html', colaboradores=colaboradores, roles=roles)

