import pandas as pd

#estamos haciendo analisis de datos nulos que hay en el dataframe
def checar_nulos(df):
    nulos = df.isnull()
    print(nulos.sum())
    print("Total valores nulos:", nulos.sum().sum())
    print("\nPorcentaje nulos\n")
    print(nulos.sum()/len(df))


def eliminar_nulos_columnas(df):
    #aqui puede eliminar columnas o renglones el dropna
    #siempre se trabaja sobre copias si quiero que elimine el original se pone inplace =
    df_sin_nulos = df.dropna(axis="columns")
    print(df.columns)
    print(df_sin_nulos.columns)


def eliminar_nulos_renglones(df):
    #df_sin_nulos = df.dropna(axis="index")


    #df_sin_nulos = df.dropna(axis="index", subset=["Age"]) #aqui nada mas checa lo que yo le diga o cual columna tipo edad
    #tambien puedo agregar mas de una columna despues de Age

    df_sin_nulos = df.dropna(axis="index", thresh=4) #thresh lo que hace es que conserva los valores X al menos no nulos
    #si tiene por ejemplo menos de 4 no los elimina
    print(len(df.columns))

    print("Datos con nulos:", len(df))
    print("Datos sin nulos:", len(df_sin_nulos))


def cambiar_nulos(df):
    prom_edad = df.Age.mean()
    df.Age = df.Age.fillna(prom_edad)
    #df.Age.fillna(prom_edad)
    print(df.Age.head())

    df.Cabin = df.Cabin.ffill().bfill() #___> ffill(BackwardFill)
    print(df.Cabin)

    df.Cabin = df.Cabin.ffill().ffill()
    print(df.Cabin)

#___> ffill(BackwardFill) se fija en el valor de abajo para sustituir un nulo
#---> ffill(ForwardFill) se fija en el valor de arriba para sustituir un nulo


def verificar_duplicados(df):
    duplicados = df.duplicated()
    print(duplicados.sum())


def eliminar_duplicados(df):
    df_sin_duplicados = df.drop_duplicates()
    print("Total datos original", len(df))
    print("Total datos sin duplicar", len(df_sin_duplicados))



if __name__ == "__main__":
    df = pd.read_csv("datasets/titanic.csv")
    #checar_nulos(df)
    #eliminar_nulos_columnas(df)
    #eliminar_nulos_renglones(df)
    #cambiar_nulos(df)
    #verificar_duplicados(df)
    eliminar_duplicados(df)
