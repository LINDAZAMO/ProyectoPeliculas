import pandas as pd

def crear_carrera():
    carrera = {
        "nombre":["IN", "NI", "C", "A"],
        "creditos":[350, 370, 360, 340],
        "alumnos": [400, 600, 2000, 1000]
    }
    return pd.DataFrame(carrera)



def crear_alumnos2():
    alumnos = {
        "nombre":["Pedro", "Biron", "Sherlyn"],
        "edad":[22, 22, 22],
        "carrera":["A", "IN", "IN",],
        "promedio": [90, 95, 100, ]
    }
    return pd.DataFrame(alumnos)


def crear_alumnos():
    alumnos = {
        "nombre":["Juan", "Jorge", "Aylin", "Maria", "Jose", "NUEVO"],
        "edad":[20, 19, 20, 18, 21, 20],
        "carrera":["C", "IN", "IN", "NI", "C", "-"],
        "promedio":[90, 95, 100, 85, 80, 100]
    }
    return pd.DataFrame(alumnos)


def unir_df():
    df_carrera = crear_carrera()
    df_alumnos = crear_alumnos()
    #how = inner, left, right, outer
    data = pd.merge(df_alumnos, df_carrera, left_on="carrera",
                    how="right",
                    right_on="nombre",
                    suffixes=("_alumnos", "_carrera"))
    print(data)


def concatenar():
    df_alumnos = crear_alumnos()
    df_alumnos2 = crear_alumnos2()

    #data = pd.concat([df_alumnos, df_alumnos2],
              #axis="index", ignore_index=True)

    data_horizontal = pd.concat([df_alumnos, df_alumnos2],
                                axis= "columns", ignore_index=True)

    #print(data)
    print(data_horizontal)



if __name__ == "__main__":
    unir_df()


    concatenar()