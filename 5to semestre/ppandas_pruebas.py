import pandas as pd

d = {
    'nombres':["juan","pedro","rafael","aylin","maria","guadalupe"],
    'edad':[20,19,21,20,22,21],
    'promedio':[70,85,0,100,90,75]
}

df = pd.DataFrame(d)
#print(df)
print(df.info())#informacion del dataframe
print(" /////////////////////////////////////")
print(df.describe())#saca estadistica de manera rapida
print("//////////////////////////////////////")
print(df.sample())
print(df.shape)
print(df.size)
print(df.columns)
print(df.dtypes)
print(df.index)
print("///////////////////////////////////////")
print(df.head(3))
print("///////////////////////////////////////")
print(df.tail(3))
print("///////////////////////////////////////")
print(df[["promedio", "edad", "edad"]])

#en los atributos no llevan parentesis

titanic_df = pd.read_csv("")
print(titanic_df.sample(10)) #esto es para importar un archivo y depues poner los datos
#tambien se puede hacer una carpeta que contenga todas las imagenes por url en el programa