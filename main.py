import os
import mysql.connector
import db_service
from grafica_evolucion_precio import graficar_evolucion_precio
from grafica_promedio import graficar_promedio
from union_tablas import unir_tablas
from df_01 import dataframe_pml_tbfin
from df_02 import dataframe_promedios
from grafica_precios import graficar_precios

# INICIALIZAR CONEXION A LA BD
try:
    # Obtener variables de entorno configuradas en el equipo antes de proceder
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_database = os.getenv("DB_DATABASE")

    print('Iniciando conexión a base de datos...')
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_database
    )
    cursor = conn.cursor()
    print("Conexión establecida")
except mysql.connector.Error as e:
    print(f'Error al conectar a la base de datos: { e }')
    sys.exit(1)

# CREACION DE TABLAS Y SEMBRADO DE INFORMACION
try:
    # CREAR TABLAS
    print('Creando tablas...')
    db_service.create_table_MemTraMDADet(cursor)
    db_service.create_table_MemTraMTRDet(cursor)
    db_service.create_table_MemTraTcDet(cursor)
    db_service.create_table_MemTraTBFinVw(cursor)
    conn.commit()
    print('Todas las tablas fueron creadas exitosamente')

    # SEMBRAR INFORMACION
    print('Ejecutando INSERTS...')
    db_service.seed_MemTraMDADet(conn, cursor)
    db_service.seed_MemTraMTRDet(conn, cursor)
    db_service.seed_MemTraTcDet(conn, cursor)
    db_service.seed_MemTraTBFinVw(conn, cursor)
    conn.commit()
    print('Información guardada exitosamente')
except mysql.connector.Error as e:
    print(f"Error al realizar la carga de datos: { e }")
    conn.rollback()


graficar_evolucion_precio(cursor)
graficar_promedio(cursor)
unir_tablas(cursor)

df_01 = data_frame_pml_tbfin(cursor)
print(df_01)

df_02 = data_frame_promedios(cursor)
print(df_02)

grafica_precios(cursor)


# CERRAR CONEXION
print('Cerrando la conexión...')
cursor.close()
conn.close()

print('Finalizado')