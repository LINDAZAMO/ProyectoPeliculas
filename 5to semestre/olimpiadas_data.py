import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from selenium.webdriver.common.keys import Keys  # Importar Keys
import requests
import pandas as poh
from bs4 import BeautifulSoup

def  Olimpiadas():
    s = Service(ChromeDriverManager().install())

    opc = Options()

    opc.add_argument("--window-size= 1020, 1200")
    #opc.add_argument("headless=True") #Sirve para mandarlo a segundo plano

    navegador = webdriver.Chrome(service=s, options=opc)

    navegador.get("https://www.olympedia.org/statistics/medal/country")
    time.sleep(3)

    cmbYear = navegador.find_element(By.NAME, value="edition_id")
    cmbGender = navegador.find_element(By.NAME,value= "athlete_gender")

    optionsGender = cmbGender.find_elements(By.TAG_NAME, value= "option")
    yearGroup = cmbYear.find_elements(By.TAG_NAME, value="optgroup")
    yearlist = yearGroup[0].find_elements(By.TAG_NAME,value="option")

    data ={"pais":[], "year":[], "gender":[], "oro":[], "plata":[], "bronze":[]}
    for gen in optionsGender[1:]:
        gen.click()
        for year in yearlist[18:]:
            year.click()

            soup = BeautifulSoup(navegador.page_source, "html5lib")
            tabla = soup.find("table", attrs = {"class": "table table-striped"})
            renglones = tabla.find_all("tr")
            for renglon in renglones:
                datos = renglon.find_all("td")
                if datos:
                    pais = datos[0].text
                    oro = datos[2].text
                    plata = datos[3].text
                    bronze = datos[4].text
                    data["pais"].append(pais)
                    data["year"].append(year.text)
                    data["gender"].append(gender.text)
                    data["oro"].append(oro)
                    data["plata"].append(plata)
                    data["bronze"].append(bronze)


                    print(pais)
                    print(oro)
                    print(plata)
                    print(bronze)
                    print(datos)


    navegador.quit()
    df = pd.DataFrame(data)
    df.to_csv("datasets/olimpiadas.csv")








if __name__ == "__main__":
    Olimpiadas()
