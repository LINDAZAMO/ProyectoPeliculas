import pandas as pd


#apply() -- aplicar funciones a cada elemento de una columna o fila
#map() -- reemplazar valores en una serie (columna)
#replace() -- reemplazar valores en un dataframe

def crearDF():
    d = {
        "producto": ["A", "B", "C", "D"],
        "precio": [120, 230, 300, 150],
        "origen": ["MX", "USA", "MX","USA"],
        "pregunta1": ["Si", "No", "si", "NO"],
        "pregunta2": ["20", "20", "15", "30"]

    }
    return pd.DataFrame(d)

def precioDescuento(x):
    return x * 0.9

def fun_apply(df: pd.DataFrame):
    #df["PrecioDescuento"] = df.precio.apply(lambda x: x * 0.9)
    df["PrecioDescuento"] = df.precio.apply(precioDescuento)

def clasifica_precio(precio):
    if precio < 150:
        return "Bajo"
    elif precio < 250:
        return "Medio"
    else:
        return "Alto"
def fun_map(df: pd.DataFrame):
    mapa_paises = {
        "MX": "Mexico",
        "USA": "Estados Unidos"
    }
    df["pais"] = df.origen.map(mapa_paises)
    df["clasidicar_precio"] = df.precio.map(clasifica_precio)


def fun_replace(df):
    df.replace({
        "si": "SI",
        "Si": "SI",
        "no": "NO",
        "NO": "NO"}, inplace = True)


if __name__ == "__main__":
    df = crearDF()
    fun_apply(df)
    print(df)
    fun_map(df)
    fun_replace(df)

