#Vazquez Zamora Linda Jaqueline
#951
#28/10/2024

import pandas as pd

def crear_df():
    d = {'salario': [20000, 80000, 60000, 13000],
         'edad': [40, 20, 10, 30]}
    df = pd.DataFrame(d)
    return df

columnas = ["salario", "edad"]

def min_max(df, columnas):
    for col in columnas:
        max_val = df[col].max()
        min_val = df[col].min()
        df[f'minmax_{col}'] = (df[col] - min_val) / (max_val - min_val)
    return df

def z_score(df, columnas):
    for col in columnas:
        promedio = df[col].mean()
        std_dev = df[col].std()
        df[f'z_{col}'] = (df[col] - promedio) / std_dev
    return df

def escalado_simple(df, columnas):
    for col in columnas:
        max_val = df[col].max()
        df[f'es_{col}'] = df[col] / max_val
    return df


if __name__ == '__main__':
    df = crear_df()

    df = min_max(df, columnas)
    print("DataFrame con Normalización Min-Max:\n", df)

    df = z_score(df, columnas)
    print("\nDataFrame con Normalización Z-Score:\n", df)

    df = escalado_simple(df, columnas)
    print("\nDataFrame con Escalado Simple:\n", df)
