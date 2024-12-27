import secrets

secret_key = secrets.token_hex(16)  # Genera una clave secreta de 32 caracteres hexadecimales
print(secret_key)
