import pandas as pd

#int64
#float64
#object- str
#bool
#datetime

def crear_df():
    d = {
        "nombres": ["Pedro", "Maria", "Juan", "Rosa"],
        "edad": [20, 19, 21, 22],
        "salario": [20000.5, 18954.2, 25000.8, 30000.45],
        "Activo": [True, False, True, True],
        "Ingreso": ["2023-03-15", "2023-05-15", "2023-10-15", "2023-11-15"]
    }

    df = pd.DataFrame(d)
    return df


def funciones_fechas(df:pd.DataFrame):
    print(df.Ingreso.dt.day)
    print(df.Ingreso.dt.month)
    print(df.Ingreso.dt.year)
    print(df.Ingreso.dt.hour)
    print(df.Ingreso.dt.minute)
    print(df.Ingreso.dt.dayofweek) # 0 = lunes ... 6 = Domingo
    print(df.Ingreso.dt.day_name())
    print(df.Ingreso.dt.month_name())




if __name__ == "__main__":
    df = crear_df()
    #print(df.dtypes)
    """

    #cambiar datos float a int
    df["salario_int"] = df.salario.astype("int64")
    print(df.dtypes)
    print("\n\n",df)
"""
    print("\n\n\n")
    #Cambiar a fecha
    df["Ingreso"] = pd.to_datetime(df["Ingreso"])
    #print(df.dtypes)


    #nueva funcion
    funciones_fechas(df)
    pd.to_numeric(df.salario, errors="coerce")
    print(df.dtypes)