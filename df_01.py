import pandas as panda
import mysql.connector

# Genera un dataFrame nodo, fecha, hora, pml, tbfin de los datos que el pml sea mayor que la tbfin
def dataframe_pml_tbfin(cursor):
    try:
        cursor.execute('''
            SELECT
                mdaMtr.claNodo,
                mdaMtr.fecha,
                mdaMtr.hora,
                mdaMtr.pml,
                tb.TbFin
            FROM (
                SELECT
                    mda.claNodo,
                    mda.fecha,
                    mda.hora,
                    mda.pml
                FROM MemSch.MemTraMDADet mda

                UNION ALL

                SELECT
                    mtr.claNodo,
                    mtr.fecha,
                    mtr.hora,
                    mtr.pml
                FROM MemSch.MemTraMTRDet mtr
            ) AS mdaMtr
            INNER JOIN MemSch.TraTBFinVw tb
                ON mdaMtr.fecha = tb.fecha
        ''')
        data = cursor.fetchall()

        columns = ['Nodo', 'Fecha', 'Hora', 'PML', 'TBFin']

        dataframe = panda.DataFrame(data, columns = columns)

        dataframe_diferencias = dataframe[dataframe['PML'] > dataframe['TBFin']]

        return dataframe_diferencias[['Nodo', 'Fecha', 'Hora', 'PML', 'TBFin']]

    except mysql.connector.Error as e:
        print(f"Error en la consulta de datos: { e }")
        return None
    except Exception as e:
        print(f"Ocurrió un error durante el procesamiento de la información: { e }")
        return None