import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("datasets/titanic.csv")
    grupos = df.groupby(["Pclass", "Sex"]) #aqui tambien se puede agrupar ppor dos columnas

    #aqui estamos sacando la edad promedio de hombres y de mujeres
    print(grupos.Age.mean())
    #en el ultimo mean se puede poner cualquier agregacion tipo sum, count y asi


    #print(grupos.PassengerId.count())
    grupos_d = grupos.groups
    print(grupos_d[(1, "male")])
    print(grupos.get_group((3, "female")))
