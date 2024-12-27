from werkzeug.security import generate_password_hash # type: ignore

# Generar el hash de la contraseña
password_hash = generate_password_hash('Fernando123')

# Luego imprime o guarda el hash para insertarlo en tu base de datos
print(password_hash)