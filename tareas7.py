import psycopg2

# Conexión a PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="yourpassword"
)

cursor = conexion.cursor()

# 1. Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    edad INT
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50),
    precio DECIMAL
);
""")
conexion.commit()
print("Tablas creadas correctamente.")

# 2. Agregar columnas nuevas
cursor.execute("ALTER TABLE clientes ADD COLUMN correo VARCHAR(100);")
conexion.commit()
print("Columna 'correo' agregada a clientes.")

# 3. Renombrar columna
cursor.execute("ALTER TABLE productos RENAME COLUMN precio TO precio_unitario;")
conexion.commit()
print("Columna 'precio' renombrada a 'precio_unitario'.")

# 4. Eliminar columna
cursor.execute("ALTER TABLE clientes DROP COLUMN edad;")
conexion.commit()
print("Columna 'edad' eliminada de clientes.")

# 5. Agregar un CHECK
cursor.execute("ALTER TABLE productos ADD CONSTRAINT precio_check CHECK (precio_unitario > 0);")
conexion.commit()
print("Constraint CHECK agregada a productos.")

# 6. Eliminar tabla
cursor.execute("DROP TABLE IF EXISTS productos;")
conexion.commit()
print("Tabla 'productos' eliminada.")

# Cerrar conexión
cursor.close()
conexion.close()
print("Conexión cerrada.")