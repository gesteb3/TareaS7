# TareaS7
# Proyecto PostgreSQL + Python (Docker)

## Descripción
Este proyecto demuestra cómo conectar Python a una base de datos PostgreSQL utilizando Docker y realizar operaciones DDL básicas (Data Definition Language) directamente desde Python.  
Se crean tablas, se modifican columnas, se agregan restricciones y se eliminan tablas mediante código Python usando la librería `psycopg2`.

---


## Pasos realizados

### 1️Instalación de la librería Python

Antes de conectarse a PostgreSQL, debemos instalar la librería `psycopg2`:

```bash
pip install psycopg2-binary

### Levantar PostgreSQL en Docker
Ejecuta el siguiente comando para levantar PostgreSQL:

```bash
docker run --name postgres-db2 -e POSTGRES_PASSWORD=yourpassword -p 5432:5432 -d postgres:15```
##  Conexión a PostgreSQL desde Python

Se establece la conexión a la base de datos que está corriendo en Docker:

```python
import psycopg2

# Crear conexión
conexion = psycopg2.connect(
    host="localhost",       # Servidor donde corre PostgreSQL (Docker)
    port=5432,              # Puerto de PostgreSQL
    database="postgres",    # Nombre de la base de datos
    user="postgres",        # Usuario
    password="mi_contraseña" # Contraseña
)

# Crear cursor para ejecutar comandos SQL
cursor = conexion.cursor()


El flujo de operaciones del script es el siguiente:

*   **Conexión a la Base de Datos**: Primero, el script se conecta al servidor de PostgreSQL que está corriendo en Docker, utilizando las credenciales y el puerto especificados.
    
*   **Creación de Tablas**: A continuación, ejecuta comandos **DDL** (CREATE TABLE) para crear dos nuevas tablas, **clientes** y **productos**, si no existen previamente.
    
*   **Modificación de la Estructura**: El script realiza varias alteraciones en las tablas existentes. Añade una columna correo, renombra la columna precio a precio\_unitario, elimina la columna edad y agrega una restricción (CHECK) para asegurar que el precio sea siempre positivo.
    
*   **Eliminación de Tabla**: Finalmente, el script borra la tabla productos de la base de datos, limpiando parte de la estructura que se creó.
    
*   **Cierre de Conexión**: Para finalizar, se asegura de cerrar correctamente el cursor y la conexión a la base de datos, liberando los recursos del sistema de forma segura.
