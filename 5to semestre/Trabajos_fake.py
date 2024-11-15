import requests
import pandas as pd
from bs4 import BeautifulSoup


def extraer():
    response = requests.get("https://realpython.github.io/fake-jobs/")

    data = {"puesto": [], "empresa": [], "ciudad": [], "fecha": []}

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html5lib")
        print(soup.prettify())
        tarjetas = soup.find_all("div", attrs={"class": "card-content"})

        for item in tarjetas:

            company = item.find("h3", attrs={"class": "subtitle is-6 company"})  # Busca la company
            puesto = item.find("h2", attrs={"class": "title is-5"})  # Buscas el titulo y lo extraes
            location = item.find("p", attrs={"class": "location"})
            fecha = item.find("time")

            print(type(puesto))
            print(company)
            print(location)
            print(fecha)
            print("========")

            data = {"puesto": []}
            data["puesto"].append(puesto.text)
            data["empresa"].append(company.text)
            data["ciudad"].append(location.text)
            data["fecha"].append(location.tect)


        df = pd.DataFrama(data)
        df.to_cvs("datasets/fake-jobs.csv")





if __name__== "__main__":
    extraer()