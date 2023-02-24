import hashlib


def hash_password(password):
    # Verificar que la contraseña tiene entre 6 y 12 caracteres
    if len(password) < 6 or len(password) > 12:
        raise ValueError("La contraseña debe tener entre 6 y 12 caracteres.")

    # Convertir la contraseña a bytes
    password_bytes = password.encode('utf-8')

    # Calcular el hash de la contraseña
    hash_object = hashlib.sha256(password_bytes)
    hash_bytes = hash_object.digest()

    # Convertir el hash a una cadena de texto alfanumérica de 32 caracteres
    hash_text = ''.join('{:02x}'.format(b) for b in hash_bytes)
    return hash_text

nueva = hash_password(input("dame una contraseña: "))

print(nueva)