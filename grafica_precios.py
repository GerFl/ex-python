import matplotlib.pyplot as plot
import mysql.connector

# Grafica el precio del Nodo y el precio de la tbfin por fecha y hora
def graficar_precios(cursor):
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

        fechas_horas = []
        precios_nodo = []
        precios_tbfin = []

        for registro in data:
            nodo, fecha, hora, pml, tbfin = registro
            fecha_hora = f"{fecha} {hora}"
            fechas_horas.append(fecha_hora)
            precios_nodo.append(pml)
            precios_tbfin.append(tbfin)


        plot.figure(figsize=(12, 6))
        plot.plot(fechas_horas, precios_nodo, label='Precio Nodo (PML)', color='b', linestyle='-', marker='o')
        plot.plot(fechas_horas, precios_tbfin, label='Precio TBFin', color='r', linestyle='--', marker='x')
        plot.title('Precio del nodo y precio TBFin por fecha y hora')
        plot.legend()
        plot.xlabel('Fecha y Hora')
        plot.ylabel('Precio')
        plot.xticks(rotation=45)
        plot.tight_layout()
        plot.show()

    except mysql.connector.Error as e:
        print(f"Error en la consulta de datos: { e }")
        return None
    except Exception as e:
        print(f"Ocurrió un error durante el procesamiento de la información: { e }")
        return None