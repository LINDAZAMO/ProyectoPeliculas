import pandas as pd

def crear_df():
    personas ={
        "salario": [15000, 40000, 70000, 25000],
        "edad": [20, 30, 40, 50]
    }
    df = pd.DataFrame(personas)
    return df


def escalado_simple(df):
    max_salario = df.salario.max()
    max_edad = df.edad.max()
    df["es_salario"] = df.salario/max_salario
    df["es_edad"] = df.edad/max_edad
    print(df)

def min_max(df):
    # X = (Xi - min) / (max - min)
    max_salario = df.salario.max()
    max_edad = df.edad.max()
    min_salario = df.salario.min()
    min_edad = df.edad.min()
    df["minmax_salario"] = (df.salario - min_salario) / (max_salario - min_salario)
    df["minmax_edad"] = (df.edad - min_edad) / (max_edad - min_edad)
    print(df)


def z_core(df):
    # X = (Xi - promedio) / std
    promedio_salario = df.salario.mean()
    std_salario = df.salario.std()
    promedio_edad = df.edad.mean()
    std_edad = df.edad.std()
    df["z_salario"] = (df.salario - promedio_salario) / std_salario
    df["z_edad"] = (df.edad - promedio_edad) / std_edad
    print(df)

if __name__ == "__main__":
    crear_df()
    escalado_simple(df)
    min_max(df)
    z_core(df)
