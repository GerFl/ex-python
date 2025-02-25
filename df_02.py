import pandas as panda
import mysql.connector

# Genera un dataframe que tenga el promedio diario de los precios del pml
def dataframe_promedios(cursor):
    try:
        cursor.execute('''
            SELECT
                mda.claNodo,
                mda.fecha,
                mda.hora,
                AVG(mda.pml) as precio_promedio_pml,
                AVG(mda.pml_ene) as precio_promedio_pml_ene,
                AVG(mda.pml_per) as precio_promedio_pml_per,
                AVG(mda.pml_cng) as precio_promedio_pml_cng
            FROM MemSch.MemTraMDADet mda

            UNION ALL

            SELECT
                mtr.claNodo,
                mtr.fecha,
                mtr.hora,
                AVG(mtr.pml) as precio_promedio_pml,
                AVG(mtr.pml_ene) as precio_promedio_pml_ene,
                AVG(mtr.pml_per) as precio_promedio_pml_per,
                AVG(mtr.pml_cng) as precio_promedio_pml_cng
            FROM MemSch.MemTraMTRDet mtr
        ''')
        data = cursor.fetchall()

        columns = ['Nodo', 'Fecha', 'Hora', 'Promedio_PML', 'Promedio_PML_ENE', 'Promedio_PML_PER', 'Promedio_PML_CNG']

        dataframe = panda.DataFrame(data, columns = columns)

        return dataframe

    except mysql.connector.Error as e:
        print(f"Error en la consulta de datos: { e }")
        return None
    except Exception as e:
        print(f"Ocurrió un error durante el procesamiento de la información: { e }")
        return None