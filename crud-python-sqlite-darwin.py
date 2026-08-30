import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT
    )
    """
)
conn.commit()


# Crear Registro -> C
def crear_usuario(nombre: str, email: str) -> str:
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES(?, ?)", (nombre, email))
    conn.commit()
    return "Usuario Agregado"


# Obtener registros -> R
def obtener_registros() -> list:
    cursor.execute("SELECT id, nombre, email FROM usuarios")
    return cursor.fetchall()


# Actualizar Usuario por id -> U
def actualizar_usuario(id: int, nombre: str, email: str) -> str:
    cursor.execute(
        "UPDATE usuarios SET nombre=?, email=? WHERE id = ?", (nombre, email, id)
    )
    conn.commit()
    return "Usuario actualizado"


# Eliminar Usuario por id -> D
def eliminar_usuario(id: int) -> str:
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    return "Usuario eliminado"


# Leer registro por id
def obtener_usuario(id: int):
    cursor.execute("SELECT id, nombre, email FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    return usuario if usuario else "Usuario no encontrado"


if __name__ == "__main__":
    # Prueba de inserciones
    crear_usuario("Juan", "juan@gmail.com")
    crear_usuario("Marcos", "marcos@gmail.com")
    crear_usuario("Darwin", "darwin@gmail.com")

    # Mostrar registros en consola
    print(obtener_registros())

    conn.close()