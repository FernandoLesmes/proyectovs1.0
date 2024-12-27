@colaborador_bp.route('/dashboard')
def dashboard():
    if not validar_sesion():
        flash("Sesión no válida. Por favor, inicia sesión nuevamente.", "warning")
        return redirect(url_for('colaborador.login'))

    print("DEBUG - Sesión actual en dashboard:", session)
    return render_template('dashboard.html', users=current_user)