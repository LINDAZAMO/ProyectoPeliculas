import pandas as pd
from transformacion_datos_parte2 import crear_alumnos


def cambiar_indices(df: pd.DataFrame):
    df_modificado = df.set_index("carrera", drop=False)
    return df_modificado


def funcion_loc(df: pd.DataFrame):
    carrera = ["C", "IN"]
    columnas = ["nombre", "promedio"]
    df_res = df.loc[carrera, columnas]
    print(df_res)


if __name__ == "__main__":
    df = crear_alumnos()
    df_modificado = cambiar_indices(df)
    df_reset = df_modificado.reset_index(drop= True)
    funcion_loc(df_modificado)
    #print(df_modificado)
    #print(df_reset)
