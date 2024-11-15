#Vazquez Zamora Linda Jaqueline
#951
#20/10/2024

import pandas as pd

def porcentaje_valores_nulos_columna(df):
    porcentaje_nulos = (df.isnull().sum() / len(df)) * 100
    print("Porcentaje de valores nulos por columna:\n", porcentaje_nulos)
    return porcentaje_nulos

def renglones_duplicados(df):
    duplicados = df.duplicated().sum()
    print("\nNúmero de renglones duplicados:", duplicados)
    return duplicados

def eliminar_columnas_por_nulos(df, porcentaje_maximo):
    if porcentaje_maximo < 0 or porcentaje_maximo > 1:
        print("El porcentaje máximo debe estar entre 0 y 1")
        return []

    nulos_por_columna = df.isnull().sum() / len(df)
    columnas_eliminar = nulos_por_columna[nulos_por_columna >= porcentaje_maximo].index.tolist()
    df.drop(columns=columnas_eliminar, inplace=True)

    print("\nColumnas eliminadas por altos valores nulos:", columnas_eliminar)
    return columnas_eliminar

def rellenar(df, lista, cadena):
    print("\nEjercicio 4:")
    if cadena == "mean":
        for i in lista:
            if pd.api.types.is_numeric_dtype(df[i]):
                prom_edad = df[i].mean()
                df[i] = df[i].fillna(prom_edad)
                print(f"Columna '{i}' rellena usando el promedio:\n", df)
            else:
                print(f"Error: 'mean' no se puede aplicarse a la columna '{i}' que no es numérica.")
    elif cadena == "bfill":
        for i in lista:
            df[i] = df[i].bfill().ffill()
            print(f"Columna '{i}' rellena usando 'bfill':\n", df)
    elif cadena == "ffill":
        for i in lista:
            df[i] = df[i].ffill().bfill()
            print(f"Columna '{i}' rellena usando 'ffill':\n", df)
    else:
        print("No se ha ingresado ninguna de las opciones especificadas")
    return df


def eliminar_renglones_repetidos(df):
    renglones_originales = len(df)
    df_sin_duplicados = df.drop_duplicates()
    renglones_eliminados = renglones_originales - len(df_sin_duplicados)

    print("\nCantidad de renglones eliminados:", renglones_eliminados)
    return renglones_eliminados


if __name__ == "__main__":
    data = {
        "name": [None, "Linda", None, "Jaqueline", None],
        "years": [19, None, 17, None, 20],
    }
    df = pd.DataFrame(data)

    porcentaje_valores_nulos_columna(df)

    renglones_duplicados(df)

    eliminar_columnas_por_nulos(df, 0.5)

    lista_columnas = ["years"]
    metodo = "bfill"
    rellenar(df, lista_columnas, metodo)

    eliminar_renglones_repetidos(df)


