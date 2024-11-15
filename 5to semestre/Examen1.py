import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup


def simulador1():
    return """"
        <body>
        <div class = "producto">
            <h2> Nombre: "Camara digital>
            <p> Precio: "80"</p>
        </div>
        <div class = "producto">
            <h2>Nombre:"smartphone"</h2>
            <p>Precio: "200"</p>
        </div>
    </body>
"""
def busqueda():
    dicc = {"Nombre":[],
            "Precio":[]}
    soup = BeautifulSoup(simulador1, "html5lib")
    divs_ligas= soup.find_all("div",attrs={"class": "producto"})


    for item in divs_ligas:
        nombre = item.find_all("h2")
        precio = item.find_all("p")
        dicc["Nombre"].append(nombre.text)
        dicc["Precio"].append(precio.text)

    data = pd.DataFrame(dicc)
    data.to_csv("ejercicio3")





def simulador2():
    listaw =[]
    s = Service(ChromeDriverManager().install())
    opc = Options

    opc.add_argument("medida de pagina")
    navegador = webdriver.chrome(Service = s, options= opc)
    navegador.get("link de la pagina")
    buscador = navegador.find_element(By.ID, value="busqueda en la pagina")
    buscador.send_keys("productos en la pagina")
    buscador.submint()
    soup = BeautifulSoup(simulador2.page_source, "html5lib")

    divs = soup.find_all("div", attrs = {"class": "producto"})
    for item in divs:
        nom = item.find("h2")
        listaw.append(nom.text)


    return listaw






simulador1()





