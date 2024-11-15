import pandas as pd


def crearDatos():
    d = {
        "producto": ["A","A","B","B","A","B"],
        "vendedor": ["Carlos","Ana","Carlos","Ana","Carlos","Ana"],
        "cantidad": [10, 15, 20, 30, 10, 20],
        "precio": [20, 20, 15, 15, 20, 15]
    }
    return pd.DataFrame(d)


def resumir(df: pd.DataFrame):
    #Media de cantidad vendida por vendedor y por producto
    #df_resumen = pd.pivot_table(df, values="cantidad", index="producto", columns="vendedor", aggfunc="mean")

    #
    #df_resumen = pd.pivot_table(df, values=["cantidad", "precio"], index="producto", aggfunc="mean")

    #
    df_resumen = pd.pivot_table(df, values=["cantidad", "precio"], index="producto",)



    return df_resumen


if __name__ == "__main__":
    df = crearDatos()

    df_resumen = resumir(df)
    print(df_resumen)
    resumir(df)