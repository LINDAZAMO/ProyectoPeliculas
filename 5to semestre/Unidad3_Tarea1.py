#Vazquez Zamora Linda Jaqueline
#951
#05/11/2024

import pandas as pd

def crear_db():
    dic = {
        "Tienda": ["X", "X", "Y", "Y", "Z", "Z", "X", "Y", "Z"],
        "Producto": ["Arroz", "Frijoles", "Maíz", "Arroz", "Frijoles", "Maíz", "Arroz", "Frijoles", "Maíz"],
        "Categoria": ["Grano", "Grano", "Grano", "Grano", "Grano", "Grano", "Grano", "Grano", "Grano"],
        "Precio": [15, 10, 12, 14, 9, 13, 16, 11, 14],
        "Cantidad Vendida": [100, 50, 70, 90, 60, 80, 110, 55, 75],
        "Calificacion": ["B", "A", "C", "B", "A", "C", "A", "B", "C"]
    }
    df = pd.DataFrame(dic)
    return df

def Asignacion_Codigo(df):
    df["Codigo de Tienda"] = df["Tienda"].map({"X": 1, "Y": 2, "Z": 3})
    df["Calificacion Numerica"] = df["Calificacion"].map({"A": 3, "B": 2, "C": 1})
    print(df)

def Etiquetado(df):
    df["Etiqueta Cantidad"] = df["Cantidad Vendida"].map(lambda x: "Alta" if x > 50 else "Baja" if x < 25 else "Media")
    print(df)

def Total_Ventas(df):
    df["Total Ventas"] = df["Precio"] * df["Cantidad Vendida"]
    print(df)


def Total_Ventas_Tienda(df):
    df["Total Ventas"] = df["Precio"] * df["Cantidad Vendida"]
    ventas_totales = df.groupby("Tienda")["Total Ventas"].sum().reset_index()
    print(ventas_totales)

def Precio_Promedio(df):
    promedio_precios = df.groupby("Tienda")["Precio"].mean().reset_index()
    print(promedio_precios)

def Cantidad_Vendida(df):
    cantidad_vendida = pd.pivot_table(df, values="Cantidad Vendida", index="Tienda", columns="Producto", aggfunc="sum")
    print(cantidad_vendida)

def Total_Ventas_Por_Producto(df):
    df["Total Vendido"] = df["Precio"] * df["Cantidad Vendida"]
    total_ventas = pd.pivot_table(df, values="Total Vendido", index="Producto", columns="Tienda", aggfunc="sum")
    print(total_ventas)


if __name__ == "__main__":
    df = crear_db()
    print("DataFrame")
    print(df)

    print("\nEjercicio 1: Asignar Código y Calificación Numérica")
    Asignacion_Codigo(df)

    print("\nEjercicio 2: Etiquetado de Cantidad Vendida")
    Etiquetado(df)

    print("\nEjercicio 3: Calcular Total de Ventas")
    Total_Ventas(df)

    print("\nEjercicio 4: Total de Ventas por Tienda")
    Total_Ventas_Tienda(df)

    print("\nEjercicio 5: Precio Promedio de Producto por Tienda")
    Precio_Promedio(df)

    print("\nEjercicio 6: Cantidad Vendida por Producto y Tienda")
    Cantidad_Vendida(df)

    print("\nEjercicio 7: Total de Ventas por Tienda y Producto")
    Total_Ventas_Por_Producto(df)
