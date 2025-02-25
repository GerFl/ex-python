import matplotlib.pyplot as plot
import mysql.connector

def graficar_evolucion_precio(cursor):
    try:
        # Consultar los datos de precios MDA y MTR para el nodo '01ANS-85'
        # De manera separada para obtener ambas lineas
        cursor.execute('''
            SELECT
                mda.fecha,
                mda.pml
            FROM MemSch.MemTraMDADet mda
            WHERE mda.claNodo = '01ANS-85'
            ORDER BY mda.fecha
        ''')
        mda_data = cursor.fetchall()

        cursor.execute('''
            SELECT
                mtr.fecha,
                mtr.pml
            FROM MemSch.MemTraMTRDet mtr
            WHERE mtr.claNodo = '01ANS-85'
            ORDER BY mtr.fecha
        ''')
        mtr_data = cursor.fetchall()

        # Organizar los conjuntos
        fechas_mda = []
        precios_mda = []

        for registro in mda_data:
            fechas_mda.append(registro[0])
            precios_mda.append(registro[1])

        fechas_mtr = []
        precios_mtr = []

        for registro in mda_data:
            fechas_mtr.append(registro[0])
            precios_mtr.append(registro[1])

        # Construccion de la grafica
        plot.figure(figsize=(10, 6))
        # Graficar MDA
        plot.plot(fechas_mda, precios_mda, label='Precio MDA', color='blue', marker='o')
        # Graficar MTR
        plot.plot(fechas_mtr, precios_mtr, label='Precio MTR', color='green', marker='x')

        plot.title('Evolución del precio MDA y MTR del nodo 01ANS-85')
        plot.legend()
        plot.xlabel('Fecha')
        plot.ylabel('Precio')
        plot.xticks(rotation=45)
        plot.grid(True)
        plot.tight_layout()
        plot.show()

    except mysql.connector.Error as e:
        print(f"Error en la consulta de datos: { e }")
        return None
    except Exception as e:
        print(f"Ocurrió un error durante el procesamiento de la información: { e }")
        return None