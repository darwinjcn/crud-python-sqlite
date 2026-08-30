# 🗃️ Sistema CRUD con Python y SQLite

Un sistema de gestión básico **CRUD** (Create, Read, Update, Delete) desarrollado en **Python** utilizando el motor de base de datos **SQLite3**. Este proyecto administra un registro de usuarios (con campos de `id`, `nombre` y `email`) y demuestra las operaciones fundamentales con bases de datos relacionales sin requerir librerías externas.

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **SQLite3** (Módulo nativo de Python)

---

## 📌 Funcionalidades

El proyecto implementa las siguientes funciones principales:

| Operación | Función | Descripción |
|-----------|---------|-------------|
| **Crear** | `crear_usuario(nombre, email)` | Inserta un nuevo registro en la tabla |
| **Leer** | `obtener_registros()` | Devuelve la lista completa de usuarios registrados |
| **Leer** | `obtener_usuario(id)` | Consulta los datos de un usuario específico por ID |
| **Actualizar** | `actualizar_usuario(id, nombre, email)` | Modifica los datos de un usuario existente según su ID |
| **Eliminar** | `eliminar_usuario(id)` | Remueve un usuario según su ID |

---

## 🚀 Instalación y Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/crud-python-sqlite-darwin.git
cd crud-python-sqlite-darwin
```

### 2. Ejecutar el script

No se requieren dependencias externas. Solo ejecuta desde tu terminal:

```bash
python crud-python-sqlite-darwin.py
```

> **Nota:** Al ejecutarse por primera vez, el script generará automáticamente el archivo `database.db` en la carpeta raíz con la estructura de la tabla `usuarios`.

---

## 🗄️ Estructura de la Base de Datos

```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    email TEXT
);
```

---

## 📷 Capturas de Pantalla

### Ejecución del programa
<img src="https://raw.githubusercontent.com/darwinjcn/crud-python-sqlite/main/img/ejecucion.png" alt="Ejecución en Consola" width="600" style="border-radius: 12px;" />

### Estructura de la Base de Datos en SQLite
<img src="https://raw.githubusercontent.com/darwinjcn/crud-python-sqlite/main/img/base-de-datos.png" alt="Tabla Usuarios" width="600" style="border-radius: 12px;" />

---

## 📚 Créditos y Referencias

Este proyecto se desarrolló tomando como guía el tutorial en video:

- **Video:** 72. CRUD Con PYTHON y SQLite
- **Canal:** [Jcva Coder](https://www.youtube.com/watch?v=uLt7y4ciRR0)