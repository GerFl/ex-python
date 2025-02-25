import matplotlib.pyplot as plot
import mysql.connector

def graficar_promedio(cursor):
    try:
        # Obtener los registros
        cursor.execute('''
            SELECT
                mda.fecha,
                AVG(mda.pml) AS precio_promedio,
                'MDA' AS origen
            FROM MemSch.MemTraMDADet mda
            GROUP BY mda.fecha

            UNION ALL

            SELECT
                mtr.fecha,
                AVG(mtr.pml) AS precio_promedio,
                'MTR' AS origen
            FROM MemSch.MemTraMTRDet mtr
            GROUP BY mtr.fecha

            ORDER BY fecha;
        ''')
        data = cursor.fetchall()

        # Crear diccionarios para almacenar los precios de MDA y MTR por fecha
        mda_data = {}
        mtr_data = {}

        for registro in data:
            fecha = registro[0]
            precio = registro[1]
            origen = registro[2]
            
            if origen == 'MDA':
                mda_data[fecha] = precio
            else:
                mtr_data[fecha] = precio

        # Calculo de diferencias
        diferencia_promedio = {}
        for fecha in mda_data.keys():
            if fecha in mtr_data:
                mda_precio = mda_data[fecha]
                mtr_precio = mtr_data[fecha]
                diferencia = mda_precio - mtr_precio
                diferencia_promedio[fecha] = diferencia
            else:
                diferencia_promedio[fecha] = mda_data[fecha]    
        
        fechas = sorted(diferencia_promedio.keys())
        diferencias = [diferencia_promedio[fecha] for fecha in fechas]

        plot.figure(figsize=(10, 6))
        plot.plot(fechas, diferencias, label='Diferencia promedio (MDA - MTR)', color='blue', marker='o')

        plot.title('Diferencia promedio diaria del precio entre MDA y MTR (todos los nodos)')
        plot.legend()
        plot.xlabel('Fecha')
        plot.ylabel('Diferencia de precio')
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