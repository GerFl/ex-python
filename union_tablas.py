import mysql.connector

def unir_tablas(cursor):
    try:
        cursor.execute('''
            SELECT
                mdaMtr.*,
                tc.valor
            FROM (
                SELECT
                    'MDA' AS origen,
                    *
                FROM MemSch.MemTraMDADet mda

                UNION ALL

                SELECT
                    'MTR' AS origen,
                    *
                FROM MemSch.MemTraMTRDet mtr
            ) AS mdaMtr
            INNER JOIN MemSch.MemTraTcDet tc
                ON mdaMtr.fecha = tc.fecha
        ''')
        data = cursor.fetchall()

        # Y luego?

    except mysql.connector.Error as e:
    print(f"Error en la consulta de datos: { e }")
    return None