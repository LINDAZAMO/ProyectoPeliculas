import pandas as pd

def crearDataFrame():
        d = {
            "nombre": ["Juan", "Jorge", "Maria", "Ana", "Pedro"],
            "carrera": ["LC", "LIN", "LIN", "LIN", "LC"],
            "promedio": [90, 100, 95, 100, 85],
            "edad": [20, 19, 20, 19, 20]
        }
        df = pd.DataFrame(d)
        return df

def seleccionar_columna(df):
    c = df.carrera
    print(df.carrera) #esta forma es mas orienta a objetos
    print(type(c))
    print(df["carrera"]) #esta forma es mas tipo diccionarios

def multiples_columnas(df):
  columnas = ["nombre", "carrera", "promedio"]
  df_filter = df[columnas]
  print(type(df_filter))
  print(df_filter)

def filtrar_renglones(df):
    # and ---> & or ----->
    filtrado = print(df.carrera == "LIN") & (df.edad < 20)
    def_filtrado = df[filtrado]
    print(df[filtrado])


def agregar_columnas():
    df["Facultad"] = ["FCA", "FCA", "FCA", "FCA", "FCA"]
    df["MesesEdad"] = [df.edad * 12]
    print(df)


def agregacion(df):
    """
    print(df.promedio.min())
    print(df.promedio.max())
    print(df.promedio.mean())
    print(df.promedio.std())
    print(df.promedio.count())
    """
    print(df.mean(numeric_only= True))


def calcular(df):
    columnas = ["promedo", "edad"]
    maximos = df[columnas].max()
    minimos = df[columnas].min()
    promedios = df[columnas].mean()
    data = [minimos, maximos, promedios]
    indices = ["min", "max", "mean"]
    df_calcular = pd.DataFrame(data, index= indices)
    #print(maximos)
    #print(minimos)
    #print(promedios)
    #print(df_calcular)


def eliminar_columas(df):
    columnas = ["Facultad", "edad"]
    df.drop(columns=columnas, inplace=True) #aqui se elimaria en la original
    #df_eliminados = df.drop(columns= columnas) #esto es para eliminar dentro de la copia no en la variable original
    #print(df_eliminados)
    print(df)


def eliminar_renglones(df):
    indices = [1, 2]
    #df.drop(index= indices, inplace=True)
    #print(df)
    df_copia = df.drop(index=indices) # aqui es igual con una copia
    print(df_copia)


if __name__ == "__main__":
    df = crearDataFrame()
    #seleccionar_columna(df)

    #multiples_columnas(df)

    #filtrar_renglones(df)

    #agregar_columnas(df)

    #agregacion(df)

    #Crear dataframe  a partir de calculos
    #calcular(df)

    #eliminar_columnas(df)

    eliminar_renglones(df)

