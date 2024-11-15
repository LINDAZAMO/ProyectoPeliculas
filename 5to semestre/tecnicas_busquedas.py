import pandas as pd
import transformacion_datos_parte2 as td


def filtrado(df):
    c1 = df.promedio >= 90
    c2 = df.carrera == "IN"
    c3 = df.carrera.isin(["IN", "C"])
    # & = AND | = OR
    print(df[c3 & c1])


def filtrado_query(df):
    data = df.query("promedio > 85")
    #se debe poner comillas simple para especificar que esta dentro de una cadena
    data2 = df.query("carrera == 'IN' and promedio > 85")
    data3 = df.query("promedio > 85 and carrera.isin(['IN', 'C'])")
    print(data3)


if __name__ == "__main__":
    df = td.crear_alumnos()

    filtrado(df)
    filtrado_query(df)