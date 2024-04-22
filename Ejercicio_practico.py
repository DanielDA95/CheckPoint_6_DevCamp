class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

usuario1 = Usuario(nombre_usuario="mi_usuario", contrasena="secreta123")

print(f"Nombre de usuario: {usuario1.nombre_usuario}")
print(f"Contraseña: {usuario1.contrasena}")
