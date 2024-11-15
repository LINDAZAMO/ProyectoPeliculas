import pandas as pd
from sqlalchemy import create_engine


def read__data__pandas():
    user = "root"
    password = "12345678"
    server = "localhost"
    db = "escuela"

    #es para saber a que base de datos entrar
    cadena_de_conexion = f"mysql+mysqlconnector://{user}:{password}@{server}/{db}"
    engine = create_engine(cadena_de_conexion)

    #este nos permite conectarnos a la base de datos
    conexion = engine.connect()

    #es la consulta que voy a revisar
    sql = "select * from alumnos where id_carrera = %s" #se puede poner para buscar una vista etc o sea una condicion mas grande
    valores = (1,) #se pone una , porque es una tupla que va del %s

    #es para leer el sql
    #data = pd.read_sql(sql, conexion, params=valores, chunksize=5) #chinksize sirve para saber de cuantos en cuantos va a traer
    #print(data)


    for item in pd.read_sql(sql, conexion, params=valores, chunksize=4):
        print("procesando chunk")
        print(item)


def insertar_data_pandas():
    user = "root"
    password = "12345678"
    server = "localhost"
    db = "escuela"


    cadena_de_conexion = f"mysql+mysqlconnector://{user}:{password}@{server}/{db}"
    engine = create_engine(cadena_de_conexion)
    conexion = engine.connect()

    df = pd.read_csv("datasets/titanic.csv")
    df.to_sql("titanic", conexion, if_exists="replace", index=False, chunksize = 100)

    #el fail es para que marque error
    #el append es para agregar abajo
    #el replace es para quitar y que construya de nuevo
    #si usas lo de fail o replace crea la tabla pero no tiene una llave primaria
    #conexion.commit() #es necesario cuando se haga append

    conexion.close()



if __name__ == "__main__":
    #read__data__pandas()
    insertar_data_pandas()