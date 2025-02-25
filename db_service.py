import csv
import mysql.connector

# Ruta de los archivos
ruta_memTraMDA = './files/MemTraMDADet.csv'
ruta_memTraMTR = './files/MemTraMTRDet.csv'
ruta_memTraTc = './files/MemTraTcDet.csv'
ruta_memTraTB = './files/MemTraTBFinVw.csv'
ruta_archivo_prueba = './data.csv'

# CREACION DE TABLAS
def create_table_MemTraMDADet(cursor):
    try:
        # Las tablas combinan camelCase, snake_case y PascalCase
        # Deberian seleccionar una convencion para mejorar la consistencia
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MemSch.MemTraMDADet (
                idMDA BIGINT NOT NULL,
                claNodo VARCHAR(10) NOT NULL,
                fecha DATE NOT NULL,
                hora TINYINT NOT NULL,
                pml DECIMAL(10,5),
                pml_ene DECIMAL(10,5),
                pml_per DECIMAL(10,5),
                pml_cng DECIMAL(10,5),
                FechaUltimaMod DATE,
                NombrePcMod VARCHAR(30),
                ClaUsuarioMod INT,
                PRIMARY KEY (claNodo, fecha, hora)
            )
        ''')
    except mysql.connector.Error as e:
        print(f'Error al crear la tabla MemTraMDADet: { e }')
        raise

def create_table_MemTraMTRDet():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MemSch.MemTraMTRDet (
                idMDA BIGINT,
                claNodo VARCHAR(10) NOT NULL,
                fecha DATE NOT NULL,
                hora TINYINT NOT NULL,
                pml DECIMAL(10,5),
                pml_ene DECIMAL(10,5),
                pml_per DECIMAL(10,5),
                pml_cng DECIMAL(10,5),
                FechaUltimaMod DATE,
                NombrePcMod VARCHAR(10),
                ClaUsuarioMod INT,
                PRIMARY KEY (claNodo, fecha, hora)
            )
        ''')
    except mysql.connector.Error as e:
        print(f'Error al crear la tabla MemTraMTRDet: { e }')
        raise

def create_table_MemTraTcDet():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MemSch.MemTraTcDet (
                idTc INT,
                fecha DATE PRIMARY KEY NOT NULL,
                valor DECIMAL(10,6),
                FechaUltimaMod DATE,
                NombrePcMod VARCHAR(30),
                ClaUsuarioMod INT
            )
        ''')
    except mysql.connector.Error as e:
        print(f'Error al crear la tabla MemTraTcDet: { e }')
        raise

def create_table_MemTraTBFinVw():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MemSch.MemTraTBFinVw (
                FECHA DATE,
                TbFin DECIMAL(38,14),
                TbFinTGR DECIMAL(38,9)
            )
        ''')
    except mysql.connector.Error as e:
        print(f'Error al crear la tabla MemTraTBFinVw')
        raise

# LECTURA DE CSV E INSERCIONES
# Abrir el archivo, asumiendo que los encabezados son igual
# al numero de columnas por cada tabla

# MemSch.MemTraMDADet
def seed_MemTraMDADet(conn, cursor):
    try:
        print('Ejecutando INSERT en MemSch.MemTraMDADet...')
        with open(ruta_memTraMDA, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.reader(archivo)
            next(data)
            
            registros = []

            for row in data:
                registros.append(tuple(row[:11]))
            
            query = 'INSERT INTO MemSch.MemTraMDADet (idMDA, claNodo, fecha, hora, pml, pml_ene, pml_per, pml_cng, FechaUltimaMod, NombrePcMod, ClaUsuarioMod) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            cursor.executemany(query, registros)

            print('Registros guardados en MemTraMDADet...')
    except Exception as e:
        print(f'Error al procesar el archivo { ruta_memTraMDA }: { e }')

# MemSch.MemTraMTRDet
def seed_MemTraMTRDet(conn, cursor):
    try:
        print('Ejecutando INSERT en MemSch.MemTraMTRDet...')
        with open(ruta_memTraMTR, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.reader(archivo)
            next(data)
            
            registros = []

            for row in data:
                registros.append(tuple(row[:11]))

            query = 'INSERT INTO MemSch.MemTraMTRDet (idMDA, claNodo, fecha, hora, pml, pml_ene, pml_per, pml_cng, FechaUltimaMod, NombrePcMod, ClaUsuarioMod) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            cursor.executemany(query, registros)

            print('Registros guardados en MemTraMTRDet...')
    except Exception as e:
        print(f'Error al procesar el archivo { ruta_memTraMTR }: { e }')

# MemSch.MemTraTcDet
def seed_MemTraTcDet(conn, cursor):
    try:
        print('Ejecutando INSERT en MemSch.MemTraTcDet...')
        with open(ruta_memTraTc, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.reader(archivo)
            next(data)

            registros = []

            for row in data:
                registros.append(tuple(row[:5]))

            query = 'INSERT INTO MemSch.MemTraTcDet (idTc, fecha, valor, FechaUltimaModa, NombrePcMod, ClaUsuarioMod) VALUES (?, ?, ?, ?, ?, ?)'
            cursor.executemany(query, registros)

            print('Registros guardados en MemTraTcDet...')
    except Exception as e:
        print(f'Error al procesar el archivo { ruta_memTraTc }: { e }')

# MemSch.MemTraTBFinVw
def seed_MemTraTBFinVw(conn, cursor):
    try:
        print('Ejecutando INSERT en MemSch.MemTraTBFinVw...')
        with open(ruta_memTraTB, mode='r', newline='', encoding='utf-8') as archivo:
            data = csv.reader(archivo)
            next(data)

            registros = []

            for row in data:
                registros.append(tuple(row[:3]))

            query = 'INSERT INTO MemSch.MemTraTBFinVw (fecha, TbFin, TbFinTGR) VALUES (?, ?, ?)'
            cursor.executemany(query, registros)

            print('Registros guardados en MemTraTBFinVw...')
    except Exception as e:
        print(f'Error al procesar el archivo { ruta_memTraTB }: { e }')